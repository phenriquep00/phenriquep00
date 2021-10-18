# adding data(players, goals, total of goals) to the list ;

data = []
goals = []
player = {}
while True:
    player.clear()
    goals.clear()
    player["name"] = str(input('name: '))
    games = int(input('games played: '))
    for c in range(0, games):
        goals.append(int(input(f'  --> goals on game {c + 1}: ')))
    player["goals"] = goals[:]
    player["total"] = sum(goals)
    ask = str(input('Add more players? [y/n] ')[0].lower())
    data.append(player.copy())
    if 'n' in ask:
        break

# showing players data: id, name, goals, total goals;

print("-" * 30)
print(f'Id ', end='')
for e in player.keys():
    print(f'{e:<15}', end='')
print()
for index, dictionary in enumerate(data):
    print(f'{index:3>}  ', end='')
    for v in dictionary.values():
        print(f'{str(v):<15}', end='')
    print()

# Showing the data of a specific player;

while True:
    search = int(input("Search for what player's data? [999 to none]: "))
    if search == 999:
        break
    if search >= len(data):
        print('Invalid input!')
        search = int(input("Search for what player's data? [999 to none]: "))
    for i, g in enumerate(data[search]["goals"]):
        print(f' In game {i + 1} {data[search]["name"]} made {g} goals')
    print("-" * 40)
print('end!')
