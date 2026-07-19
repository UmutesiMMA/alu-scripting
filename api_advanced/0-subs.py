#!/usr/bin/python3
"""Number of subscribers"""

import json
import sys
import requests

if __name__ == '__main__':
    def number_of_subscribers(subreddit):
        if len(sys.argv) < 2:
            return 0
        url = 'https://www.reddit.com/dev/api/r/{}/about'.format(
            subreddit
        )
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code != 200:
            return 'nope'
        body = json.loads(res.text)
        return body['data']['subscribers']

