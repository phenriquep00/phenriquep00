def card(name='unknown', goals=0):
    print(f'The player {name} scored {goals} goals.')


# main
n = str(input('player name: '))
g = str(input('goals scored: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if len(n) == 0 and g == 0:
    card()
elif len(n) == 0 and g != 0:
    card(name='unknown', goals=g)
else:
    card(n, g)
