#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from random import uniform

__author__ = 'Francics'


def randomtime(xrand='00:00:00', yrand='23:59:59'):
    """
    生成一个随机时间,可根据在相应区间内生成时间
    :param xrand: 时间段下限
    :param yrand: 时间段上限
    :return: str 'HH:MM:SS'
    """
    if not isinstance(xrand, str):
        raise TypeError('xrand must be str')

    if not isinstance(yrand, str):
        raise TypeError('yrand must be str')

    timereg = re.compile(r'^([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')

    if re.match(timereg, xrand) is None:
        raise ValueError("xrand need like 'HH:MM:SS' and Conform "
                         "to the time specification")

    if re.match(timereg, yrand) is None:
        raise ValueError("yrand need like 'HH:MM:SS' and Conform "
                         "to the time specification")
    # test
    print("xrand:[%s] and yrand:[%s]" % (xrand, yrand))
    if xrand > yrand:
        raise ValueError("xrand need smaller than yrand")
    return "%.2d:%.2d:%.2d" % (uniform(int(xrand[0:2]), int(yrand[0:2])),
                               uniform(int(xrand[3:5]), int(yrand[3:5])),
                               uniform(int(xrand[6:8]), int(yrand[6:8])))


if __name__ == "__main__":
    print("randtime result: %s" % randomtime())
    print("randtime('08:00:00') : %s" % randomtime('08:00:00'))
    print("randtime(yrand='08:00:00'): %s" % randomtime(yrand='08:00:00'))
    print("Error Use:")
    # print(randomtime(yrand = '25:00:00'))
    #print(randomtime(xrand='22:00:00', yrand='20:00:00'))
