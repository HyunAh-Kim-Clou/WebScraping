# Ex. csv form
# name, last name, age, gender
# hana, kim, 100, female
# hana, kim, 100, female

# excel > import file > upload 
# import location: replace spreadsheet
# separator type: comma

import csv

def save_to_file(filename, attrname, datas):
  file = open(filename, mode="w")
  writer = csv.writer(file)
  
  writer.writerow(attrname)
  for data in datas:
    # job.values 타입: dict_value
    writer.writerow(list(data.values()))
  return