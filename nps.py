import urllib.request
import json
from config import api_key 

# Configure API request
endpoint = "https://developer.nps.gov/api/v1/parks?limit=1"
HEADERS = {"X-Api-Key":f"{api_key}"}
req = urllib.request.Request(endpoint, headers=HEADERS)

# Execute request and parse response
response = urllib.request.urlopen(req).read()
data = json.loads(response.decode('utf-8'))

# Prepare and execute output
for park in data["data"]:
    print(park["fullName"])

# # # Configure API request park-names-by-state.py

# state = "me"
# endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=" + state
# HEADERS = {"Authorization":f"{api_key}"}
# req = urllib.request.Request(endpoint,headers=HEADERS)

# # Execute request and parse response
# response = urllib.request.urlopen(req).read()
# data = json.loads(response.decode('utf-8'))

# # Prepare list of parks
# numParks = data["total"]
# print("There are " + str(numParks) + " in " + state.upper() + ".")
# for park in data["data"]:
#     print(park["fullName"])


# https://developer.nps.gov/api/v1/parks?limit=600&api_key=IeNCbfYIqnMxGbTQN2UiPI6gxBSWPXfIcqyYGnde