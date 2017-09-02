# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 08:30:14 2017

@author: LiHongyan
"""

from abc import abstractmethod,ABCMeta
import math

class CashSuper:
    __metaclass = ABCMeta
    
    @abstractmethod
    def acceptcash(self,money):
        pass
    

class CashNormal(CashSuper):
    
    def acceptcash(self,money):
        return money
    
class CashRebate(CashSuper):
    
    __moneyrebate = 1.0
    
    def __init__(self,moneyrebate):
        self.__moneyrebate = moneyrebate
    
    def acceptcash(self,money):
        return money*(self.__moneyrebate)
    

class CashReturn(CashSuper):
    __moneycondition = 0.0
    __moneyreturn = 0.0
    
    def __init__(self,moneycondition,moneyreturn):
        self.__moneycondition = moneycondition
        self.__moneyreturn = moneyreturn
        
    def acceptcash(self,money):
        if money > self.__moneycondition:
            result = money -math.floor(money/self.__moneycondition)*self.__moneyreturn
        return result

class CashContext():
    
    __cs = CashSuper()
    __selectitem = {"正常收费":CashNormal(),"满300返100":CashReturn(300,100),"打8折":CashRebate(0.8)}
    
    def __init__(self,ch):
        if ch in self.__selectitem:
            self.__cs = self.__selectitem[ch]
        else:
            print ("请选择正确的返利类型!")
    
    def getresult(self,money):
        return self.__cs.acceptcash(money)

if __name__ == "__main__":
    totalrprice = 0.0

    returnform = {"1":"正常收费","2":"满300返100","3":"打8折"}
    try:
        price = eval(input("请输入金额:"))
        ch = input("请选择返利模式：1-正常收费，2-满300返100，3-打8折\n")
        try:
            cc = CashContext(returnform[ch])
            totalprice = 0
            totalprice =cc.getresult(price)
            print ("应付款为: " ,totalprice)
        except:
            print ("请选择正确的返利类型!")
    except:
        print ("请输入正确的金额!")

    