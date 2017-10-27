#!/usr/bin/python3
# encoding:utf-8

"""
Task: count words
Author: Calvin Xu
"""

import sys
from operator import itemgetter
from itertools import groupby


def read_data():
    """ read the data. """
    for line in sys.stdin:
        yield line.rstrip().split('\t')


def main():
    """ count the number """
    data = read_data()
    for key, it in groupby(data, itemgetter(0)):
        s = 0
        for e in it:
            s += int(e[1])
        print(key, s, sep="\t")


if __name__ == '__main__':
    main()
