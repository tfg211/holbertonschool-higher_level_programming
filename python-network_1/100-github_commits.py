#!/usr/bin/python3
"""
Lists the 10 most recent commits of a repository
"""
import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = requests.get(url)
    commits = r.json()
    try:
        for commit in commits[:10]:
            print("{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")))
    except IndexError:
        pass
