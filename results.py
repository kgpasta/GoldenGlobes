import urllib
import json
import collections
import sys
import testing
import helpers

def process(year, hosts, winners, nominee_table, nominee_list, presenter_list):
    results = {
        "metadata": {
            "year": year,
            "hosts": {
                "method": "detected",
                "method_description": "Regular expressions searching for hosts name's within tweets."
                },
            "nominees": {
                "method": "hardcoded",
                "method_description": ""
                },
            "awards": {
                "method": "hardcoded",
                "method_description": ""
                },
            "presenters": {
                "method": "hardcoded",
                "method_description": ""
                }
            },
        "data": {
            "unstructured": {
                "hosts": hosts,
                "winners": [],
                "awards": [],
                "presenters":[],
                "nominees": nominee_list
            },
            "structured": {
            }
        }
    }

    winnerList = []
    awardsList = []
    presenterList = []

    for key in winners:
        award = {}
        award["winner"] = winners[key]
        award["nominees"] = nominee_table[key]
        results["data"]["structured"][key] = award
        winnerList.append(winners[key])
        awardsList.append(key)
    for key in presenter_list:
        for value in presenter_list[key]:
            presenterList.append(value)


    results["data"]["unstructured"]["winners"] = winnerList
    results["data"]["unstructured"]["awards"] = awardsList
    results["data"]["unstructured"]["presenters"] = presenterList

    out_file = open('results' + year + '.json', 'w')
    json.dump(results, out_file)
    out_file.close()