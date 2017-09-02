# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:40:08 2017

@author: LiHongyan
"""

"""This help me to understand the singleton in Python"""

class Singleton:
    
    __singleton = None
    
    def __init__(self):
        pass
    
    """定义该类是一个静态类"""
    @staticmethod
    def get_instance():
        if Singleton.__singleton is None:
            Singleton.__singleton = Singleton()
        return Singleton.__singleton
        

if __name__ == "__main__":
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()
    
    if(s1 == s2):
        print("两个对象是相同的实现")