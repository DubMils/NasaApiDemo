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
    # Step 1: Make the params dictionary.
    #         This API needs three things:
    #           "api_key"     your key
    #           "start_date"  the date
    #           "end_date"    the same date again (we only want one day)

    # Step 2: Send the request to NEO_URL with your params.

    # Step 3: If the status code is not 200, print the error and return None.

    # Step 4: Turn the response into a dictionary called data.

    # Step 5: The asteroids are inside the data like this:
    #           data["near_earth_objects"][date]
    #         Return that list.

    return None
