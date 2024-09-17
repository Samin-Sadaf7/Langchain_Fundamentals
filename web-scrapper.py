import requests
from bs4 import BeautifulSoup

page_to_scrape = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(page_to_scrape, "html.parser")
quotes = soup.findall("span", attrs={'class':'text'})
autohors = soup.findall("span", attrs={'class':'author'})

for quote in quotes:
    print(quote.text)
for author in autohors:
    print(author.text)