from database import session, Tweet


def analyze_data():
    tweets = session.query(Tweet).all()
    total_tweets = len(tweets)
    return total_tweets


if __name__ == '__main__':
    total_tweets = analyze_data()
    print(f'Total Tweets: {total_tweets}')
