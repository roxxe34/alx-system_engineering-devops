#!/usr/bin/python3
"""function that queries the Reddit API and returns titles of
the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit API and returns data
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    try:
        if response.status_code == 200:
            data = response.json()
            title = data.get('data').get('children')
            for i in range(10):
                print(title[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
