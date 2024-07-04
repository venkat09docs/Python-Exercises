import csv

"""
with open('empdata.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    print(type(reader))
    for row in reader:
        # print(row)
        print(f'{row[1]} is located in {row[3]}')
"""

"""
with open('empdata.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print(type(reader))
    for row in reader:
        # print(row)
        print(f"{row['EmpName']} is located in {row['EmpAddress']}")
"""