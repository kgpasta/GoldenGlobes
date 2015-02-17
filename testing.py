# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 14:08:36 2015

@author: Kaustubh
"""
import re

proper_noun_regex = "(?:\s*[A-Z][a-z]+)+"

def run_tests(frequency_map, keyword_list, stop_list, tweet, host_table, nominee_table, award_table):
    #word_array = tweet['text'].split()
    
    normal_tweet = tweet['text'].lower()
    if normal_tweet.find("hosting") > -1:
        findHosts(tweet['text'], host_table)
        
    matches = re.findall(proper_noun_regex,tweet['text'])
    for match in matches:
        match = match.strip().lower()
        if match not in stop_list and match in nominee_table:
            if match in award_table:
                award_table[match] = award_table[match] + 1
            else:
                award_table[match] = 1
#    for word in word_array:
#        if frequency_map.has_key(word):
#            frequency_map[word] += 1
#        else:
#            frequency_map[word] = 1
        
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
            
def processNominees(mention_table,  nominee_table):
    winners = {}
    for key in nominee_table.iterkeys():
        maxMentions = 0
        winner = None
        for nominee in nominee_table[key]:
            if nominee in mention_table and mention_table[nominee] > maxMentions:
                maxMentions = mention_table[nominee]
                winner = nominee
        winners[key] = winner
        print key + " : " + winner
    return winners
        
def processHosts(table):
    sortedTable = sorted(table.iterkeys(), key=lambda x: table[x])
    host1 = sortedTable[len(sortedTable) - 1]
    host2 = sortedTable[len(sortedTable) - 2]
    print "Hosts: " + host1.lower() + " , " + host2.lower()
   
#def populateTable(tweet, award, nominee_list, table, stop_list):
#    matches = re.findall(proper_noun_regex, tweet)
#    for match in matches:
#        match = match.strip().lower()
#        if match in nominee_list:        
#            if award in table:
#                if match in table[award]:
#                    table[award][match] = table[award][match] + 1
#                else:
#                    table[award][match] = 1
#                    
#            else:
#                table[award] = {}
#                table[award][match] = 1
    
        
        