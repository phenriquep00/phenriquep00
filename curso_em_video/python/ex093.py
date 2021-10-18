dict1 = {'player_name': str(input('Player name: ')),
         'games': int(input('Games played: ')),
         'goals': list()}
for c in range(0, (dict1['games'])):
    dict1['goals'].append(int(input(f'Number of goals on game {c+1}: ')))
dict1['total_goals'] = sum(dict1['goals'])
dict1['yield'] = dict1['total_goals'] / len(dict1['goals'])
print("¬=" * 18)
print(f'{dict1["player_name"]} ==> {dict1["games"]} games played. \n'
      f'{dict1["total_goals"]} goals marked \n'
      f'Yield: {dict1["yield"]}  goals per game')
