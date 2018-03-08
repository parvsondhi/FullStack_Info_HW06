from collections import namedtuple

def dict_to_obj(d):
    for k,v in d.items():
        if isinstance(v, dict):
            d[k] = dictToObject(v)
    return namedtuple('object', d.keys())(*d.values())