# generate_report.py

from analyze_data.py import analyze_data
from datetime import datetime


def generate_report():
    total_tweets = analyze_data()
    report = f"Report for {datetime.utcnow().date()}\nTotal Tweets: {total_tweets}\n"
    with open('report.txt', 'w') as f:
        f.write(report)
        

if __name__ == '__main__':
    generate_report()
