# 하단의 페이지링크 가져오기
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50&radius=0")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# pagination=페이지 모음
pagination = indeed_soup.find("div", {"class":"pagination"})
pages = pagination.find_all('a')
spans = []
for page in pages:
    spans.append(int(page.string))
    # spans.append(page.find("span").string)
spans = spans[:-1]
print(spans)
