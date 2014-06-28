'''
Created on 28/06/2014

@author: bobbruno
'''
import unittest
from Q1 import symbolParser


class Test(unittest.TestCase):
    param = "L#$KJ#()JSEFS(DF)(SD*F"
    param2 = "#KJ$H#K$JH@#K$JHD)SF"

    def testLineProcessingSize(self):
        symbolP = symbolParser()
        result = symbolP.processLine(Test.param)
        self.assertEqual(result, len(Test.param),
                         "Reported size ({0}) does not match param size ({1})"
                                .format(result, len(Test.param)))

    def testProcessStats(self):
        symbolP = symbolParser()
        symbolP.processLine(Test.param)
        symbolP.processLine(Test.param2)
        result = symbolP.reportStats(1)
        self.assertEqual(result["K"], 0.5, "'K' should have 50%, has {0}".format(result["K"]))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()