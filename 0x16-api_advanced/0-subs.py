#!/usr/bin/python3
""" rerturns number of subscribers """
import requests
def number_of_subscribers(subreddit):
    """ checks and returns total number of subscribers """


    headers = { 'User-Agent': 'testing' }
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except requests.exceptions.RequestException as e:
        return 0
