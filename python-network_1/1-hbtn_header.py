#!/usr/bin/python3
"""
Module that sends a request to a URL and prints the X-Request-Id header value.
"""

import sys
from urllib import request


def print_request_id():
    """
    Sends a request to the URL given as argument and prints X-Request-Id.
    """
    url = sys.argv[1]
    req = request.Request(url)

    with request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))


if __name__ == "__main__":
    print_request_id()
