import time
import os
import sys
import json
import MissionSelect

x = .5
files = ['email.txt']
addedFiles = []

with open("Directories.json", "r") as read_file:
    data = json.load(read_file)
with open("Commands.json", "r") as read_file:
    commands = json.load(read_file)

sourceProgram = 'HydraHack'
AdminPassword = 'Admin'

def tutorial():
    print('Your first task is a test. Using your skills you must hack website that contains important data.\nThe website you are hacking is',
          'www.testhack.com.\n')
    print('You must then take the data and log into Johns account and get his email.\n')

    print("To start of you must hack the website using the command 'ftpsploit [port] [url]'\n")

    print("To start the mission you must install the nmap tool with the version of 1.00.'\n")

    print("To Install a program you type 'sudo apt-get install [program] [version]' '\n")

    CommandIn = input(f'Root@{sourceProgram}~$ ')
    if CommandIn == "sudo apt-get install nmap 1.00":
        pass

    # print('Well done you completed the tutorial.')
    # MissionSelect.missions()

if __name__ == "__main__":
    tutorial()
