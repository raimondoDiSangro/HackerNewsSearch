import webbrowser

import requests
from bs4 import BeautifulSoup
import re


# Send a GET request to the Hacker News front page
url = "https://news.ycombinator.com/news"
response = requests.get(url)

# Parse the page content
soup = BeautifulSoup(response.text, 'html.parser')

links = []
for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
    href = link.get('href')
    if 'ycombinator' not in href:
        links.append(href)

#change the [:5 to select more or less]
for link in links[:5]:
    print(link)
    #optional open the links
    #webbrowser.open(link)

# Extract the text of each article
for link in links[:5]:  # Adjust the slice to control how many articles you want to extract
    print(f"Fetching article from: {link}")

    # Send a GET request to the article page
    article_response = requests.get(link)

    # Parse the article page content
    article_soup = BeautifulSoup(article_response.text, 'html.parser')

    # Extract the main article text
    # This depends on the structure of the page, but commonly the article text is found in <p> tags
    paragraphs = article_soup.find_all('p')

    article_text = "\n".join([para.get_text() for para in paragraphs])

    # Print or process the article text
    print("Article Text:\n", article_text)
    print("-" * 80)  # Separator between articles

    # Optional: If you want to save the article text, you can do so here
    #with open('article.txt', 'w') as file:
         #file.write(article_text)