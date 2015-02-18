# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 00:41:32 2015

@author: Kaustubh
"""

#Generate list of nominees
def parseNominees(nomineeTable):
    nominees = []
    for key in nomineeTable.iterkeys():
        nominees = nominees + nomineeTable[key]
        
    return nominees
    
#Parse input file to get nominee mappings
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

    nominees["Cecil B. Demille Award"] = []
    nomineeFile.close()            
    return nominees

#Parse input file to get presenter mappings
def parsePresenterList(filename):
    presenterFile = open(filename)
    presenters = {}
    award = "new"
    for line in presenterFile:
        line = line.strip().encode('ascii','ignore')
        if len(line) == 0:
            award = "new"
        elif award == "new":
            presenters[line] = []
            award = line
        else:
            presenters[award].append(line.lower())
            
    presenterFile.close()
    return presenters

#Parse Red carpet awards
#def parseRedCarpet(filename):
#	redCarpetFile = open(filename)
#	redCarpet = {}
#	for line in redCarpetFile:
#		li=line.strip()
#		if not li.startswith("#"):
#			redCarpet[line].append(li)
#
#	redCarpetFile.close()
#	return redCarpet
#
#def parseRedCarpet(filename):
#    redCarpetFile = open(filename)
#    redCarpet = {}
#    category = "new"
#    for line in redCarpetFile:
#        line = line.strip().encode('ascii','ignore')
#        if len(line) == 0:
#            category = "new"
#        elif category == "new":
#            redCarpet[line] = []
#            category = line
#        else:
#            redCarpet[category].append(line.lower())
#            
#    redCarpetFile.close()
#    return redCarpet
