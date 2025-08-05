
import requests
from bs4 import BeautifulSoup


URL = "https://www.bbc.com/news/"

# HTTP request to the website
response = requests.get(URL)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <h2> and <title> tags
    h2_tags = soup.find_all('h2')
    title_tags = soup.find_all('title')

    # Extract text from tags
    headlines = [tag.get_text(strip=True) for tag in h2_tags + title_tags]

    # Remove duplicates and filter short items
    unique_headlines = list(set([headline for headline in headlines if len(headline) > 5]))

    # Write to a text file
    with open('headlines.txt', 'w', encoding='utf-8') as file:
        for line in unique_headlines:
            file.write(line + '\n')

    print("Headlines saved to 'headlines.txt'")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
