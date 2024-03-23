import requests
from bs4 import BeautifulSoup
from constants import URL_PATH
import pandas as pd

def get_url_content(url : str):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    content_divs = soup.find_all('article', class_='doc')
    contents = ""
    for div in content_divs:
        
        # remove <nav>
        nav_tag = div.find('nav', class_='pagination')
        if nav_tag:
            nav_tag.decompose()
        
        content = div.get_text(strip=True, separator = "\n")
        contents = contents + content
    
    return contents

def main():
    # load urls content
    urls = URL_PATH
    contents = []
    from_url = []

    for url in urls:
        text = get_url_content(url)
        from_url.append(url)
        print(text)
        contents.append(text)
        print("\n\n\n")
        
    result = pd.DataFrame()
    result["url"] = from_url
    result["content"] = contents
    result.to_csv("Starknet_docs.csv",index = False, encoding = "utf-8")
    

if __name__ == "__main__":
    main()