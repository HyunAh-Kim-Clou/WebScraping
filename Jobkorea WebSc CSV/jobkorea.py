import requests
from bs4 import BeautifulSoup

LIMIT = 60
URL = f"http://www.jobkorea.co.kr/recruit/joblist?menucode=duty"
DOMAIN = "http://www.jobkorea.co.kr/"

def get_lastpage_no():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"id":"dvGIPaging"})
  links = pagination.find_all("a")
  spans = []
  for link in links[:-1]:
    spans.append(int(link.string))
  max_page = spans[-1]
  return max_page

def extract_job(html):
  company = html.find("td", {"class":"tplCo"})
  if company is not None:
    company = str(company.find("a").string)
  else:
    company = str(company)
  company = company.strip()
  
  second_row = html.find("td", {"class":"tplTit"})
  t_anchor = second_row.find("a", {"class":"link"})
  title = t_anchor["title"]
  link = t_anchor["href"]

  etc = second_row.find("p", {"class":"etc"})
  etc = etc.find_all("span")
  career = etc[0].string + etc[1].string
  location = etc[2].string + etc[3].string

  return {
    'title':title,
    'company':company,
    'career':career,
    'location':location,
    'link':f"{DOMAIN}{link}"
  }

def extract_jobkorea_jobs(no):
  jobs = []
  for page in range(no):
    # scrap 확인
    print(f"Scrapping page {page+1}")

    result = requests.get(f"{URL}#anchorGICnt_{page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    soup = soup.find("div", {"id":"dev-gi-list"})
    results= soup.find_all("tr")
    for result in results[1:]:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_jobkorea_jobs():
  no = get_lastpage_no()
  jobs = extract_jobkorea_jobs(no)
  return jobs
