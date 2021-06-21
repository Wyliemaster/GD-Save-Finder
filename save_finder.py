import requests
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
    username = config_data[1].split('=')[1]
    password = config_data[2].split('=')[1]

print("Data collected. Requesting save data")

data = {
    "userName": username,
    "password": password,
    "secret": "Wmfv3899gc9",
    "gameVersion": 21,
    "binaryVersion": 35,
    "gdw": 0
}

req = requests.post(
    f"{server}/database/accounts/syncGJAccountNew.php", data=data
)

print("Responsed Received")

if req.text == '-11':
    print(f"Login Credentials Incorrect - Error Code {req.text}")
    exit()

elif req.text == '-6':
    print(f"The server currently has too much traffic to process the request. Please try again later - Error Code: {req.text}")
    exit()

elif len(req.text) < 10:
    print(f"Unknown Error - Error Code: {req.text}")
    exit()

(
    cc_game_manager,
    cc_local_levels,
    game_version,
    binary_version,
    a1,
    a2
) = req.text.split(';')

print("Writing Saves")

with open('CCGameManager.dat', 'w') as file:
    file.write(xor_cipher(cc_game_manager, 0xB))

with open('CCLocalLevels.dat', 'w') as file:
    file.write(xor_cipher(cc_local_levels, 0xB))

print(f"Saves can be found in {os.getcwd()}",
      "Preparing a JSON with response Data")

save_obj = {
    "UserName": username,
    "GameVersion": game_version,
    "BinaryVersion": binary_version,
    "CCGameManager.dat": cc_game_manager,
    "CCLocalLevels.dat": cc_local_levels,
    "UnknownData": a1,
    "UnknownData2": a2
}

save_json = json.dumps(save_obj, indent=4)

with open('save_data.json', 'w') as save: save.write(save_json)
