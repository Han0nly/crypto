# !/usr/bin/python
#   Written against python 2.7
#   Matasano Problem 8
#
#   Created by 404 on 15/11/26.
#
#   Copyright (c) 2015 404. All rights reserved.


def divide(input, denominator):
    result = []
    for i in range(0, len(input), denominator):
        chunk = input[i:i + denominator]
        result.append(chunk)
    return result


lines = [line.rstrip().decode('hex') for line in open('8.txt')]
i = 1
for line in lines:
    result = []
    lined = divide(line, 16)
    if len(set(lined)) != 10:
        print 'line%d' % i,
        print line.encode('hex')
    i += 1
