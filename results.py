import urllib
import json
import collections
import sys
import testing
import helpers

def process(winners):
    results = {
        "metadata": {
            "year": 2015,
            "hosts": {
                "method": "Hardcoded",
                "method_description": ""
                },
            "nominees": {
                "method": "Scraped",
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
                "hosts": [],
                "winners": [],
                "awards": [],
                "presenters": [],
                "nominees": []
            },
            "structured": {
            }
        }
    }

    for key in winners:
        award = {}
        award["winner"] = winners[key]


    out_file = open('results.json', 'w')
    json.dump(results, out_file)
    out_file.close()