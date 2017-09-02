# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 10:29:33 2017

@author: Li Hongyan
"""


import unittest
import strategy
import sys

sys.path.append('..')

class TestStrategy(unittest.TestCase):
    
    __returnform = {"1":"正常收费","2":"满300返100","3":"打8折"}
    
    def test_cashnormal(self):
        result = 0
        cc = strategy.CashContext(self.__returnform["1"])
        money = 110.5
        result = cc.getresult(money)
        self.assertEqual(result,110.5)
    
    def test_cashreturn(self):
        result = 0
        cc = strategy.CashContext(self.__returnform["2"])
        money = 500.5
        result = cc.getresult(money)
        self.assertEqual(result,400.5)
    
    def test_cashrebate(self):
        result = 0
        cc = strategy.CashContext(self.__returnform["3"])
        money = 110.5
        result = cc.getresult(money)
        self.assertEqual(result,88.4)

if __name__ == "__main__":
    unittest.main()
    
