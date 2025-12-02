#!/usr/bin/python3
"""
Module that sends a POST request with an email parameter and prints the body.
"""

import sys
from urllib import request, parse


def send_post():
    """
    Sends a POST request to the given URL with an email field
    and prints the response body decoded in utf-8.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({"email": email}).encode("utf-8")
    req = request.Request(url, data=data, method="POST")

    with request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)


if __name__ == "__main__":
    send_post()
