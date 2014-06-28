'''
Created on 28/06/2014

@author: bobbruno
'''

from Q1 import symbolParser


def printStats(position, stats):
    textToPrint = "Position {0}: (".format(position)
    for key, value in stats.iteritems():
        textToPrint += "'{0}': {1:.1%}, ".format(key, value)
    textToPrint = textToPrint[:-2] + ")"
    print(textToPrint)


if __name__ == '__main__':
    sp = symbolParser()
    nlines = 0
    with open("../../Data/q1data.txt") as f:
        for line in f:
            sp.processLine(line)
            nlines += 1
    print "Processed {0} lines.".format(nlines)
    if (nlines):
        position = 0
        stats = sp.reportStats(position)
        while (stats != {}):
            printStats(position, stats)
            position += 1
            stats = sp.reportStats(position)
