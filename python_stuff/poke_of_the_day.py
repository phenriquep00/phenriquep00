import requests
from bs4 import BeautifulSoup

url = "https://otpokemon.com/"
html = requests.get(url=url).text
soup = BeautifulSoup(html, 'html.parser')
poke_day = soup.findAll('div', attrs={'class': 'dex tooltip2'})
str_poke = str(poke_day)
lst = []
for _ in str_poke[55:]:
    if _ != '.':
        lst.append(_)
    else:
        break
poke_of_the_day_name = "".join(lst)

print(poke_of_the_day_name)
