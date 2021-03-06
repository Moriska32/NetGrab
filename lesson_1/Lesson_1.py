import json
from pprint import pprint
import requests
from getpass import getpass

#ЗАДАНИЕ 1
print("***************\nЗадание 1\n********************\n")
url = "https://api.github.com/user/repos"

login = input("Логин: ",)
password = input("Пароль: ",)

req = requests.get(url, auth=(login, password))

repos = req.json()
for repo in repos:
	if not repo['private']:
		print(repo['html_url'])

#Задание 2
print("***************\nЗадание 2\n********************\n")
track = input("Введите название аудиотрека: ",)
url = "http://ws.audioscrobbler.com/2.0/"
param = {"method":"track.search",
		"track":track,
		"api_key":"69205b6c9d1c3066da0c099ef95d0403",
		"format":"json"}

req = requests.get(url, params = param)

for line in req.json()['results']['trackmatches']['track']:
	print(line['artist']," - ",line['name'])
file = open("response.json","w", encoding = "utf-8")
file.write(str(req.json()))