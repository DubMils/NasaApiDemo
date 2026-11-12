# api.py
# This file has one job: talk to NASA and give back the data.

import requests
from config import API_KEY

EPIC_URL = "https://api.nasa.gov/EPIC/api/natural/date/"
NEO_URL = "https://api.nasa.gov/neo/rest/v1/feed"


# ----- LEVEL 2 -----
# Get the photos of Earth taken from space on a date like "2026-03-09".
def get_earth_photos(date):
    # TODO A: Fill in the params. This is what NASA needs from us.
    params = {
        "api_key": None,   # replace None with the variable that holds your key
    }

    # This API wants the date in the address, so we add it to the URL.
    url = EPIC_URL + date

    # TODO B: Send the request.
    #         Replace None with requests.get(url, params=params)
    response = None

    if response is None:
        return None

    # 200 means it worked. Anything else is an error.
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None

    # TODO C: Turn the answer into Python data with response.json()
    #         (replace the None). Here it gives you a list of photos.
    data = None

    return data


# ----- LEVEL 3 -----
# Get the list of asteroids that passed near Earth on a date.
# Same pattern as get_earth_photos, but this time you write it.
def get_asteroids(date):
  
    return None
