import ex109

number = int(input('Type a number(R$): '))
print(f'The half of {ex109.coin(number)} is {ex109.half(number, co=True)}')
print(f'The double of {ex109.coin(number)} is {ex109.double(number, True)}')
print(f'{ex109.coin(number)} + 10% is {ex109.increase(number, 10, co=True)}')
print(f'{ex109.coin(number)} - 13% is {ex109.decrease(number, 13, co=True)}')
