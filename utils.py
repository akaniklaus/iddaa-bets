from itertools import chain

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
