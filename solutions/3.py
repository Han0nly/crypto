# coding=utf-8
# !/usr/bin/python
#   Written against python 2.7
#   Matasano Problem 3
#
#   Created by 404 on 15/11/26.
#
#   Copyright (c) 2015 404. All rights reserved.



from operator import itemgetter

# sort character by statistics frequency
character_frequency = {
    'e': 27,
    't': 26,
    'a': 25,
    'o': 24,
    'i': 23,
    'n': 22,
    's': 21,
    'r': 20,
    'h': 19,
    'l': 18,
    'd': 17,
    'c': 16,
    'u': 15,
    'm': 14,
    'f': 13,
    'p': 12,
    'g': 11,
    'w': 10,
    'y': 9,
    'b': 8,
    'v': 7,
    'k': 6,
    'x': 5,
    ' ': 4,
    'j': 3,
    'q': 2,
    'z': 1
}


# define a function XOR the input bytes and the keys in bytes
def xor_singlechar(input_bytes, key_value):
    output = ''

    for char in input_bytes:
        output += chr(ord(char) ^ key_value)

    return output


# calculate the sum of the score of every bytes of possible plaintext.
# so that the max one of them may be the correct one.
def xor_find_singlechar_key(ciphertext):
    candidates = list()

    for key_candidate in range(256):
        total_score = 0
        plaintext_candidate = xor_singlechar(ciphertext, key_candidate)

        for byte in plaintext_candidate:
            char_score = character_frequency.get(byte, 0)
            total_score += char_score

        result = {
            'score': total_score,
            'key': key_candidate,
            'plaintext': plaintext_candidate
        }

        candidates.append(result)
    winner = max(candidates, key=itemgetter('score'))

    return winner


ct = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'.decode('hex')

best = xor_find_singlechar_key(ct)
print best['key']
print best['plaintext']
