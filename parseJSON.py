import urllib
import json
import collections
import sys

filename = sys.argv[1]
file = open("out.txt", "w")

tweets = []
with open(filename) as f:
    for line in f:
        tweets.append(json.loads(line))

frequency_map = {}
for index, text in enumerate(tweets[0]):
	file.write ("Current Tweet %s: %s" % (index, text))
	word_array = text['text'].split(" ")
	for word in word_array:
		if frequency_map.has_key(word):
			frequency_map[word] += 1
		else:
			frequency_map[word] = 1

freq_list = sorted(frequency_map, key=frequency_map.get, reverse=True)

for i in freq_list[:100]:
	file.write( "%s frequency: %s occurences" % (i, str(frequency_map[i])))

print("Done!")
file.close()



