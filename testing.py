# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 14:08:36 2015

@author: Kaustubh
"""
import re

#universal regex expressions
proper_noun_regex = "(?:\s*[A-Z][a-z]+)+"
quote_regex = '"[^"]+"'

#Main run tests function, normalizes and takes out stop words
def run_tests(frequency_map, special_table, stop_list, tweet, host_table, nominee_table, award_table, jokeTable):
    #word_array = tweet['text'].split()
    tweet['text'] = tweet['text'].decode('unicode_internal').encode('ascii','ignore')
    
    normal_tweet = tweet['text'].lower()
    if normal_tweet.find("hosting") > -1:
        findHosts(tweet['text'], host_table)
        
    if normal_tweet.find("demille") > -1:
        findHosts(tweet['text'], special_table)
        
    if normal_tweet.find("lol") > -1 or normal_tweet.find("hahaha") > -1:
        jokes = re.findall(quote_regex, tweet['text'])
        for joke in jokes:
            extractFunny(tweet['text'], jokeTable, joke)
        
    #Proper noun frequencies
    matches = re.findall(proper_noun_regex,tweet['text'])
    for match in matches:
        match = str(match.strip().lower())
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
        
#Find name of hosts in tweet, add to table
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
          
#Find name of nominee in tweet, add to table
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
    return winners
     
#Find most popular host names in Table
def processHosts(table):
    sortedTable = sorted(table.iterkeys(), key=lambda x: table[x])
    host1 = sortedTable[len(sortedTable) - 1]
    host2 = sortedTable[len(sortedTable) - 2]
    #print "Hosts: " + host1.lower() + " , " + host2.lower()
    hosts = [host1, host2]
    return hosts

#Determine fashion awards
def fashionPolice(tweet, table):
	matches = re.findall(proper_noun_regex, tweet)
	for match in matches:
		match = match.strip()
		if match.find("Golden") > -1 or match.find("Globes") > -1:
			continue
		if match in table:
			table[match] = table[match] + 1
		else:
			table[match] = 1

#Find best fashionable awards from table
def processFashion(table):
	sortedTable = sorted(table.iterkeys(), key=lambda x: table[x])
	print "\nThe Fashion Police voted for:\n"
	stop_list = [line.strip() for line in open('stoplist.txt')]
	for i in stop_list:
		try:
			sortedTable.remove(i)
		except ValueError:
			pass
	for j in sortedTable:
		if sum(1 for x in j if x.isupper()) < 2:
			sortedTable.remove(j)
	for i in range(1,11):
		print sortedTable[len(sortedTable)-i]

#Red carpet tweet parsing
def run_redCarpet(tweet, red_carpet_table, keyword):
	normal_tweet = tweet['text'].lower()
	if normal_tweet.find(keyword) > -1:
		fashionPolice(tweet['text'], red_carpet_table)
    
#Process Cecil award winners
def processSpecial(winners,table):
    sortedTable = sorted(table.iterkeys(), key=lambda x: table[x])
    special = sortedTable[len(sortedTable) - 1]
    winners["Cecil B. Demille Award"] = special
    
#Extract joke from tweet with lol or haha
def extractFunny(tweet, table, joke):
    matches = re.findall(proper_noun_regex, tweet)
    for match in matches:
        match = match.strip()
        if match.find("Golden") > -1 or match.find("Globes") > -1:
            continue
        
        if match in table:
            if joke in table[match]:
                table[match][joke] += 1
            else:
                table[match][joke] = 1
        else:
            table[match] = {}
            table[match][joke] = 1
        
#Get the best jokes over a certain threshold
def extractTopJokes(table):
    threshold = 3
    jokeFile = open('jokeout.txt','w')
    for match in table.iterkeys():
        if table[match].keys > 1:
            for joke in table[match].iterkeys():
                if table[match][joke] > threshold:
                    jokeFile.write(str(match) + " " + str(joke) + "\n\n")
                    
    
   
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
