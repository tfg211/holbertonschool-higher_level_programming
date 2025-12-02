#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the
GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(url, auth=(user, password))
    print(r.json().get("id"))
