#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2019-10-26
# file: test_filter_getDisjointIntervals.py
# tested with python 2.7.15
# tested with python 3.7.2
##########################################################################################

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

    	X = [0, 0, 1, 1, 1]
    	res = getDisjointIntervals(X)
    	print(res)
    	self.assertTrue(res == [(2, 4, 1)])

    	X = [0, 0, 1, 1, 1, 0, 1]
    	res = getDisjointIntervals(X)
    	print(res)
    	self.assertTrue(res == [(2, 4, 1), (6, 6, 1)])

    	X = [0]
    	res = getDisjointIntervals(X)
    	print(res)
    	self.assertTrue(res == [])

if __name__ == '__main__':

    unittest.main()
