# package requests 단위test
# Response 200 = ok
import requests

indeed_result = requests.get("https://kr.indeed.com/jobs?q=python&limit=50&radius=0")
print(indeed_result)
# print(indeed_result.text)
