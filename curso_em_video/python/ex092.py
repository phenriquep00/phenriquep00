import time
# from datetime import datetime
# now = datetime.now().year

dict1 = dict()
now = int(time.strftime('%Y'))
dict1['name'] = str(input('Name: '))
dict1['byear'] = int(input('Birth Year: '))
dict1['age'] = now - dict1['byear']
dict1['ctps'] = int(input('ctps number [0 for none]: '))
if dict1['ctps'] == 0:
    print(f'{dict1["name"]} -- Age: {dict1["age"]} unemployed')
elif dict1['ctps'] != 0:
    dict1['contract_year'] = int(input('Year of contract: '))
    dict1['salary'] = int(input('salary: '))
    dict1['retirement'] = dict1['contract_year'] + 35
    print(f'{dict1["name"]} -- Age: {dict1["age"]} -- Salary: {dict1["salary"]}'
          f' -- Retirement year: {dict1["retirement"]}')
