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

    Args:
    subreddit (str): The subreddit to retrieve subscriber count for.

    Returns:
    int: Number of subscribers, or 0 if the subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else
        return 0
