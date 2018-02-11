import json
from pprint import pprint


# with open("company1.json") as file_json:
#     d = json.load(file_json)
#     pprint(d)


with open("company1.json", 'r+') as file_json:
    d = json.loads(file_json.read())
    d['employees'].append(dict(firstName="Albert",lastName="Bert"))    
    pprint(d)
    file_json.seek(0)
    json.dump(d, file_json, indent=4, sort_keys=True)    
    file_json.truncate()
