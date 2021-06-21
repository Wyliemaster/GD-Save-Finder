import requests
import itertools
import os
import json


def xor_cipher(string: str, key: int) -> str:
    result = ""
    for char in string:
        result += chr(ord(char) ^ key)
    return result


print("Reading Config")
with open('config.ini', 'r') as config:
    config_data = config.read().split()
    server = config_data[0].split('=')[1]
    userName = config_data[1].split('=')[1]
    password = config_data[2].split('=')[1]

print("Data collected", "requesting save data")

data = {
    "userName": userName,
    "password": password,
    "secret": "Wmfv3899gc9",
    "gameVersion": 21,
    "binaryVersion": 35,
    "gdw": 0
}

req = requests.post(
    "{}/database/accounts/syncGJAccountNew.php".format(server), data=data)

print("Responsed Received")

if req.text == '-11':
    print("Login Credentials Incorrect - Error Code {}".format(req.text))
    exit()

elif req.text == '-6':
    print("The server currently has too much traffic to process the request. Please try again later - Error Code: {}".format(req.text))
    exit()

elif len(req.text) < 10:
    print("Unknown Error - Error Code: {}".format(req.text))
    exit()

response_data = req.text.split(';')


CCGameManager, CCLocalLevels, game_version, binary_version, a1, a2 = response_data

print("Writing Saves")

with open('CCGameManager.dat', 'w') as file:
    file.write(xor_cipher(CCGameManager, 0xB))

with open('CCLocalLevels.dat', 'w') as file:
    file.write(xor_cipher(CCLocalLevels, 0xB))

print("saves can be found in {}".format(os.getcwd()),
      "Preparing a JSON with response Data")

SaveObj = {
    "UserName": userName,
    "GameVersion": game_version,
    "BinaryVersion": binary_version,
    "CCGameManager.dat": CCGameManager,
    "CCLocalLevels.dat": CCLocalLevels,
    "UnknownData": a1,
    "UnknownData2": a2
}

Save_JSON = json.dumps(SaveObj, indent=4)

with open('save_data.json', 'w') as save:
    save.write(Save_JSON)
