import Tutorial
import MissionSelect

def HydraOsLogin():
    operatingSystem = 'HydraOS'
    defaultPassword = 'HYDRA'
    idNumber = '1'
    userPasswordVerification = input(f"{operatingSystem}: Please Enter Your Password: ")
    if userPasswordVerification == defaultPassword:
        GameTutorial()
    else:
        passwordFinder = input('Do you want to know your password? Y/N: ')
        if passwordFinder == 'Y':
            idInput = input('Please state you id number: ')
            if idInput == idNumber:
                print(f'Your password is: {defaultPassword}\n')
                HydraOsLogin()
        else:
            print('FINE! You Can Just Try And Guess the Password!')
            HydraOsLogin()

def GameTutorial():
    CommandEnter = input('Do You Want To Do The Tutorial (Y/N): ')
    if CommandEnter == 'y':
        print('\n')
        Tutorial.tutorial()
    if CommandEnter == 'n':
        MissionSelect.missions()

if __name__ == "__name__":
    HydraOsLogin()
