#!/usr/bin/python3
"""Number of subscribers"""

import json
import requests
import sys


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent":
        "python:subreddit.subscriber.counter:v1.0 (by /u/Background_Lemon_726)"
        }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print(None)
    else:
        data = json.loads(res.text)["data"]["children"]
        for post in data[:10]:
            print(post["data"]["title"])
