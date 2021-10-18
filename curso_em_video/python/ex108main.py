import ex108

number = int(input('Type a number(R$): '))
print(f'The half of {ex108.coin(number)} is {ex108.coin(ex108.half(number))}')
print(f'The double of {ex108.coin(number)} is {ex108.coin(ex108.double(number))}')
print(f'{ex108.coin(number)} + 10% is {ex108.coin(ex108.increase(number, 10))}')
print(f'{ex108.coin(number)} - 13% is {ex108.coin(ex108.decrease(number, 13))}')
