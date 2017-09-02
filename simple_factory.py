# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:58:44 2017

@author: LiHongyan
"""

"""This is to demonstrate the simple factory in Python"""

class Operation:
     
    def getresult(self):
        pass

class OperationAdd(Operation):
    
    def getresult(self):
            result = 0
            result = self.numberA + self.numberB
            return result

class OperationSub(Operation):
    
    def getresult(self):      
        result = 0
        result = self.numberA - self.numberB
        return result

class OperationDiv(Operation):
    
    def getresult(self):
        try:
            result = self.numberA/self.numberB
            return result
        except:
            print ("error:divided by zero")
            return result

class OperationMul(Operation):
    
    def getresult(self):
        result = self.numberA * numberB
        return result
    
    #result = 0

class OperationUndef(Operation):
        
    def getresult(self):
        pass
 
    
class OperationFactory:
    
    operation = {"+":OperationAdd(),"-":OperationSub(),"*":OperationMul(),"/":OperationDiv()}
    
    def createOperate(self,ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op

if __name__ == "__main__":
    print ("please select one of +, -, *, \  as your operator:")
    op = input("operator:")
    try:
        numberA = eval(input("a:"))
        try:
            numberB = eval(input("b:"))
            factory = OperationFactory()
            oper = factory.createOperate(op)
            oper.numberA = numberA
            oper.numberB = numberB
            result = oper.getresult() 
            if result is not None:
                print ("The result is:",result)
            else:
                print ("Please check your operator!") 
        except:
            print ("Please check your input of b")
    except:
        print ("please check your input of a")
    
    
        
        
       