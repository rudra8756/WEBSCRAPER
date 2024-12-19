import requests
from bs4 import BeautifulSoup
from config import NEWS_URL, HEADERS

def scrape_headlines(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h3', class_='gs-c-promo-heading__title')
        print("Latest News Headlines:")
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline.get_text(strip=True)}")
    except Exception as e:
        print(f"An error occurred: {e}")

scrape_headlines(NEWS_URL)
