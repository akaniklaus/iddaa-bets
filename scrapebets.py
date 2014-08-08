#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson
import urllib2
import re
from db_conn import DB_CONN
from matches import Match
from utils import concat


URL_DATES = """http://www.mackolik.com/AjaxHandlers/ProgramComboHandler.ashx?sport=1&type=6&sortValue=DATE&day=-1&sortDir=1&groupId=-1&np=0"""
URL_MATCHES = """http://www.mackolik.com/AjaxHandlers/ProgramDataHandler.ashx?type=6&sortValue=DATE&week=%d&day=-1&sort=-1&sortDir=1&groupId=-1&np=0&sport=1"""


def get_json_data(url):
    response = urllib2.urlopen(url)
    j = response.read()
    j = re.sub(r"{\s*(\w+):", r'{"\1":', j)
    j = re.sub(r",\s*(\w+):", r',"\1":', j)
    j = j.replace("'", '"')
    result = simplejson.loads(j)
    return result


def get_today_id():
    """
        returns the id for today's period
    """
    response = urllib2.urlopen(URL_DATES)
    content = response.read()
    return int(content[6:11])


def update_winner_coupons():
    x = DB_CONN.cursor()
    query = """SELECT couponID from tbl_UserCoupon WHERE won IS NULL"""
    x.execute(query)
    user_coupon_rows = x.fetchall()
    # TODO: check this
    for row in user_coupon_rows:
        couponID = row[0]
        query = """SELECT * from tbl_Coupons WHERE won IS NULL AND couponID=%d""" % couponID
        x.execute(query)
        results = x.fetchall()
        
        if len(results) == 0:
            query = """UPDATE tbl_UserCoupon SET won=true WHERE couponID=%d""" % couponID
            x.execute(query)
            DB_CONN.commit()


def update_user_coupon_ratios():
    x = DB_CONN.cursor()
    query = """SELECT couponID FROM tbl_UserCoupon WHERE ratio IS NULL"""
    x.execute(query)
    user_coupon_rows = x.fetchall()
    for row in user_coupon_rows:
        couponID = row[0]
        query = """SELECT weekID, matchID, bet_index FROM tbl_Coupons WHERE couponID=%d""" % couponID
        x.execute(query)
        results = x.fetchall()
        ratio = 1
        for row in results:
            weekID, matchID, bet_index = row
            query = """SELECT r%d FROM tbl_Ratios WHERE weekID=%d AND matchID=%d""" %\
                        (bet_index + 1, weekID, matchID)
            x.execute(query)
            ratio *= x.fetchone()[0]

        
        query = """UPDATE tbl_UserCoupon SET ratio=%f WHERE couponID=%d""" %\
                (ratio, couponID)
        x.execute(query)
        DB_CONN.commit()


today_id = get_today_id()

j = get_json_data(URL_MATCHES % today_id)
matches_last = {j['m'][i]['d']: j['m'][i]['m'] for i in range(len(j['m']))}

j = get_json_data(URL_MATCHES % (today_id - 1))
matches_previous = {j['m'][i]['d']: j['m'][i]['m'] for i in range(len(j['m']))}

all_matches = concat(matches_previous.values() + matches_last.values())

for md in concat(matches_previous.values()):
    match = Match(md, weekid=today_id - 1)
    match.save_all()

for md in concat(matches_last.values()):
    match = Match(md, weekid=today_id)
    match.save_all()

update_user_coupon_ratios()

update_winner_coupons()

DB_CONN.close()