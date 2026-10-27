#!/usr/bin/python3
"""Top ten hot posts for a subreddit"""

import requests
from sys import argv


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent":
        "python:subreddit.subscriber.counter:v1.3 (by /u/Background_Lemon_726)"
        }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print(None)
    else:
        data = res.json().get("data", {}).get("children", [])
        for post in data[:10]:
            print(post["data"]["title"])
if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: ./script.py <subreddit>")