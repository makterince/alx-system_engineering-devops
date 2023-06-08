#!/usr/bin/python3
""" rerturns number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ checks and returns total number of subscribers """
    headers = {'User-Agent': 'testing'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data("data")("subscribers")
    else:
        return 0
