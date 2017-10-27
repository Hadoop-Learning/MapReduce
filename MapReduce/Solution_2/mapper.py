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
        wordsDict = dict()
        for word in words:
            if word in wordsDict:
                wordsDict[word] += 1
            else:
                wordsDict[word] = 1
        
        for word in wordsDict:
            print(word, wordsDict[word], sep="\t")


if __name__ == "__main__":
    main()
