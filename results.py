import urllib
import json
import collections
import sys
import testing
import helpers

def process(hosts, winners, nominee_table, nominee_list, presenter_list):
    results = {
        "metadata": {
            "year": 2013,
            "hosts": {
                "method": "",
                "method_description": ""
                },
            "nominees": {
                "method": "",
                "method_description": ""
                },
            "awards": {
                "method": "",
                "method_description": ""
                },
            "presenters": {
                "method": "",
                "method_description": ""
                }
            },
        "data": {
            "unstructured": {
                "hosts": hosts,
                "winners": [],
                "awards": [],
                "presenters": presenter_list,
                "nominees": nominee_list
            },
            "structured": {
            }
        }
    }

    winnerList = []
    awardsList = []

    for key in winners:
        award = {}
        award["winner"] = winners[key]
        award["nominees"] = nominee_table[key]
        results["data"]["structured"][key] = award
        winnerList.append(winners[key])
        awardsList.append(key)

    results["data"]["unstructured"]["winners"] = winnerList
    results["data"]["unstructured"]["awards"] = awardsList

    out_file = open('results.json', 'w')
    json.dump(results, out_file)
    out_file.close()