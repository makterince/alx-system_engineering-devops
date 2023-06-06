#!/usr/bin/python3
import requests

def recurse(subreddit):
    """
    Recursively queries the Reddit API and returns a list containing the title
    Args:
        subreddit (str): The name of the subreddit.
        
    Returns:
        list: A list containing the titles of all hot articles,
        or None if the subreddit is invalid or no results are found.
    """
    
    hot_list = []
    headers = {"User-Agent": "My Reddit API Client"}
    after = None

    def _recurse_helper(subreddit, hot_list, after):
    """
    Helper function for recursive API queries.
    
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store the titles of hot articles.
        after (str): The pagination token.
        
    Returns:
        list: A list containing the titles of all hot articles,
        or None if no results are found.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                hot_list.append(post["data"]["title"])
            after = data["data"]["after"]
            if after:
                return _recurse_helper(subreddit, hot_list, after)
            else:
                return hot_list
        elif response.status_code == 404:
            return None
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None
return _recurse_helper(subreddit, hot_list, after)
