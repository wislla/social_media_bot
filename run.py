# run.py

import fetch_data
import generate_report
import send_email

if __name__ == '__main__':
    fetch_data.fetch_tweets('Python')
    generate_report.generate_report()
    send_email.send_email()
