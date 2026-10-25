#!/usr/bin/python3
"""Number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    print(res)
    if res.status_code != 200:
        return 0
    return res.json().get("data", {}).get("subscribers", 0)
