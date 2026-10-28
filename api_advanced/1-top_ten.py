#!/usr/bin/python3
"""Top ten hot posts for a subreddit"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 10}
    res = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if res.status_code != 200:
        print(None)
    else:
        data = res.json().get("data", {}).get("children", [])
        for post in data[:10]:
            print(post["data"]["title"])