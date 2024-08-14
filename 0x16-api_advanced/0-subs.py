#!/usr/bin/python3
"""
Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetch comments from a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Reddit API Tester"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            return 0
    else:
        return 0
