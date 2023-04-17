import csv 
with open('students_data.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        print(f"{data['first_name']} --- {data['last_name']} --- {data['fee']} --- {data['date_of_birth']} --- {data['joined_on']} --- {data['matriculation']}")
