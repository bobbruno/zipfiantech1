#!/usr/local/bin/python2.7
# encoding: utf-8
'''

@author:     user_name

@contact:    user_email
'''

import sys
import os

from argparse import ArgumentParser
from Q2 import contentAnalyser

_defaultFile = "../../Data/textfile.txt"
print(__name__)

if __name__ == "__main__":
    # Setup argument parser
    parser = ArgumentParser()
    parser.add_argument('filename', nargs="?")

    # Process arguments
    args = parser.parse_args()

    if args.filename:
        fname = open(args.filename, "r")
    elif not sys.stdin.isatty():
        fname = sys.stdin
    else:
        print "No file specified. Using default"
        fname = open(_defaultFile, "r")

    ctAnl = contentAnalyser()
    ctAnl.anlText(fname)
    totWords, unqWords, wrdList = ctAnl.getWordStats()
    stcCnt, stcLen = ctAnl.getStcStats()
    fname.close()

    print "Total word count: {0}".format(totWords)
    print "Unique word count: {0}".format(unqWords)
    print "Sentence count: {0}".format(stcCnt)
    print "Sentence average length: {0}".format(stcLen)
    print "Word list (sorted by frequency):"
    for key, val in wrdList:
        print "Word '{0}' happened {1} times".format(key, val)
