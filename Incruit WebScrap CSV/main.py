from incruit import get_incruit_jobs
from save_csv import save_to_file

jobs = get_incruit_jobs()

attr = ["title", "company", "career", "location", "link"]
save_to_file("incruit_jobs.csv", attr, jobs)
