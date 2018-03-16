#python3
# Currency converter

import requests, json, datetime, pprint

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

# check response time
currency_url = "http://www.apilayer.net/api/live?access_key=YOURKEYHERE&currencies=AUD,EUR,GBP,CAD,RUB,JPY"
response = requests.get(currency_url)
data = response.json()
if response != '<Response [200]>':
    print(response)
else:
    None
# 404 - resource wasn't found on the web
# 200 - everything went okay
# 400 - server thinks you made a bad request
currency = response.json()
print("Information is refreshed every 30 minutes")
print("Conversion is to 1 US Dollar")
print("------------------------------------")
pp_json(data["quotes"])
timestamp = data["timestamp"]
print("Updated as of " +
    datetime.datetime.fromtimestamp(
        int(timestamp)
    ).strftime('%Y-%m-%d %H:%M:%S')
)
