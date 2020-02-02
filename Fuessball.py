from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.kicker.de/serie-a-tim/spieltag').text

soup = BeautifulSoup(source, 'lxml')

list = []

for game in soup.find_all('div', class_= 'kick__v100-gameList__gameRow'):

    team_1 = game.find('div', class_ = 'kick__v100-gameCell__team__name').text

    try:
        result = game.find('div', class_ = 'kick__v100-scoreBoard__scoreHolder').text
    except:
        result = game.find('div', class_ = 'kick__v100-scoreBoard__dateHolder').text

    team_2 = game.find_all('div', class_ = 'kick__v100-gameCell__team__name')[1].text

    status = game.find('div', class_ = 'kick__v100-gameList__gameRow__stateCell').text


    if not "'" in status.replace('\n', ''):
        status = ''
    else:
        status = f"...LIVE...{status}"


    raw= f"{team_1} {result} {team_2} {status}"

    true = raw.replace("\n", " ")

    list.append(true)



with open(r'C:\Users\DioG\Desktop\Serie A.txt', 'w') as file:
    file.write('Resultati Serie A')
    file.write('\n')
    file.write('\n')
    for stat in list:
        file.write(stat)
        file.write('\n')
        file.write('\n')