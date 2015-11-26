#   !/usr/bin/python
#   Written against python 2.7
#   Matasano Problem 2
#
#   Created by 404 on 15/11/26.
#
#   Copyright (c) 2015 404. All rights reserved.


c1 = '1c0111001f010100061a024b53535009181c'
c2 = '686974207468652062756c6c277320657965'

m = ''
# Decode with hex 
# Then XOR bytes by bytes
if len(c1) == len(c2):
    for i in xrange(len(c1) / 2):
        t1 = c1.decode('hex')[i]
        t2 = c2.decode('hex')[i]
        m += chr(ord(t1) ^ ord(t2))
# print in hex
print m.encode('hex')
