data = {'name': list(),
        'age': list(),
        'sex': list()}
c = 0
female = []
over_aged = list()
while True:
    data['name'].append(str(input('Name: ')))
    data['age'].append(int(input('Age: ')))
    data['sex'].append(str(input('Sex [M/F]')[0].upper()))
    if data['sex'][c] == 'F':
        female.append(data['name'][c])
    ask = str(input("Want to continue? [y/n] ")[0].upper())
    c += 1
    if 'N' in ask:
        break
average = sum(data['age']) / len(data['age'])
print("=+" * 20)
print(f'{c} people were registered in total.')
print(f'The average age is: {average:.2f} years')
print(f'The females were: {female}')
for i in range(0, len(data["age"])):
    if data["age"][i] > average:
        over_aged.append(data['name'][i])
print(f'{over_aged} were above the age average.')
