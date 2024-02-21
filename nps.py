import urllib.request
import json
from config import api_key 
from park_dict import park_dict
# Configure API request
# endpoint = "https://developer.nps.gov/api/v1/parks?limit=600"
# HEADERS = {"X-Api-Key":f"{api_key}"}
# req = urllib.request.Request(endpoint, headers=HEADERS)

# # Execute request and parse response
# response = urllib.request.urlopen(req).read()
# data = json.loads(response.decode('utf-8'))

# # Prepare and execute output
# for park in data["data"]:
    
#     park_dict[park['fullName']]=park['parkCode']
#     print(park_dict)

# # Configure API request park-names-by-state.py

# state = input("Enter the State abbreviation: ")
# endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=" + state
# HEADERS = {"X-Api-Key":f"{api_key}"}
# req = urllib.request.Request(endpoint,headers=HEADERS)

# # Execute request and parse response
# response = urllib.request.urlopen(req).read()
# data = json.loads(response.decode('utf-8'))

# # Prepare list of parks
# numParks = data["total"]
# print("There are " + str(numParks) + " in " + state.upper() + ".")
# for park in data["data"]:
#     # print(park)
#     print(f"Park Name: {park['fullName']}",f"Park Code: {park['parkCode']}")



# state = input("Enter the State abbreviation: ")
# endpoint = "https://developer.nps.gov/api/v1/alerts?parkCode=shil"
# HEADERS = {"X-Api-Key":f"{api_key}"}
# req = urllib.request.Request(endpoint,headers=HEADERS)

# Execute request and parse response
# response = urllib.request.urlopen(req).read()
# data = json.loads(response.decode('utf-8'))

# # Prepare list of parks
# # numParks = data["total"]
# # print("There are " + str(numParks) + " in " + state.upper() + ".")
# for alert in data["data"]:
#     print(alert["title"],alert["url"],alert["description"])
#     # print(park)
    


# endpoint = "https://developer.nps.gov/api/v1/passportstamplocations?parkCode=shil"
# HEADERS = {"X-Api-Key":f"{api_key}"}
# req = urllib.request.Request(endpoint,headers=HEADERS)

# # Execute request and parse response
# response = urllib.request.urlopen(req).read()
# data = json.loads(response.decode('utf-8'))

# # Prepare list of parks
# # numParks = data["total"]
# # print("There are " + str(numParks) + " in " + state.upper() + ".")
# for location in data["data"]:
#     print(location["id"], location["label"],location["parks"])

   
#     # print(park)

print(park_dict['Zion National Park'])