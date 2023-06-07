#!/usr/bin/python3
""" gets the first 10 hot posts listed for a subreddit """

import requests
import sys


def top_ten(subreddit):
    """ gets the 10 hot posts """

    headers = {"User-Agent": "My Reddit API Client"}
    url = "https://www.reddit.com/r/{subreddit}/hot.json".format(subredit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data("data")("children")
            for post in posts[:10]:
                print(post("data")("title"))
        elif response.status_code == 404:
            print("None")
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print("None")
