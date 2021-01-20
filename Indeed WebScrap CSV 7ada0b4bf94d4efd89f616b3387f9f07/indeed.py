import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=0"

def extract_indeed_pages():
  result = requests.get(INDEED_URL)
  soup = BeautifulSoup(result.text, "html.parser")

  # pagination=하단 페이지 모음
  pagination = soup.find("div", {"class":"pagination"})
  links = pagination.find_all("a")
  spans = [0]
  for link in links[:-1]:
    spans.append(int(link.string))
  max_page = spans[-1]
  return max_page

def extract_job(html):
  title = html.find("h2", {"class":"title"}).find("a")["title"]

  company = html.find("span", {"class": "company"})
  company_anchor = company.find("a")
  if company_anchor is not None:
    company = str(company_anchor.string)
  else: # company_anchor에 없으면
    company = str(company.string)
  # 끝가지의 공백제거
  company = company.strip()

  # 속성값은 []로 가져옴
  location = html.find("span", {"class":"location"}).string

  # 상세페이지를 위한 키값
  job_id = html["data-jk"]

  return {
    'title':title,
    'company':company,
    'location':location,
    'link':f"https://www.indeed.com/viewjob?jk={job_id}"
  }

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    # scrap 확인
    print(f"Scrapping page {page}")

    result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results= soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_indeed_jobs():
  last_pages = extract_indeed_pages()
  jobs = extract_indeed_jobs(last_pages)
  return jobs
