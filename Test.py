import time
import json
import StoreItems
from StoreItems import *

x = .5

with open("Bank.json", 'r') as f:
    bank = json.load(f)
with open("Commands.json", 'r') as f:
    commands = json.load(f)

print(Store.vpn())
print("--------------------------")
print(Store.HackingPack())

def store():
    while True:
        print("\nWhat do you want to buy?\n")
        time.sleep(x)
        choice = input(">> ")
        if choice == "1":
            if bank["Bank"]["Money"] >= vpnPrice:
                commands["Test"]["InstalledCommands"]["Command1"] = "vpn"
            with open("Commands.json", 'w') as f:
                    commands = json.dump(commands, f)

            if bank["Bank"]["Money"] < vpnPrice:
                print("You cant buy this tool")

        if choice == "2":
            if bank["Bank"]["Money"] >= HackingPackPrice:
                commands["Test"]["Commands"]["InstalledCommands"]["Command2"] = "HackingPack"
                with open("Commands.json", 'w') as f:
                        commands = json.dump(commands, f)
            if bank["Bank"]["Money"] < HackingPackPrice:
                print("You cant buy this tool")
