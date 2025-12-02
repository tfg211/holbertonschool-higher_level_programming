#!/usr/bin/python3
"""
Module that fetches https://intranet.hbtn.io/status using the requests package.
"""

import requests


def fetch_status():
    """
    Sends a GET request and prints the body information.
    """
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)

    content = r.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))


if __name__ == "__main__":
    fetch_status()
