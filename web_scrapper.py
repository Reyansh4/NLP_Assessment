import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_url(url):
    data = {'url': url, 'heading': None, 'date': None, 'editor': None, 'news_text': None}

    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, 'html.parser')

    heading = soup.h1.string
    data['heading'] = heading

    date_element = soup.find(class_="ArticleDetail_ArticleDetail__date__hDHi9")
    if date_element:
        date = date_element.get_text()
        data['date'] = date

    editor_elements = soup.find_all(class_="ArticleDetail_ArticleDetail__name__3AcuN")
    if len(editor_elements) > 1:
        editor = editor_elements[1].get_text()
        data['editor'] = editor

    news_content = soup.find_all('p')
    news_text = ' '.join(paragraph.get_text(strip=True) for paragraph in news_content)
    data['news_text'] = news_text

    return data

with open("urls.txt", "r") as file:
    urls = file.readlines()

urls = [url.strip() for url in urls]

all_data = []

for url in urls:
    data = scrape_url(url)
    all_data.append(data)

df = pd.DataFrame(all_data)

directory = 'data'
if not os.path.exists(directory):
    os.makedirs(directory)

df.to_csv(os.path.join(directory, 'data.csv'), index=False, encoding='utf-8')