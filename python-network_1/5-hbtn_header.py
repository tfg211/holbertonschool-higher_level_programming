#!/usr/bin/python3
"""
Module that sends a request to a URL and prints the X-Request-Id header value.
"""

import sys
import requests


def print_request_id():
    """
    Sends a request to the given URL and prints the X-Request-Id header.
    """
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))


if __name__ == "__main__":
    print_request_id()
