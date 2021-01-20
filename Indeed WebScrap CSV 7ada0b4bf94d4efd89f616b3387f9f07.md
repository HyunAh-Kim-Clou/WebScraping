# Indeed WebScrap CSV

[Watch Now - 노마드 코더 Nomad Coders](https://nomadcoders.co/python-for-beginners/lobby)

위 강의의 **#2 BUILDING A JOB SCRAPPER** 를 실습해보았다.

++ Web Scraping : Web상의 data를 추출하는 것

++ Response 200 = ok

## Indeed 에서 일자리목록 추출하기

- Target Web page

  : [https://kr.indeed.com/jobs?q=python&limit=50&radius=0](https://kr.indeed.com/jobs?q=python&limit=50&radius=0)

- Work Environment

[The collaborative browser based IDE](https://repl.it/)

└ Packages

[repl.it](http://repl.it/) > packages > requests, beautifulsoup4 추가

└ reference

: [https://requests.readthedocs.io/en/master/](https://requests.readthedocs.io/en/master/)

: [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- Source Code

[main.py](Indeed%20WebScrap%20CSV%207ada0b4bf94d4efd89f616b3387f9f07/main.py)

[indeed.py](Indeed%20WebScrap%20CSV%207ada0b4bf94d4efd89f616b3387f9f07/indeed.py)

[save_csv.py](Indeed%20WebScrap%20CSV%207ada0b4bf94d4efd89f616b3387f9f07/save_csv.py)

- Output

    : [직업, 회사명, 위치, 상세정보URL] CSV 파일

    ![Indeed%20WebScrap%20CSV%207ada0b4bf94d4efd89f616b3387f9f07/jobs_res.png](Indeed%20WebScrap%20CSV%207ada0b4bf94d4efd89f616b3387f9f07/jobs_res.png)

### 단위테스트 목록

[test_package_beautifulsoup4.py](Indeed%20WebScrap%20CSV%207ada0b4bf94d4efd89f616b3387f9f07/test_package_beautifulsoup4.py)

[test_package_requests.py](Indeed%20WebScrap%20CSV%207ada0b4bf94d4efd89f616b3387f9f07/test_package_requests.py)

[Extract_down_pagelinks.py](Indeed%20WebScrap%20CSV%207ada0b4bf94d4efd89f616b3387f9f07/Extract_down_pagelinks.py)

[Extract_jobtitles.py](Indeed%20WebScrap%20CSV%207ada0b4bf94d4efd89f616b3387f9f07/Extract_jobtitles.py)