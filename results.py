import urllib
import json
import collections
import sys
import testing
import helpers

def process(year, hosts, winners, nominee_table, nominee_list, presenter_list):
    [x.encode('utf-8') for x in winners]
    [x.encode('utf-8') for x in nominee_list]
    [x.encode('utf-8') for x in presenter_list]
    results = {
        "metadata": {
            "year": year,
            "names": {
                "hosts": {
                    "method": "detected",
                    "method_description": "Regular expressions searching for hosts name's (proper nouns) within tweets."
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
            "mappings": {
                "nominees": {
                    "method": "hardcoded",
                    "method_description": ""
                    },
                "presenters": {
                    "method": "hardcoded",
                    "method_description": ""
                    }
                }
            },
        "data": {
            "unstructured": {
                "hosts": hosts,
                "winners": [],
                "awards": [],
                "presenters": [],
                "nominees": []
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
        if key in presenter_list:
            award["presenters"] = presenter_list[key]
        results["data"]["structured"][key] = award
        winnerList.append(winners[key])
        awardsList.append(key)
    for key in presenter_list:
        for value in presenter_list[key]:
            presenterList.append(value)

    results["data"]["unstructured"]["winners"] = winnerList
    results["data"]["unstructured"]["awards"] = awardsList
    results["data"]["unstructured"]["presenters"] = presenterList
    results["data"]["unstructured"]["nominees"] = nominee_list

    out_file = open('results' + year + '.json', 'w')
    json.dump(results, out_file, encoding="utf-8", ensure_ascii=False)
    out_file.close()