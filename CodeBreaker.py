#Imports
from random import randint
from local_resources import gameclasses
#from local_resources.colorama_master import colorama
#from colorama import Fore
import os
import platform
import time


#List of Variables for the code
attempt = 1
codeNew = []
codeHack = []
codeCry = []
cryptTries = []
hackerTries = []
newbieTries = []
level = 1
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
    trial = [int(x) for x in input('>>>').split()]
    mychecker = gameclasses.check()
    check = mychecker.check(trial, codeNew)
    if check == 'You Got the Code!!!':
        print(check)
        print(trial[0:4])
        return True
    else:
        newbieTries.append(trial[0:4])
        print(trial[0:4], check)
        return False
def trialHacker():
    trial = [int(x) for x in input('>>>').split()]
    mychecker = gameclasses.check()
    check = mychecker.check(trial, codeHack)
    if check == 'You Got the Code!!!':
        print(check)
        print(trial[0:4])
        return True
    else:
        print(trial[0:4], check)
        return False
def trialCrypt():
    trial = [int(x) for x in input('>>>').split()]
    mychecker = gameclasses.check()
    check = mychecker.checkhard(trial, codeCry)
    if check == 'You Got the Code!!!':
        print(check)
        print(trial[0:5])
        return True
    else:
        print(trial[0:5], check)
        return False
#Game starts
print("""
 __      __       .__
/  \    /  \ ____ |  |   ____  ____   _____   ____
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
       \/       \/          \/            \/     \/
                ___________
                \__    ___/___
                  |    | /  _ \
                  |    |(  <_> )
                  |____| \____/
""")
time.sleep(5)
if platform.system == 'Windows':
    os.system('cls')
else:
    os.system('clear')
print("""
_________  ________  ________  __________________________________________   _____   ____  __._____________________
\_   ___ \ \_____  \ \______ \ \_   _____/\______   \______   \_   _____/  /  _  \ |    |/ _|\_   _____/\______   \
/    \  \/  /   |   \ |    |  \ |    __)_  |    |  _/|       _/|    __)_  /  /_\  \|      <   |    __)_  |       _/
\     \____/    |    \|    `   \|        \ |    |   \|    |   \|        \/    |    \    |  \  |        \ |    |   \
 \______  /\_______  /_______  /_______  / |______  /|____|_  /_______  /\____|__  /____|__ \/_______  / |____|_  /
        \/         \/        \/        \/         \/        \/        \/         \/        \/        \/         \/ """)
time.sleep(5)
if platform.system == 'Windows':
    os.system('cls')
else:
    os.system('clear')
print('What gmae mode would you like to play? Story or single code.')
print('Game mode needs to be 1 for Story and 2 for Single Code.')
gameMode = input('>>>')
if gameMode == '1':
    storymode = gameclasses.storyMode()
    print('Do you have a password? Enter NO if you do not.  They are case sensitive.')
    password = input('>>>')
    if password == 'NO':
        level = 1
        storymode.LevelOne(1,0)
        if level == 2:
            storymode.LevelTwo(2,0)
            
elif gameMode == '2':
    # Checking the code
    print('Enter a Difficulty. Newbie, Hacker, and Crypt')
    print('Difficulties need to be 1 for Newbie, 2 for Hacker, and 3 for Crypt.')
    diff = input('>>>')
    if diff == '1':
        codeNewbie()
        while attempt != 11:
            if trialNewbie() == True:
                break
            else:
                attempt += 1
        print('the Code was:')
        print(codeNew)
    elif diff == '2':
        codeHacker()
        while attempt != 11:
            if trialHacker() == True:
                break
            else:
                attempt += 1
        print('the Code was:')
        print(codeHack)
    elif diff == '3':
        codeCrypt()
        while attempt != 11:
            if trialCrypt() == True:
                break
            else:
                attempt += 1
        print('the Code was:')
        print(codeCry)
    elif diff == '4':
        codeNew = [1, 2, 3, 4]
        while True:
            if trialNewbie():
                print('Test Complete')
                break
            else:
                print('Test is still active')
                pass
    else:
        print('Your Difficulty is not an option.  Please choice a new difficulty')
