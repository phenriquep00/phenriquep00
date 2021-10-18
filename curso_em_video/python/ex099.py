def things(lst):
    print(f'The total numbers were {len(lst)}. The bigger number was {max(lst)}')


numbers = []
while True:
    numbers.append(int(input('Insert a number: ')))
    call = str(input("Want to add other number? [y/n]"))[0].lower()
    if 'n' in call:
        break

things(numbers)
