#!/usr/bin/env python
# -*- coding: utf-8 -*-


def paser(args):
    temp = ''
    for value in args:
        if len(value) < 2:
            value = '0' + value
        temp += value
    record = [temp[i * 4: i * 4 + 4] for i in range(len(temp))]
    result = {}
    result['pm2_5'] = int(record[1], 16)
    result['CO2'] = int(record[3], 16)
    result['temperature'] = int(record[7], 16) * 0.1
    result['humidity'] = int(record[8], 16) * 0.1
    return result

