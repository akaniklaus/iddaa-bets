from datetime import date, datetime
from db_conn import DB_CONN
from utils import parse_int, parse_float, concat, get_json_data

URL_MATCHES_DETAIL = """http://www.mackolik.com/AjaxHandlers/IddaaHandler.aspx?command=morebets&mac=%d&type=ByLeague&duel="""

BET_ORDER = ['mac', 'ilk', 'han', 'kar', 'cif', 'iy', 'au1', 'au2', 'au3', 'top']

# 1/1     1/X     1/2     X/1     X/X     X/2     2/1     2/X     2/2
IYMS_ORDER = ['IYMS11', 'IYMS10', 'IYMS12', 'IYMS01', 'IYMS00', 'IYMS02', 'IYMS21', 'IYMS20', 'IYMS22']

# 1:0     2:0     2:1     3:0     3:1     3:2     4:0     4:1     4:2     4:3     5+:0    5+:1    5+:2    5+:3    5+:4
# 0:0     1:1     2:2     3:3     4:4     5+:5+        
# 0:1     0:2     1:2     0:3     1:3     2:3     0:4     1:4     2:4     3:4     0:5+    1:5+    2:5+    3:5+    4:5+
SK_ORDER = ['SK10', 'SK20', 'SK21', 'SK30', 'SK31', 'SK32', 'SK40', 'SK41', 'SK42', 'SK43', 'SK50', 'SK51', 'SK52', 'SK53', 'SK54',
            'SK00', 'SK11', 'SK22', 'SK33', 'SK44', 'SK55',
            'SK01', 'SK02', 'SK12', 'SK03', 'SK13', 'SK23', 'SK04', 'SK14', 'SK24', 'SK34', 'SK05', 'SK15', 'SK25', 'SK35', 'SK45']

FULL_BET_ORDER = BET_ORDER + IYMS_ORDER + SK_ORDER


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

    iy_diff = iy_goals_1 - iy_goals_2
    ms_diff = ms_goals_1 - ms_goals_2
    res['IYMS11'] = iy_diff > 0 and ms_diff > 0
    res['IYMS10'] = iy_diff > 0 and ms_diff == 0
    res['IYMS12'] = iy_diff > 0 and ms_diff < 0
    res['IYMS01'] = iy_diff == 0 and ms_diff > 0
    res['IYMS00'] = iy_diff == 0 and ms_diff == 0
    res['IYMS02'] = iy_diff == 0 and ms_diff < 0
    res['IYMS21'] = iy_diff < 0 and ms_diff > 0
    res['IYMS20'] = iy_diff < 0 and ms_diff == 0
    res['IYMS22'] = iy_diff < 0 and ms_diff < 0

    for i in range(6):
        for j in range(6):
            res['SK%d%d' % (i, j)] = ms_goals_1 == i and ms_goals_2 == j
            if i==5:
                res['SK%d%d' % (i, j)] = ms_goals_1 > 5 and ms_goals_2 == j
            if j==5:
                res['SK%d%d' % (i, j)] = ms_goals_1 == i and ms_goals_2 > 5

    res = concat([res[bet] for bet in BET_ORDER] + [[res[bet] for bet in IYMS_ORDER + SK_ORDER]])

    return res


