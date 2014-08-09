#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db_conn import DB_CONN
from matches import Match
from utils import concat, get_json_data, get_today_id


URL_MATCHES = """http://www.mackolik.com/AjaxHandlers/ProgramDataHandler.ashx?type=6&sortValue=DATE&week=%d&day=-1&sort=-1&sortDir=1&groupId=-1&np=0&sport=1"""


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

x = DB_CONN.cursor()
query = """DELETE * FROM tbl_MatchInfo WHERE weekID!=%d AND weekID!=%d""" % (today_id, (today_id -1))
x.execute(query)
query = """DELETE * FROM tbl_Results WHERE weekID!=%d AND weekID!=%d""" % (today_id, (today_id -1))
x.execute(query)
query = """DELETE * FROM tbl_Ratios WHERE weekID!=%d AND weekID!=%d""" % (today_id, (today_id -1))
x.execute(query)
DB_CONN.commit()

query = """SELECT matchID FROM tbl_MatchInfo WHERE weekID=%d AND was_played=False""" % (today_id -1)
results = x.execute(query)
matches_previous = {}

if results:
  j = get_json_data(URL_MATCHES % (today_id - 1))
  matches_previous = {j['m'][i]['d']: j['m'][i]['m'] for i in range(len(j['m']))}

query = """SELECT matchID FROM tbl_MatchInfo WHERE weekID=%d AND was_played=True""" % today_id
x.execute(query)
results = [row[0] for row in x.fetchall()]

j = get_json_data(URL_MATCHES % today_id)
matches_last = {j['m'][i]['d']: j['m'][i]['m'] for i in range(len(j['m']))}

all_matches = concat(matches_previous.values() + matches_last.values())

for md in concat(matches_previous.values()):
    match = Match(md, weekid=today_id - 1)
    match.save_all()

for md in concat(matches_last.values()):
    match = Match(md, weekid=today_id)
    if not match.matchID in results:
      match.save_all()

update_user_coupon_ratios()

update_winner_coupons()

DB_CONN.close()
