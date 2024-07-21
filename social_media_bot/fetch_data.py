from typing import List, Dict, Any

import tweepy


def fetch_tweets(
    api_key: str,
    api_key_secret: str,
    access_token: str,
    access_token_secret: str,
    query: str,
    count: int = 100
) -> List[Dict[str, Any]]:
    auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=query, count=count)
    return [tweet._json for tweet in tweets]
