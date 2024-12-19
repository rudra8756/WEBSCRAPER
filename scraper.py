import requests
from bs4 import BeautifulSoup


def scrape_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h2', class_='headline')
        print("Latest News Headlines:")
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline.get_text(strip=True)}")
    except Exception as e:
        print(f"An error occurred: {e}")
news_url ="https://www.wikipedia.org"
scrape_headlines(news_url)
