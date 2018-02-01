'''
Author:
    Thomas VanDivier
Description:
    A simple programm used to learn how to use the urllib module

'''
import urllib.request
import json
class connection_test:
    pass

with urllib.request.urlopen('https://maps.googleapis.com/maps/api/distancematrix/json?origins=Seattle&destinations=San+Francisco&source=False') as response:
    data = response.read()

read = data.decode('ascii')
word = ""
data_list = []
for i in read:
    if i == '' or i == "\t" or i == "\n" or i == "\r":
        data_list.append(word)
        word = ""
        continue
    else:
        word += i
for i in data_list:
    if "{" or "}" in i:
        data_list.remove(i)
for i in data_list:
    for j in i:
        i.replace(" ", "")
        i.replace("\n", "")
        i.replace("\t", "")
        i.replace("\r", "")

    print(i)
    input()
