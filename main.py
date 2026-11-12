# main.py
# This file runs the app. It is already done.
# It uses config.py for the key and api.py to talk to NASA.

from config import API_KEY
from api import get_earth_photos, get_asteroids


def show_earth():
    date = input("Date (YYYY-MM-DD): ")
    photos = get_earth_photos(date)

    if photos is None:
        print("Nothing came back. Is get_earth_photos finished in api.py?")
        return

    if len(photos) == 0:
        print("NASA has no Earth photos for that day. Try a date after June 2015.")
        return

    photo = photos[0]

    # Build the link to the real image from the date and the image name.
    parts = date.split("-")
    link = "https://epic.gsfc.nasa.gov/archive/natural/" + parts[0] + "/" + parts[1] + "/" + parts[2] + "/png/" + photo["image"] + ".png"

    print()
    print("NASA took", len(photos), "photos of Earth on", date)
    print("First one was taken at", photo["date"])
    print("Link:", link)


def show_asteroids():
    date = input("Date (YYYY-MM-DD): ")
    rocks = get_asteroids(date)

    if rocks is None:
        print("Nothing came back. Is get_asteroids finished in api.py?")
        return

    print()
    print(len(rocks), "asteroids passed near Earth on", date)

    for rock in rocks:
        name = rock["name"]
        size = rock["estimated_diameter"]["meters"]["estimated_diameter_max"]
        miss = float(rock["close_approach_data"][0]["miss_distance"]["kilometers"])
        print(name, "| about", round(size), "m wide | missed us by", round(miss), "km")


def main():
    print("=== SPACE EXPLORER ===")

    if API_KEY is None or API_KEY == "paste_your_key_here":
        print("No key found. Check your .env file and finish config.py (Level 1).")
        return

    print("Key loaded! It starts with", API_KEY[:4])

    choice = ""
    while choice != "3":
        print()
        print("1. Earth from space on a date")
        print("2. Asteroids for a date")
        print("3. Quit")
        choice = input("Pick one: ")

        if choice == "1":
            show_earth()
        elif choice == "2":
            show_asteroids()


main()
