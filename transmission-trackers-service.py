import json, os, re, subprocess
from shutil import copyfile
from argparse import ArgumentParser
from distutils.spawn import find_executable
from urllib import request

# check if transmission is installed

if find_executable("transmission-gtk") is None:
    print("Transmission is not installed")
    exit(1)
    
argparser = ArgumentParser(description='Transmission tracker updater')
argparser.add_argument('-c', '--config', help='Path to transmission config file')
argparser.add_argument('-d', '--dry-run', help='Do not write to config file', action='store_true')
argparser.add_argument('-f', '--file', help='Path to file with trackers')
argparser.add_argument('--trackers', help='List of trackers to use', nargs='+')
args = argparser.parse_args()

if args.config:
    config_path = args.config
else:
    home_directory = os.path.expanduser( '~' )
    config_path = os.path.join(home_directory, '.config', 'transmission', 'settings.json')

trackers_list = []
default_tracker = "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt"

if args.file:
    try:
        with open(args.file, 'r') as file:
            for line in file:
                trackers_list.append(line.strip())
    except:
        print("File could not be opened, skipped")
if args.trackers:
    trackers_list = args.trackers

if not trackers_list:
    trackers_list.append(default_tracker)

text = ""

for tracker in trackers_list:
    response = request.urlopen(tracker)
    data = response.read()
    raw_text = data.decode('utf-8')
    for line in raw_text.splitlines():
        if not line or line.startswith('#') or line.startswith('ws'):
            continue
        text += line + "\n"
text = text[:-1]

if args.dry_run:
    print(text)
    exit(0)

# check if config file exists
if not os.path.isfile(config_path):
    print("Config file does not exist")
    exit(1)

# backup config file
backup_path = config_path + ".bak"
try:
    copyfile(config_path, backup_path)
except:
    print("Could not backup config file")
    exit(1)

# modify config file
try:
    with open(config_path, 'r') as file:
        data = json.load(file)
        data['default-trackers'] = text
except:
    print("Could not load config file")
    exit(1)
    
try:
    with open(config_path, 'w') as file:
        json.dump(data, file, indent=4)
except:
    print("Could not write to config file")
    exit(1)

