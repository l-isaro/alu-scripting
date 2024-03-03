#!/usr/bin/python3
"""
1-main
"""
import requests

def number_of_subscribers(subreddit):
    """Query the Reddit API and return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0 (by YourUsername)"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        else:
            print(f"Error: Status code {response.status_code}")
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
