from jobkorea import get_jobkorea_jobs
from save_csv import save_to_file

jobs = get_jobkorea_jobs()

attr = ["title", "company", "career", "location", "link"]
save_to_file("jobkorea_jobs.csv", attr, jobs)
