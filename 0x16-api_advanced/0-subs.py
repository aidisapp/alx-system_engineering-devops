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
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.RequestException as e:
        print(f"HTTP request failed: {e}")
        return 0
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return 0
