#!/usr/bin/python3
"""
Module that sends a POST request with an email parameter using requests.
"""

import sys
import requests


def send_post():
    """
    Sends a POST request with an email and prints the response body.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    r = requests.post(url, data=data)
    print(r.text)


if __name__ == "__main__":
    send_post()
