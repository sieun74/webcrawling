import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote_plus
from print_html import print_html

keyword = '환경'
encoded_keyword = quote_plus(keyword)
url = f'https://search.naver.com/search.naver?where=news&query={encoded_keyword}'
print("검색 URL:", url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# HTML 파일로 저장 (디버깅용)
with open("page.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())


# 뉴스 제목 크롤링
news_list = soup.select("a.Q4Y2t_v6TP0bwxdR9avD.CL8ortS8q0ByUMOIzqrc")

for i, item in enumerate(3):
    title = item.get_text(strip=True)
    link = item['href']
    print(f"{i+1}번 뉴스 제목: {title}")
    print(f"링크: {link}")
    print("-" * 30)
