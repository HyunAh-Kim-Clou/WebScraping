# Jobkorea WebSc CSV

## Jobkorea 에서 일자리목록 추출하기

### Scrapped WebPage

  : [http://www.jobkorea.co.kr/recruit/joblist?menucode=duty](http://www.jobkorea.co.kr/recruit/joblist?menucode=duty)

### Page Structure

<div id="dvGIPaging"> ## 하단 페이지링크
<ul>
  <li><span class="now" data-page="1">1
  <li><a href="/recruit/_GI_List?Page=2" data-page="2">2
  <li><a href="/recruit/_GI_List?Page=3" data-page="3">3

<div class="detailArea"> ## 세부 분류선택 (??안함)
<dd class="resultList">
  <li class="local item" data-value="K000" data-group="localK000" data-type="">
  <li class="career item" data-value="1" data-group="career1" data-type="">

<div id="dev-gi-list">
<table>
  <td class="tplCo"><a>회사명
  <td class="tplTit"><strong><a href="세부페이지" title="채용제목">채용제목
                                <p class="etc"><span>경력
                                                          <span>학력/위치/기간 등등

### Source Code

[main.py](Jobkorea%20WebSc%20CSV%20f82127de5f5747268c5cf26727fe396f/main.py)

[jobkorea.py](Jobkorea%20WebSc%20CSV%20f82127de5f5747268c5cf26727fe396f/jobkorea.py)

### Result

![Jobkorea%20WebSc%20CSV%20f82127de5f5747268c5cf26727fe396f/__2021-01-22_230314.png](Jobkorea%20WebSc%20CSV%20f82127de5f5747268c5cf26727fe396f/__2021-01-22_230314.png)
