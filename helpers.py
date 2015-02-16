# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 00:41:32 2015

@author: Kaustubh
"""

def parseNominees(filename):
    nomineeFile = open(filename)
    nominees = []
    for line in nomineeFile:
        nominee = line.strip().lower()
        if nominee not in nominees:
            nominees.append(nominee)

    nomineeFile.close()            
    return nominees
    
def parseNomineeTable(filename):
    nomineeFile = open(filename)
    nominees = {}
    award = "new"
    for line in nomineeFile:
        if len(line.strip()) == 0:
            award = "new"
        elif award == "new":
            nominees[line.strip()] = []
            award = line.strip()
        else: 
            nominees[award].append(line.strip().lower())

    nomineeFile.close()            
    return nominees