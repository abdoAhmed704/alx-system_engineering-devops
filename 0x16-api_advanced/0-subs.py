#!/usr/bin/python3
""" requests subscribers from reddit api """
import re
import requests


def number_of_subscribers(subreddit):
    """ return the number of subscribers for a given sub reddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about/"
    res = requests.get(url)
    html = res.text
    pattern = r'subscribers="([^"]*)"'
    subscribers = re.search(pattern, html)

    if subscribers:
        return int(subscribers[0][13:-1])
    else:
        return 0
