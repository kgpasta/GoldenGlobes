# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 14:08:36 2015

@author: Kaustubh
"""
import re

proper_noun_regex = "(?:\s*[A-Z][a-z]+)+"

def run_tests(frequency_map, keyword_list, tweet, hostTable, awardTable):
    word_array = tweet['text'].split()
    
    for keyword in keyword_list:
        if tweet['text'].find("hosting") > -1:
            findHosts(tweet['text'], hostTable)
        
        if tweet['text'].find(keyword) > -1:
            findAwardWinners(tweet['text'], keyword, awardTable)
    
    for word in word_array:
        if frequency_map.has_key(word):
            frequency_map[word] += 1
        else:
            frequency_map[word] = 1
        
def findHosts(tweet, table):
    matches = re.findall(proper_noun_regex, tweet)
    for match in matches:
        match = match.strip()
        if match.find("Golden") > -1 or match.find("Globes") > -1:
            continue
        
        if match in table:
            table[match] = table[match] + 1
        else:
            table[match] = 1
        
def findAwardWinners(tweet, award, table):
    matches = re.findall(proper_noun_regex, tweet)
    for match in matches:
        match = match.strip()
        if match in award or match.find("Golden") > -1 or match.find("Globes") > -1:
            continue
        
        if award in table:
            if match in table[award]:
                table[award][match] = table[award][match] + 1
            else:
                table[award][match] = 1
                
        else:
            table[award] = {}
            table[award][match] = 1
        

def processAwards(table):
    for award in table.keys():
        maxkey = max(table[award].iterkeys(), key=lambda x: table[award][x])
        print award + ":" + maxkey 
        
def processHosts(table):
    sortedTable = sorted(table.iterkeys(), key=lambda x: table[x])
    host1 = sortedTable[len(table) - 1]
    host2 = sortedTable[len(table) - 2]
    print "Hosts: " + host1 + " , " + host2
        
        