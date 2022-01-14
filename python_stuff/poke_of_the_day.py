import requests
from bs4 import BeautifulSoup

url = "https://otpokemon.com/"
html = requests.get(url=url).text
soup = BeautifulSoup(html, 'html.parser')
poke_day = soup.findAll('div', attrs={'class': 'dex tooltip2'})
str_poke = str(poke_day)
poke_of_the_day_name = str_poke[55:-309]

print(poke_of_the_day_name)
