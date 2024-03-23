import requests
from bs4 import BeautifulSoup
from langchain_community.document_loaders import TextLoader
from constants import URL_PATH

def crawl_website(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the main content container
        content_container = soup.find('div', class_='markdown-section')

        if content_container:
            # Extract the text content from the container
            content = content_container.get_text()

            # Print the extracted content
            print(content)
        else:
            print("Content container not found.")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

loader = TextLoader("./information.txt")
loader.load()
