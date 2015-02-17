# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 01:00:58 2015

@author: Kaustubh
"""
import json


def main():
    results = None
    
    with open("gg2013answers.json") as f:
        for line in f:
            results = json.loads(line)
            
    lists = results["unstructured"]
    dicts = results["structured"]
    
    while(True):
        command = raw_input("\nEnter Command: ")
        command_list = command.split()
        
        if len(command_list) <= 1:
            print "Invalid Command"
            continue
        
        arg1 = command_list[0]
        arg2 = " ".join(command_list[1:len(command_list)])
        
        if arg1 == "list":
            if arg2 in lists:
                prettyprint(lists[arg2])
            else:
                print "No such type of unstructured data"
        
        else:
            a = findAward(arg2, dicts)
            if a is not None:
                if arg1 in dicts[a]:
                    prettyprint(dicts[a][arg1])
            else:
                print "No such award exists"
                
    
def prettyprint(dataList):
    if type(dataList) is list:
        for item in dataList:
            print item
            
    else:
        print dataList
        
def findAward(command, dicts):
    for award in dicts.iterkeys():
        if award.lower().find(command) > -1:
            return award
            
    return None
        
        

main()