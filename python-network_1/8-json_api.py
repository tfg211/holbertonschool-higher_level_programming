#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
"""
import sys
import requests


if __name__ == "__main__":
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]

    payload = {'q': letter}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        response = r.json()
        if response:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
