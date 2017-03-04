# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:23:28 2016

@author: nausheenfatma
"""

class Page():
    def __init__(self):
        self.title=""
        self.text=""
        self.comment=""
        self.ref=""
        self.id=""
        self.wordlist=[]
        self.text_lines=[]
	

    def getTitle(self):
        return self.title
        
    def getText(self):
        return self.text
        
    def getComment(self):
        return self.comment      
        
    def getId(self):
        return self.id  
        
    def getWordlist(self):
        return self.wordlist  

    def gettextLines(self):
        return self.text_lines 
