import time
import os
import sys
import json
import Test

with open("missionSelect.json", "r") as read_file:
    AvailableMissions = json.load(read_file)
with open("User.json", 'r') as f:
    user = json.load(f)


def menu():
    print("--- Mission Select ---")
    print("--- Shop ---")

    choice = input(">> ")
    if choice == "1":
        missions()
    elif choice == "2":
        Test()

def missions():
    print('\n'.join(AvailableMissions['AllMissions']))
    mission_select = input("Select Mission: ")

if __name__ == "__main__":
    menu()
