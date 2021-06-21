# GD Save Finder

A quick python script to fetch your Geometry Dash save data from a server of your choice.   

Currently, 3 files will be generated after using this script:

- CCGameManager.dat

- CCLocalLevels.dat

- save_data.json

**CCGameManager.dat** and **CCLocalLevels.dat** are your saves and can be placed in `%localappdata%/GeometryDash/`. The **save_data.json** is a seperate file generated which seperates the raw response and assigns each component of the response with a name, the JSON includes some data that is excluded from your CCFiles however, the way to access the content of this other data is currently unknown

## Requirements

- Python >= 3.6

- A Geometry Dash account with a backed up save

## Usage

**config.json** contains essential data in order to successfully use this program.

- **server** -> The target server you want to fetch your save from. By default it is the Geometry Dash Data Server however, it can be used for GDPS's if you type `http://<target server>/database`

- **username** -> this field is for your username on the target server

- **password** -> this field is for your password on the target server

After setting up config.ini, you can either run the python script in the command prompt using `python3 <current directory>/save_finder.py` or by executing the `run.bat` file provided

## Notes

- This tool is for ***Geometry Dash 2.1***

- This tool utilises a few modules from the official Python Package Index. They are required for the tool to run, and are able to obtain them through running the command `python3 -m pip install -r requirements.txt`.
