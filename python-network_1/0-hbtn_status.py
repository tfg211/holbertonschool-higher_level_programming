#!/usr/bin/python3
"""
Module that fetches the status page from the Holberton intranet.
It sends a required header so the request is accepted behind the firewall.
"""

from urllib import request


def fetch_status():
    """
    Fetches https://intranet.hbtn.io/status and prints details about the body.
    """
    url = "https://intranet.hbtn.io/status"
    headers = {"cfclearance": "true"}

    req = request.Request(url, headers=headers)

    with request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    fetch_status()
