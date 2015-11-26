# !/usr/bin/python
#   Written against python 2.7
#   Matasano Problem 6
#
#   Created by 404 on 15/11/26.
#
#   Copyright (c) 2015 404. All rights reserved.

from itertools import combinations
from base64 import b64decode
from operator import itemgetter

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


def xor_singlechar(input_bytes, key_value):
    output = ''

    for char in input_bytes:
        output += chr(ord(char) ^ key_value)

    return output


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


def find_key(ct):
    MaxScores = 0
    MaxScore = 0
    for i in xrange(256):
        mt = ''
        for j in ct:
            mt += chr(ord(j) ^ i)
        Score = fA.englishFreqMatchScore(mt)
        if Score >= MaxScore:
            MaxScore = Score
            find = i

    if MaxScore >= MaxScores:
        MaxScores = MaxScore
        flag_find = find
        flag_MaxScore = MaxScores
        mt = ''
        for j in ct:
            mt += chr(ord(j) ^ find)
        flag_mt = mt

    return chr(flag_find)


def transpose(list_of_chunks):
    max_chunklength = len(list_of_chunks[0])

    result = []

    for position in range(0, max_chunklength):
        new_chunk = ''

        for chunk in list_of_chunks:
            try:
                new_chunk += chunk[position]
            except IndexError:
                break

        result.append(new_chunk)

    return result


def divide(input, denominator):
    result = []
    for i in range(0, len(input), denominator):
        chunk = input[i:i + denominator]
        result.append(chunk)
    return result


def hamming_distance(s1, s2):
    score = 0
    for i in range(len(s1)):
        score += bin(ord(s1[i]) ^ ord(s2[i])).count('1')

    return score


def get_score(keysize):
    haha = ciphertext[:30 * keysize]
    chunks = divide(haha, keysize)

    total_score = 0

    for (x, y) in combinations(chunks, 2):
        total_score += hamming_distance(x, y)

    normalized_score = total_score / keysize

    return normalized_score


def xor(plaintext, key):
    ciphertext = ''
    for i in xrange(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext


ciphertext = b64decode(open('6.txt', 'r').read())

scores = []
for i in xrange(2, 41):
    scores += [(get_score(i), i)]
keysize = min(scores)[1]

key_material = transpose(divide(ciphertext, keysize))
# print str(key_material)

key = ''
for char in key_material:
    best = xor_find_singlechar_key(char)
    key += chr(best['key'])

print xor(ciphertext, key)
