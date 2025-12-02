#!/usr/bin/python3
"""
Module that sends a request to a URL and prints the response body.
If an HTTPError occurs, it prints: Error code: <status_code>.
"""

import sys
from urllib import request, error


def fetch_url():
    """
    Sends a request to the URL given as argument and prints the body decoded.
    Handles HTTPError and prints its status code.
    """
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            print(body)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    fetch_url()
