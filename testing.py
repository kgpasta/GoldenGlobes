# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 14:08:36 2015

@author: Kaustubh
"""
import re

def run_tests(frequency_map, keyword_list, tweet, awardTable):
    word_array = tweet['text'].split()
    
    for keyword in keyword_list:
        if tweet['text'].find(keyword) > -1:
            findAwardWinners(tweet['text'], keyword, awardTable)
    
    for word in word_array:
        if frequency_map.has_key(word):
            frequency_map[word] += 1
        else:
            frequency_map[word] = 1
        
        
        
def findAwardWinners(tweet, award, table):
    matches = re.findall("[A-Z][a-z]+", tweet)
    for match in matches:
        if match in award or match == "Golden" or match == "Globes":
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
        