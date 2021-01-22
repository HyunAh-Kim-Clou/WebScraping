# Incruit WebScrap CSV

## Incruit 에서 일자리목록 추출하기

### Scrapped WebPage

  : [https://job.incruit.com/jobdb_list/searchjob.asp?crr=99&crr=1&rgn2=18&rgn2=14&rgn2=11&occ1=150&articlecount=60&page=1](https://job.incruit.com/jobdb_list/searchjob.asp?crr=99&crr=1&rgn2=18&rgn2=14&rgn2=11&occ1=150&articlecount=60&page=1)

### Page Structure

<p class="sqr_paging">
  <a href="?crr=99&crr=1&rgn2=18&rgn2=14&rgn2=11&occ1=150&articlecount=60&page=2">
  <span>2

회사명/ 채용제목/ 지원자격/ 근무조건 (Qualification/Terms)
<div class="n_job_list_default">
<div class="n_job_list_table_a">
  <tr>
    <th><div class="companys"><a title="회사명">회사명
    <td><div class="subjects"><a href="세부페이지" title="채용제목"><span>채용제목
    <td><div class="subjects"><em>지원자격 (경력/학력)
    <td><div class="subjects"><em>근무조건 (위치/근무기간)

### Source Code

[main.py](Incruit%20WebScrap%20CSV%20f8b74c34fb9a41f49cedff6f31d458e2/main.py)

[incruit.py](Incruit%20WebScrap%20CSV%20f8b74c34fb9a41f49cedff6f31d458e2/incruit.py)

### Result

![Incruit%20WebScrap%20CSV%20f8b74c34fb9a41f49cedff6f31d458e2/__2021-01-21_182034.png](Incruit%20WebScrap%20CSV%20f8b74c34fb9a41f49cedff6f31d458e2/__2021-01-21_182034.png)