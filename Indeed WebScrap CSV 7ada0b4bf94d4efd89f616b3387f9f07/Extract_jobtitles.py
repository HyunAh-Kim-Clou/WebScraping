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
  spans = spans[-1]
  return spans

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    # # 각 페이지 코드 가져오기
    # result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
    # print(result.status_code)

    result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results= soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for result in results:
      job = result.find("h2", {"class":"title"}).find("a")["title"]
      jobs.append(job)
    return jobs


if __name__=="__main__":
    # from indeed import extract_indeed_pages, extract_indeed_jobs
    max_indeed_pages = extract_indeed_pages()
    jobs = extract_indeed_jobs(max_indeed_pages)
    print(jobs)