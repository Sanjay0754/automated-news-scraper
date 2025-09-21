# news_scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import schedule
import time
import os

def scrape_news():
    url = "https://www.bbc.com/news"   # Stable site for headlines
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines (BBC uses <h2>)
    headlines = [h.text.strip() for h in soup.find_all("h2") if h.text.strip()]

    # Put into dataframe
    df = pd.DataFrame({"Headline": headlines, "Scraped At": datetime.now()})

    # Append to CSV (create if doesn't exist)
    file_exists = os.path.isfile("headlines.csv")
    df.to_csv("headlines.csv", mode="a", header=not file_exists, index=False)

    print(f"[{datetime.now()}] Scraped {len(headlines)} headlines")

# Run once immediately
scrape_news()

# Schedule to run every day at 10:00 AM
schedule.every().day.at("10:00").do(scrape_news)

print("Scheduler started... (Press CTRL+C to stop)")
while True:
    schedule.run_pending()
    time.sleep(1)
