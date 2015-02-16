import urllib
import json
import collections
import sys
import testing
import helpers

filename = sys.argv[1]
file = open("out.txt", "w")

tweets = []
with open(filename) as f:
    for line in f:
        tweets.append(json.loads(line))

frequency_map = {}

awards_list = [line.strip() for line in open('AwardsList.txt')]
stop_list = [line.strip() for line in open('stoplist.txt')]
nominee_list = helpers.parseNominees('NomineeList2013Unstructured.txt')
#presenter_list = helpers.parsePresenters('PresenterList2013.txt')
nominee_table = helpers.parseNomineeTable('NomineeList2013Structured.txt')
award_table = {}
host_table = {}

for index, text in enumerate(tweets[0]):
    file.write ("Current Tweet %s: %s" % (index, text))
    
    testing.run_tests(frequency_map, awards_list, stop_list, text, host_table, nominee_list, award_table)

testing.processHosts(host_table)
testing.processNominees(award_table,nominee_table)

#freq_list = sorted(frequency_map, key=frequency_map.get, reverse=True)
#
#freqFile = open("freqencymap.txt","w")
#
#for i in freq_list[:100]:
#    freqFile.write( "%s frequency: %s occurences\n" % (i, str(frequency_map[i])))

print("Done!")
file.close()
#freqFile.close()


        

    