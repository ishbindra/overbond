#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:14:11 2020

@author: Ishmeet Bindra

"""

import pandas as pd
import json
import unittest
from code import test
import warnings
warnings.simplefilter(action='ignore', category=Warning)

class Test_functions(unittest.TestCase):

    def test_sample(self):
        test ("sample_input.json","code_output.json")
        with open('sample_output.json') as f:
            data = json.load(f)
        self.assertEqual(data, data)


if __name__ == '__main__':
    unittest.main()