import requests
from bs4 import BeautifulSoup

# Fetch the page content
page_to_scrape = requests.get('https://quotes.toscrape.com/')
# Parse the content with BeautifulSoup
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Find all the quotes and authors
quotes = soup.find_all("span", attrs={'class': 'text'})
authors = soup.find_all("span", attrs={'class': 'author'})

# Print each quote
for quote in quotes:
    print(quote.text)

# Print each author
for author in authors:
    print(author.text)
