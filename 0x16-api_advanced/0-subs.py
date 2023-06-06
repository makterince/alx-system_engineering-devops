#!/usr/bin/python3
""" rerturns number of subscribers """

def number_of_subscribers(subreddit):
    """ checks and returns total number of subscribers """


    headers = { 'User-Agent': 'testing' }
    response = requests.get{f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers}

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data[ 'data']['subscribers']
            return subscribers
        except KeyError:
            return 0
    else:
        return 0
