import urllib
import json
import collections
import sys
import testing
import helpers
import results
filename = sys.argv[1]
year = sys.argv[2]
file = open("out.txt", "w")

tweets = []
with open(filename) as f:
    for line in f:
        tweets.append(json.loads(line))

frequency_map = {}

awards_list = [line.strip() for line in open('AwardsList.txt')]
stop_list = [line.strip() for line in open('stoplist.txt')]

if year == "2013":
    presenter_list = helpers.parsePresenterList('PresenterList2013Structured.txt')
    nominee_table = helpers.parseNomineeTable('NomineeList2013Structured.txt')
else:
    year = "2015"
    presenter_list = helpers.parsePresenterList('PresenterList2015Structured.txt')
    nominee_table = helpers.parseNomineeTable('NomineeList2015Structured.txt')
    
nominee_list = helpers.parseNominees(nominee_table)
award_table = {}
host_table = {}

for index, text in enumerate(tweets[0]):
    file.write ("Current Tweet %s: %s" % (index, text))
    testing.run_tests(frequency_map, awards_list, stop_list, text, host_table, nominee_list, award_table)

hosts = testing.processHosts(host_table)
winners = testing.processNominees(award_table,nominee_table)

#freq_list = sorted(frequency_map, key=frequency_map.get, reverse=True)
#
#freqFile = open("freqencymap.txt","w")
#
#for i in freq_list[:100]:
#    freqFile.write( "%s frequency: %s occurences\n" % (i, str(frequency_map[i])))

print("Done!")
file.close()
results.process(year, hosts, winners, nominee_table, nominee_list, presenter_list)
#freqFile.close()


        

    