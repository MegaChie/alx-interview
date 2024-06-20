#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics about
status codes count and total file size
"""
import sys


codes = {}
size = 0
limit = 0
try:
    for line in sys.stdin:
        intel = line.split(" ")
        if len(intel[-2]) == 3:
            size += int(intel[-1])
            codes[int(intel[-2])] = codes.get(int(intel[-2]), 1) + 1
            limit += 1
        if limit == 10:
            limit = 0
            print('File size: {}'.format(size))
            for key, value in sort(codes.items()):
                print("{}: {}".format(key, value))
except Exception as wrong:
    pass
finally:
    print('File size: {}'.format(size))
    for key, value in sort(codes.items()):
        print("{}: {}".format(key, value))
