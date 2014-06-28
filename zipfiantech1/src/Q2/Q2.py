'''
Created on 28/06/2014

@author: bobbruno
'''

import re
import collections
from operator import itemgetter


class contentAnalyser(object):

    def __init__(self, stcSeps=r'[\.!\?]', wrdSeps=r'[,\:;\-\s=\(\)\+]'):
        """
        Constructor for the class
        :param stcSeps: list of sentence separators - regular expression.
        :type stcSeps: str
        :param wrdSeps: list of word separators
        :type wrdSeps:
        """
        self._stcSeps = stcSeps
        self._wrdSeps = wrdSeps
        self._wordCounter = collections.defaultdict(int)
        self._totalWords = 0
        self._totalSentences = 0

    def getWordStats(self):
        """
        returns the total number of words, the number of unique words found and
        the list of words sorted by frequency.
        :rtype: (int, int, [(str, int)]
        """
        wordList = []
        for key, value in sorted(self._wordCounter.iteritems(),
                                  key=itemgetter(1), reverse=True):
            wordList.append((key, value))
        return (self._totalWords, len(self._wordCounter), wordList)

    def getStcStats(self):
        """
        Returns the total number of sentences processed and the average
        sentence length (in words) of all sentences processed, which is the
        total number of words divided by the total number of sentences.
        :rtype: (int, float)
        """
        return (self._totalSentences,
                float(self._totalWords) / float(self._totalSentences))

    def anlSentence(self, sentence):
        """
        Analyses an entire sentence, parsing and counting words. Punctuation is
        ignored.
        :param sentence: the sentence text
        :type sentence: str
        """
        cleanStr = re.sub(self._wrdSeps, " ",
                          re.sub(self._stcSeps, "", sentence))
        for word in cleanStr.split():
            self._wordCounter[word] += 1
            self._totalWords += 1
        else:
            self._totalSentences += 1

    def anlText(self, inputFile):
        """
        Analyses all the text in inputFile, processing sentences as they
        are terminated. Returns when finished processing inputFile
        :param inputFile: input stream to be processed.
        :type inputFile: file
        """
        strBuf = ""
        splitter = re.compile(self._stcSeps)
        for rawLine in inputFile:
            line = rawLine.replace("\n", "")
            if (not splitter.search(line)):  # Don't have a full sentence yet
                strBuf += " " + line
            else:  # Found a sentence end. Get and process the full sentence.
                tempText = strBuf + line
                while splitter.search(tempText):
                    stcList = splitter.split(tempText, 1)
                    self.anlSentence(stcList[0])
                    tempText = stcList[1]  # Store what's left for the next
                strBuf = tempText
        if len(strBuf):             # Process whatever is left at the end.
            self.anlSentence(strBuf)
