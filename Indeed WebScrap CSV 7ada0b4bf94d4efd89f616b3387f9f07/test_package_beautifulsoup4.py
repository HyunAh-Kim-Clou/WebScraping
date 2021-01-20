# package bs4 단위test
# BeautifulSoup: html에서 데이터object 추출
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50&radius=0")
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
print(indeed_soup)
