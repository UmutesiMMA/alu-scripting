#!/usr/bin/python3
"""Number of subscribers"""

import json
import requests
import sys


def top_ten(subreddit):
    if len(sys.argv) < 2:
        print(None)
    url = 'https://www.reddit.com/dev/api/r/{}/hot.json'.format(
        subreddit
    )
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print(None)
    else:
        data = json.loads(res.text)["data"]["children"]
        for post in data[:10]:
            print(post["data"]["title"])
