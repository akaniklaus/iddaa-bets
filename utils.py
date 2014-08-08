from itertools import chain
import simplejson
import urllib2
import re

URL_DATES = """http://www.mackolik.com/AjaxHandlers/ProgramComboHandler.ashx?sport=1&type=6&sortValue=DATE&day=-1&sortDir=1&groupId=-1&np=0"""


def concat(ls):
    return [i for i in chain.from_iterable(ls)]


def parse_int(s):
    try:
        res = int(s)
    except Exception:
        res = None
    return res


def parse_float(s):
    try:
        res = float(s)
        assert(res)
    except Exception:
        res = None
    return res

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
