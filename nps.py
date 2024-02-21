import urllib.request
import json
from config import api_key 
from park_dict import *

def all_national_parks():
    endpoint = "https://developer.nps.gov/api/v1/parks?limit=600"
    HEADERS = {"X-Api-Key":f"{api_key}"}
    req = urllib.request.Request(endpoint, headers=HEADERS)
    # Execute request and parse response
    response = urllib.request.urlopen(req).read()
    data = json.loads(response.decode('utf-8'))
    # Prepare and execute output
    for park in data["data"]:
        park_dict[park['fullName']]=park['parkCode']
        print(park_dict)

def parks_by_state():
    state = input("Enter the State abbreviation: ")
    endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=" + state
    HEADERS = {"X-Api-Key":f"{api_key}"}
    req = urllib.request.Request(endpoint,headers=HEADERS)
    # Execute request and parse response
    response = urllib.request.urlopen(req).read()
    data = json.loads(response.decode('utf-8'))
    # Prepare list of parks
    numParks = data["total"]
    print("There are " + str(numParks) + " in " + state.upper() + ".")
    for park in data["data"]:
        # print(park)
        print(f"Park Name: {park['fullName']}",f"Park Code: {park['parkCode']}")


def alerts_by_state():
    state = input("Enter the State abbreviation: ")
    endpoint = f"https://developer.nps.gov/api/v1/alerts?stateCode={state}"
    HEADERS = {"X-Api-Key":f"{api_key}"}
    req = urllib.request.Request(endpoint,headers=HEADERS)
    # Execute request and parse response
    response = urllib.request.urlopen(req).read()
    data = json.loads(response.decode('utf-8'))
    for alert in data["data"]:
        print(alert["title"],alert["url"],alert["description"], '\n')
        # print(park)
    

def passport_stamp_location():
    park_code = input("Enter Park Code: ")
    endpoint = f"https://developer.nps.gov/api/v1/passportstamplocations?parkCode={park_code}"
    HEADERS = {"X-Api-Key":f"{api_key}"}
    req = urllib.request.Request(endpoint,headers=HEADERS)
    response = urllib.request.urlopen(req).read()
    data = json.loads(response.decode('utf-8'))
    locations = ''
    for location in data["data"]:
        locations+=location['label']
        if len(location)>=1:
            locations += ", "
    print(f"You can get your passport stamped at {locations}inside the {location['parks'][0]['fullName']}.", '\n')

   


# alerts_by_state()
passport_stamp_location()