class Match(object):
    def __init__(self, md, weekid): # md is match_data
        self.weekID = weekid
        self.matchID = int(md[10])
        self.detailID = int(md[0])
        self.datetime = datetime.strptime(md[7] + " " + md[6], '%d.%m.%Y %H:%M')
        self.league = md[26]
        self.team_1 = md[1]
        self.team_2 = md[3]
        self.mbs = parse_int(md[13])
        self.iy_goals_1 = parse_int(md[11])
        self.iy_goals_2 = parse_int(md[12])
        if self.iy_goals_1 is None or self.iy_goals_2 is None:
	    self.iy_goals_1 = None
	    self.iy_goals_2 = None
	    self.ms_goals_1 = None
	    self.ms_goals_2 = None
        else:
            self.ms_goals_1 = parse_int(md[8])
            self.ms_goals_2 = parse_int(md[9])

        self.was_played = self.ms_goals_1 is not None
        self.h1 = 0 if md[14] == '' else int(md[14])
        self.h2 = 0 if md[15] == '' else int(md[15])
        self.ratios = []
        res = {}
        res['mac'] = [parse_float(x) for x in md[16:19]]
        res['ilk'] = [parse_float(x) for x in md[33:36]]
        res['han'] = [parse_float(x) for x in md[36:39]]
        res['kar'] = [parse_float(x) for x in md[39:41]]
        res['cif'] = [parse_float(x) for x in md[19:22]]
        res['iy'] = [parse_float(x) for x in md[42:44]]
        res['au1'] = [parse_float(x) for x in md[44:46]]
        res['au2'] = [parse_float(x) for x in md[22:24]]
        res['au3'] = [parse_float(x) for x in md[46:48]]
        res['top'] = [parse_float(x) for x in md[29:33]]
        
        if self.was_played:
            self.results = get_results(self.iy_goals_1, self.iy_goals_2,
                            self.ms_goals_1, self.ms_goals_2, self.h1, self.h2)

        self.ratios = concat([res[bet] for bet in BET_ORDER])
        if self.league != 'DUEL':
            self.fetch_details()


    def fetch_details(self):
	jf = get_json_data(URL_MATCHES_DETAIL % self.detailID)
        
        details = jf[0]

        for key in IYMS_ORDER:
            self.ratios.append(parse_float(details[key]))

        for key in SK_ORDER:
            self.ratios.append(parse_float(details[key]))


    def save_all(self):
        print "saving match %d from week %d" % (self.matchID, self.weekID)
        self.save_ratios()
        self.save_matchinfo()
        if self.was_played:
            self.save_results()


    def save_ratios(self):
        querystart = """REPLACE INTO tbl_Ratios (weekID, matchID, """
        queryvalues = """VALUES ("%d", "%d", """ %\
                        (self.weekID, self.matchID)
        rnames = ""
        rvalues = ""
        has_ratios = False
        for i in range(len(self.ratios)):
            if self.ratios[i]:
                has_ratios = True
                rnames += "r%d, " % (i + 1)
                rvalues += "%.3f, " % self.ratios[i]

        if has_ratios:
            querystart += rnames
            querystart = querystart[:-2] + ") "

            queryvalues += rvalues
            queryvalues = queryvalues[:-2] + ")"

            query = querystart + queryvalues

            DB_CONN.cursor().execute(query)
            DB_CONN.commit()


    def save_matchinfo(self):
        fields = ['datetime', 'league', 'team_1', 'team_2',
                'weekID', 'matchID', 'mbs', 'iy_goals_1', 'iy_goals_2',
                'ms_goals_1', 'ms_goals_2', 'h1', 'h2', 'was_played']


        querystart = """REPLACE INTO tbl_MatchInfo ("""
        queryvalues = """VALUES ("""
        rnames = ""
        rvalues = ""
        for i, f in enumerate(fields):
            val = self.__getattribute__(f)
            if val is not None:
                rnames += "%s, " % f
                if i < 4:
                    rvalues += '"%s", ' % val
                else:
                    rvalues += "%d, " % val


        querystart += rnames
        querystart = querystart[:-2] + ") "

        queryvalues += rvalues
        queryvalues = queryvalues[:-2] + ")"

        query = querystart + queryvalues
        DB_CONN.cursor().execute(query)
        DB_CONN.commit()


    def save_results(self):
        querystart = """INSERT INTO tbl_Results (weekID, matchID, """
        queryvalues = """VALUES ("%s", "%d", """ %\
                        (self.weekID, self.matchID)
        rnames = ""
        rvalues = ""
        for i in range(len(self.results)):
            rnames += "r%d, " % (i + 1)
            rvalues += "%d, " % self.results[i]

        querystart += rnames
        querystart = querystart[:-2] + ") "

        queryvalues += rvalues
        queryvalues = queryvalues[:-2] + ")"

        query = querystart + queryvalues
        
        try:
            DB_CONN.cursor().execute(query)
            DB_CONN.commit()
            # if INSERT succeeds
            # check all related coupons
        except Exception, e:
            return

        self.update_coupons()


    def update_coupons(self):
        """
            it checks all coupons related to this match
            to see if they won
        """
        query = """SELECT bet_index, couponID from tbl_Coupons """ +\
                """WHERE weekID=%d AND matchID=%d AND won IS NULL""" % (self.weekID, self.matchID)
        x = DB_CONN.cursor()
        x.execute(query)
        coupon_rows = x.fetchall()

        loser_coupons = []
        for row in coupon_rows:
            bet_index = row[0]
            couponID = row[1]
            won = self.results[bet_index]
            
            query = """UPDATE tbl_Coupons SET won=%d WHERE couponID=%d AND weekID=%d AND matchID=%d""" % \
                        (won, couponID, self.weekID, self.matchID)
            x.execute(query)
            DB_CONN.commit()
            if not won:
                loser_coupons.append(couponID)

        for couponID in loser_coupons:
                
            query = """UPDATE tbl_UserCoupon SET won=false WHERE couponID=%d""" % couponID
            x.execute(query)
            DB_CONN.commit()

