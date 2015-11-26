# !/usr/bin/python
#   Written against python 2.7
#   Matasano Problem 15
#
#   Created by 404 on 15/11/26.
#
#   Copyright (c) 2015 404. All rights reserved.


def pkcs7pad_remove(message):
    last = message[-1]
    length_message = len(message) - ord(last)
    for i in xrange(length_message,len(message)):
	assert(message[i]==last)
    return message[:length_message]

message = 'ICE ICE BABY\x04\x04\x04\x04'
print pkcs7pad_remove(message)
