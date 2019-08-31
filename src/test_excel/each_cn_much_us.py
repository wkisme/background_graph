from src.construct_layer.find_cn_layer import find_cn_layer
from src.construct_layer.find_us_layer import find_us_layer
from src.main import result


def each_cn_much_us(key, chapter, heading, detail, us_data):

    cn_layer = find_cn_layer(key, chapter, heading, detail)
    much_us_layer = find_us_layer(key,  us_data)

    us_layer = cn_layer.copy()
    each_cn_many_us = {}
    del us_layer[2]

    for i, j in much_us_layer.items():
        us_layer.append(j)

        each_cn_many_us[i] = result(cn_layer, us_layer)
        del us_layer[2]
    return each_cn_many_us
