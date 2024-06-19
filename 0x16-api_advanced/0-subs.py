#!/usr/bin/python3
"""
This module defines a function that interacts with the Reddit API to get the
number of subscribers for a specified subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given
    subreddit using the Reddit API.
    Returns 0 if the subreddit is invalid.
    """

    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0   
