'''
Created on 28/06/2014

@author: bobbruno
'''


class symbolParser(object):
    '''
    This class will be able to process a series of input lines one by one and
    calculate frequency of each symbol at each position of all lines. That will
    allow us to calculate the population percentages for each symbol in each
    position, i.e.: what percentage of times do I see symbol X in position Y?
    '''

    def __init__(self):
        """
        Creates the parser array to store the symbol stats per position.
        The basic structure is an array of dictionaries, one per position.
        Each dictionary key is a symbol that appeared at that position, and its
        corresponding value is the number of times it was observed there.
        """
        self._symbolDictArray = []

    def processLine(self, line):
        """
        Processes one line of symbols and adds it to the dictionary
        Should return the number of symbols processed
        :param line: line text to be processed as symbols
        :type line: str
        """
        for symbol, pos in ((line[i], i) for i in range(0, len(line))):
            if symbol == '\n':
                continue
            if len(self._symbolDictArray) <= pos:  # Lazy initialization
                self._symbolDictArray.append({})
            self._symbolDictArray[pos][symbol] = (
                     self._symbolDictArray[pos].get(symbol, 0) + 1)
        return len(line)

    def reportStats(self, position):
        """
        Reports the statistcs of the requested position (0-based)as a
        dictionary of symbols and respective percentages (as keys and values in
        the range [0:1]. Non-existing positions will return an empty
        dictionary.
        :param position: Position to return stats about
        :type position: int
        :rtype: dict
        """
        if (position >= len(self._symbolDictArray)) or (position < 0):
            return {}
        totalPosition = float(
                        sum(self._symbolDictArray[position].itervalues()))
        return {key: value / totalPosition for key, value in
                         self._symbolDictArray[position].iteritems()}
