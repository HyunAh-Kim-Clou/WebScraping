from indeed import get_indeed_jobs
from save_csv import save_to_file

jobs = get_indeed_jobs()
attr = ["title", "company", "location", "link"]
save_to_file("jobs.csv", attr, jobs)
