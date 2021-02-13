#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2021-01-23
# file: test_arrayCompression.py
# tested with python 3.7.6 and numpy 1.20.1
##########################################################################################

'''
--- Example invocations ---
Cd to the directory containing this script and there invoke
$python -m pytest (-v)
where python is your chosen python interpreter or alternatively only call
$pytest
or
$pytest -v
using the default python interpreter on your system.
The -v flag (equal to --verbose) sets the pytest mode to 'verbose'.
-------------------------------------------------------------------------------
To only run the tests in this test file use
$python -m pytest (-v) test_*.py
where test_*.py is the considered unit test script.
-------------------------------------------------------------------------------
plain unittest invocation
$python test_*.py
-------------------------------------------------------------------------------
Tested with pytest version 6.2.2.
'''

import platform
import unittest
import numpy as np

from array_compression import getDisjointIntervals

class TestGetDisjointIntervals(unittest.TestCase):
    """
    Test cases for the getDisjointIntervals function.
    """

    def test_01(self):

        X = [0, 1, 0, 1]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [(1, 1, 1), (3, 3, 1)])

        X = [1, 0, 1, 0]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [(0, 0, 1), (2, 2, 1)])

        X = [0, 0, 1, 1, 1]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [(2, 4, 1)])

        X = [0, 0, 1, 1, 1, 0, 1]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [(2, 4, 1), (6, 6, 1)])

    def test_02(self):
        ''' pathological cases'''
        X = []
        res = getDisjointIntervals(X)
        self.assertTrue(res == [])

        X = [0]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [])

        X = [0, 0]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [])

        X = [0, 0, 0]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [])

        X = [0, 0, 0, 0]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [])

        X = [0, 0, 0, 0, 0]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [])
    
    def test_03(self):

        X = [1, 1]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [(0, 1, 1)])

        X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        res = getDisjointIntervals(X)
        self.assertTrue(res == [(0, 0, 1),
                                (1, 1, 2),
                                (2, 2, 3),
                                (3, 3, 4),
                                (4, 4, 5),
                                (5, 5, 6),
                                (6, 6, 7),
                                (7, 7, 8),
                                (8, 8, 9),
                                (9, 9, 10)])

if __name__ == '__main__':

    print("/////////////////////////////////////////////////////////////////////////////")
    print("Running", __file__)
    print("/////////////////////////////////////////////////////////////////////////////")
    print("Python Interpreter Version =", platform.python_version())
    print("/////////////////////////////////////////////////////////////////////////////")
    print("Start testing ...")
    print("/////////////////////////////////////////////////////////////////////////////")

    unittest.main()
