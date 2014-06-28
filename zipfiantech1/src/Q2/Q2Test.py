'''
Created on 28/06/2014

@author: bobbruno
'''
import unittest
from Q2 import contentAnalyser


class Test(unittest.TestCase):
    tSent1 = "This is the first test."
    tSent2 = "This: second test"
    tSent3 = "Another one, this can be tricky!!!"

    def setUp(self):
        self.ctAnalyser = contentAnalyser()
        self.ctAnl2 = contentAnalyser()
        self.ctAnalyser.anlSentence(Test.tSent1)
        self.ctAnalyser.anlSentence(Test.tSent2)

    def tearDown(self):
        pass

    def testWordCount(self):
        totWords, uniqueWords, wordList = self.ctAnalyser.getWordStats()
        print wordList
        self.assertEqual(uniqueWords, 6,
                         "Got {0} words instead of 6.".format(uniqueWords))

    def testStcCount(self):
        self.ctAnalyser.anlSentence(Test.tSent3)
        totStcs, avgStcs = self.ctAnalyser.getStcStats()
        self.assertEqual(totStcs, 3,
                         "Expected 3 sentences, got {0}!".format(totStcs))

    def testAnlFile(self):
        with open("../../Data/textfile.txt", "r") as inputFile:
            self.ctAnl2.anlText(inputFile)
        numStcs, stcLen = self.ctAnl2.getStcStats()
        print "Avg sentence len: {0}".format(stcLen)
        numWords, wordList = self.ctAnl2.getWordStats()
        print "Unique words: {0}".format(numWords)
        print(wordList)
        self.assertEqual(numStcs, 16,
                         "Expected 15 sentences, got {0}.".format(numStcs))
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testwordCount']
    unittest.main()
