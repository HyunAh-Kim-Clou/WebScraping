import requests
from bs4 import BeautifulSoup

LIMIT = 60
URL = f"https://job.incruit.com/jobdb_list/searchjob.asp?crr=99&crr=1&rgn2=18&rgn2=14&rgn2=11&occ1=150&articlecount={LIMIT}"

def get_lastpage_no():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("p", {"class":"sqr_paging"})
  links = pagination.find_all("a")
  spans = []
  for link in links[:-2]:
    spans.append(int(link.string))
  max_page = spans[-1]
  return max_page

def extract_job(html):
  company = html.find("th").find("span", {"class":"links"})
  if company is not None:
    company = str(company.find("a").string)
  else:
    company = str(company)
  company = company.strip()
  
  rows = html.find_all("td")
  links_anchor = rows[0].find("a", {"class":"links"})
  link = links_anchor["href"]
  title = links_anchor["title"]

  career = str(rows[1].find("em"))
  location = str(rows[2].find("em"))

  return {
    'title':title,
    'company':company,
    'career':career,
    'location':location,
    'link':link
  }

def extract_incruit_jobs(no):
  jobs = []
  for page in range(no):
    print(f"Scrapping page {page+1}")

    result = requests.get(f"{URL}&page={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results= soup.find_all("tr")
    for result in results[1:]:
      job = extract_job(result)
      jobs.append(job)
  return jobs

def get_incruit_jobs():
  no = get_lastpage_no()
  jobs = extract_incruit_jobs(no)
  return jobs
