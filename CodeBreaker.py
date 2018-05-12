#Imports
from random import randint
from local_resources import gameclasses
from local_resources.colorama_master.colorama import Fore, Style, init
import os
import platform
import time

init()
#List of Variables for the code
attempt = 1
codeNew = []
codeHack = []
codeCry = []
cryptTries = []
hackerTries = []
newbieTries = []
#Create the code
def codeNewbie():
    for i in range(0,4):
        codeNew.append(randint(0, 4))
def codeHacker():
    for i in range(0, 4):
        codeHack.append(randint(0, 9))
def codeCrypt():
    for i in range(0, 5):
        codeCry.append(randint(0, 20))
#Trial functions
def trialNewbie():
    print('Please enter a 4 digit code and put spaces between the digits like "1 2 3 4".')
    trial = [int(x) for x in input(Fore.BLUE + '>>>').split()]
    mychecker = gameclasses.check()
    check = mychecker.check(trial, codeNew)
    if check == 'You Got the Code!!!':
        print(Fore. GREEN + check)
        print(trial[0:4])
        return True
    else:
        print(trial[0:4], check)
        return False
def trialHacker():
    print('Please enter a 4 digit code and put spaces between the digits like "1 2 3 4".')
    trial = [int(x) for x in input(Fore.BLUE + '>>>').split()]
    mychecker = gameclasses.check()
    check = mychecker.check(trial, codeHack)
    if check == 'You Got the Code!!!':
        print(Fore.RESET + Fore. GREEN + str(check))
        print(trial[0:4])
        return True
    else:
        print(trial[0:4], Fore.RED + str(check))
        return False
def trialCrypt():
    print('Please enter a 4 digit code and put spaces between the digits like "1 2 3 4".')
    trial = [int(x) for x in input(Fore.BLUE + '>>>').split()]
    mychecker = gameclasses.check()
    check = mychecker.checkhard(trial, codeCry)
    if check == 'You Got the Code!!!':
        print(Fore.RESET + Fore. GREEN + str(check))
        print(trial[0:5])
        return True
    else:
        print(trial[0:5], Fore.RED + str(check))
        return False
def trialAdmin():
    trial = [int(x) for x in input(Fore.BLUE + '>>>').split()]
    mychecker = gameclasses.check()
    check = mychecker.check(trial, codeNew)
    if check == 'You Got the Code!!!':
        print(Fore.RESET + Fore. GREEN + str(check))
        print(trial[0:4])
        return True

    else:
        print(trial[0:4], Fore.RED + str(check))
        return False
#Game starts
if platform.system == 'Windows':
    os.system('cls')
else:
    os.system('clear')
print(Fore.CYAN + """
 __      __       .__
/  \    /  \ ____ |  |   ____  ____   _____   ____
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \\
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
       \/       \/          \/            \/     \/
                ___________
                \__    ___/___
                  |    | /  _ \\
                  |    |(  <_> )
                  |____| \____/
""")
time.sleep(3)
if platform.system == 'Windows':
    os.system('cls')
else:
    os.system('clear')
print(Fore.RED + """
_________  ________  ________  __________________________________________   _____   ____  __._____________________
\_   ___ \ \_____  \ \______ \ \_   _____/\______   \______   \_   _____/  /  _  \ |    |/ _|\_   _____/\______   \\
/    \  \/  /   |   \ |    |  \ |    __)_  |    |  _/|       _/|    __)_  /  /_\  \|      <   |    __)_  |       _/
\     \____/    |    \|    `   \|        \ |    |   \|    |   \|        \/    |    \    |  \  |        \ |    |   \\
 \______  /\_______  /_______  /_______  / |______  /|____|_  /_______  /\____|__  /____|__ \/_______  / |____|_  /
        \/         \/        \/        \/         \/        \/        \/         \/        \/        \/         \/ """ + Style.RESET_ALL)
time.sleep(3)
if platform.system == 'Windows':
    os.system('cls')
else:
    os.system('clear')

#Checking the code
print('Enter a Difficulty. Newbie, Hacker, and Crypt')
print('Difficulties need to be 1 for Newbie, 2 for Hacker, and 3 for Crypt.')
diff = input(Fore.BLUE + '>>>')
if diff in '1':
    codeNewbie()
    print('The first set of numbers is your try.  The second set is how many digits are in the correct place and the next is how many are in the code.')
    while attempt != 11:
        if trialNewbie() == True:
            break
        else:
            attempt += 1
    print('the Code was:')
    print(codeNew)
elif diff in '2':
    codeHacker()
    print('The first set of numbers is your try.  The second set is how many digits are in the correct place and the next is how many are in the code.')
    while attempt != 11:
        if trialHacker() == True:
            break
        else:
            attempt += 1
    print('the Code was:')
    print(codeHack)
elif diff in '3':
    codeCrypt()
    print('The first set of numbers is your try.  The second set is how many digits are in the correct place and the next is how many are in the code.')
    while attempt != 16:
        if trialCrypt() == True:
            break
        else:
            attempt += 1
    print('the Code was:')
    print(codeCry)
elif diff in '4':
    print(Fore. MAGENTA + 'Welcome Admin')
    codeNew = [1, 2, 3, 4]
    while True:
        if trialAdmin():
            print('Test Complete')
            break
        else:
            print('Test is still active')

else:
    print('Your Difficulty is not an option.  Please choice a new difficulty')
