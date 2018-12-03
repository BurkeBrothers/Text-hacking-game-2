import Login

operatingSystem = 'HydraOS'
defaultPassword = 'HYDRA'
idNumber = '1'

def Menu():

    print("--- Login ---")
    print("--- Quit ---")

    choice = input(">> ")
    if choice == "login":
        Login.HydraOsLogin()
    if choice == "quit":
        quit()

if __name__ == "__name__":
    Menu()
