from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import BeautifulSoupTransformer
import json
from constant import REMOVE_TXT, START_TXT

def main():
    
    urls = set()
    with open('output.json', 'r') as f:
        all_data = json.load(f)
        for data in all_data:
            urls.add(data["url"])
    
    urls =list(urls)

    loader = AsyncHtmlLoader(urls)
    html = loader.load()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["span","p","li","div"])
    
    with open('../data/content.txt', 'a') as file:

        for info in docs_transformed:
            need_text = info.page_content
            start_index = need_text.find(START_TXT)
            need_text = need_text[start_index + len(START_TXT):]
            for remove in REMOVE_TXT:
                need_text = need_text.replace(remove,"")

            file.write(need_text)
            file.write("\n\n")

if __name__ == "__main__":
    main()