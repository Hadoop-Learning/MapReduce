#!/usr/bin/python3
# encoding:utf-8

"""
Task: count words
Author: Calvin Xu
"""

import sys

def main():
    """ handle data streaming. """
    for line in sys.stdin:
        words = line.rstrip().split(' ')
        for word in words:
            print(word, "1", sep="\t")


if __name__ == "__main__":
    main()
