#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-10-29
# file: test_filter_getDisjointIntervals.py
# tested with python 2.7.15
# tested with python 3.7.2
##########################################################################################

'''
Also tested with pytest (version 5.2.2)
cd to the directory containing this script and
then invoke
$python -m pytest
where python is your chosen python interpreter or
alternatively simply call
$pytest
or
$pytest -v
using the default python interpreter.
'''

import os
import sys
import numpy as np
import unittest

from filter import getDisjointIntervals

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

    unittest.main()
