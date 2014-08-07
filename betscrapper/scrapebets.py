import simplejson
import urllib2
import re
#import MySQLdb

URL_DATES = """http://www.mackolik.com/AjaxHandlers/ProgramComboHandler.ashx?sport=1&type=6&sortValue=DATE&day=-1&sortDir=1&groupId=-1&np=0"""
URL_MATCHES = """http://www.mackolik.com/AjaxHandlers/ProgramDataHandler.ashx?type=6&sortValue=DATE&week=%d&day=-1&sort=-1&sortDir=1&groupId=-1&np=0&sport=1"""

class Match(object):
    def __init__(self, md): # md is match_data
        self.date = md[7]
        self.time = md[6]
        self.league = md[26]
        self.team_1 = md[1]
        self.team_2 = md[3]
        self.mbs = md[13]
        self.iy_goals_1 = md[11]
        self.iy_goals_2 = md[12]
        self.ms_goals_1 = md[8]
        self.ms_goals_2 = md[9]
        self.h1 = md[14]
        self.h2 = md[15]
        self.was_played
        self.matchID = int(md[10])
        self.ratios = []
        res = {}
        res['mac'] = md[16:19]
        res['ilk'] = md[33:36]
        res['han'] = md[36:39]
        res['kar'] = md[39:41]
        res['cif'] = md[19:22]
        res['iy'] = md[42:44]
        res['au1'] = md[44:46]
        res['au2'] = md[22:24]
        res['au3'] = md[46:48]
        res['top'] = md[29:33]

        self.ratios = res


def get_json_data(url):
    response = urllib2.urlopen(url)
    j = response.read()
    j = re.sub(r"{\s*(\w+):", r'{"\1":', j)
    j = re.sub(r",\s*(\w+):", r',"\1":', j)
    j = j.replace("'", '"')
    result = simplejson.loads(j)
    return result


def get_results(iy_goals_1, iy_goals_2, ms_goals_1, ms_goals_2, h1=0, h2=0):
    res = {}
    res['mac'] = (ms_goals_1 > ms_goals_2, ms_goals_1 == ms_goals_2, ms_goals_1 < ms_goals_2)
    res['ilk'] = (iy_goals_1 > iy_goals_2, iy_goals_1 == iy_goals_2, iy_goals_1 < iy_goals_2)

    h_goals_1 = ms_goals_1 + h1
    h_goals_2 = ms_goals_2 + h2
    res['han'] = (h_goals_1 > h_goals_2, h_goals_1 == h_goals_2, h_goals_1 < h_goals_2)
    res['kar'] = (ms_goals_1 > 0 and ms_goals_2 > 0, ms_goals_1 == 0 or ms_goals_2 == 0)
    res['cif'] = (ms_goals_1 >= ms_goals_2, ms_goals_1 != ms_goals_2, ms_goals_1 <= ms_goals_2)
    res['iy'] = (iy_goals_1 + iy_goals_2 > 1.5, iy_goals_1 + iy_goals_2 < 1.5)

    total = ms_goals_1 + ms_goals_2
    res['au1'] = (total > 1.5, total < 1.5)
    res['au2'] = (total > 2.5, total < 2.5)
    res['au3'] = (total > 3.5, total < 3.5)
    res['top'] = (total < 2, total >= 2 and total < 4, total >= 4 and total < 7, total >= 7)

    return res


def get_today_id():
    """
        returns the id for today's period
    """
    response = urllib2.urlopen(URL_DATES)
    content = response.read()
    return int(content[6:11])


today_id = get_today_id()

#j = get_json_data(URL_MATCHES % today_id)
#matches_today = {j['m'][i]['d']: j['m'][i]['m'] for i in range(len(j['m']))}

j = get_json_data(URL_MATCHES % (today_id - 1))
matches_yesterday = {j['m'][i]['d']: j['m'][i]['m'] for i in range(len(j['m']))}

    # TODO:
    # database storage




    # conn = MySQLdb.connect(host="localhost",
    #                         user="sportbets",
    #                         passwd="sportbets",
    #                         db="sportbets_db")
    # x = conn.cursor()

    # try:
    #    x.execute(
    #    "INSERT INTO CBE_meterology (Station, DateAP)"
    #    "VALUES (%s,%s)",(data['current_observation']['observation_location']['city'],data['current_observation']['observation_time_rfc822']))
    #    conn.commit()
    # except:
    #    conn.rollback()

    # conn.close()
