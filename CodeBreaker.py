#Imports
from random import randint
from local_resources import gameclasses
#from local_resources.colorama_master import colorama
#from colorama import FORE
import os


#List of Variables for the code
attempt = 1
code = []

#Create the code
for i in range(0, 4):
    code.append(randint(0, 9))

#Creating a fucnction to check
def trial():
    trial = [int(x) for x in input().split()]
    mychecker = gameclasses.check()
    check = mychecker.check(trial, code)
    if check == 'You Got the Code!!!':
        print(check)
        print(trial[0:4])
        return True
    else:
        print(trial[0:4], check)
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
os.system('clear')

print("""
_________  ________  ________  __________________________________________   _____   ____  __._____________________
\_   ___ \ \_____  \ \______ \ \_   _____/\______   \______   \_   _____/  /  _  \ |    |/ _|\_   _____/\______   \
/    \  \/  /   |   \ |    |  \ |    __)_  |    |  _/|       _/|    __)_  /  /_\  \|      <   |    __)_  |       _/
\     \____/    |    \|    `   \|        \ |    |   \|    |   \|        \/    |    \    |  \  |        \ |    |   \
 \______  /\_______  /_______  /_______  / |______  /|____|_  /_______  /\____|__  /____|__ \/_______  / |____|_  /
        \/         \/        \/        \/         \/        \/        \/         \/        \/        \/         \/ """)
#Checking the code
while attempt != 21:
    if trial() == True:
        break
    else:
        attempt += 1

"""
    if attempt == 1:

    elif attempt == 2:

    elif attempt == 3:
        trial_3 = [int(x) for x in input().split()]
        mychecker = gameclasses.check()
        check = mychecker.check(trial_3, code)
        attempt += 1
        if check == 'You Got the Code!!!':
            print(check)
            print(trial_3[0:4])
            break
        else:
            print(trial_3[0:4], check)
    elif attempt == 4:
        trial_4 = [int(x) for x in input().split()]
        mychecker = gameclasses.check
        check = mychecker.check(trial_4, code)
        attempt += 1
        if check == 'You Got the Code!!!':
            print(check)
            print(trial_4[0:4])
            break
        else:
            print(trial_4[0:4], check)
    elif attempt == 5:
        trial_5 = [int(x) for x in input().split()]
        mychecker = gameclasses.check
        check = mychecker.check(trial_5, code)
        attempt += 1
        if check == 'You Got the Code!!!':
            print(check)
            print(trial_5[0:4])
            break
        else:
            print(trial_5[0:4], check)
    elif attempt == 6:
        trial_6 = [int(x) for x in input().split()]
        mychecker = gameclasses.check
        check = mychecker.check(trial_6, code)
        attempt += 1
        if check == 'You Got the Code!!!':
            print(check)
            print(trial_6[0:4])
            break
        else:
            print(trial_6[0:4], check)
    elif attempt == 7:
        trial_7 = [int(x) for x in input().split()]
        mychecker = gameclasses.check
        check = mychecker.check(trial_7, code)
        attempt += 1
        if check == 'You Got the Code!!!':
            print(check)
            print(trial_7[0:4])
            break
        else:
            print(trial_7[0:4], check)
    elif attempt == 8:
        trial_8 = [int(x) for x in input().split()]
        mychecker = gameclasses.check
        check = mychecker.check(trial_8, code)
        attempt += 1
        if check == 'You Got the Code!!!':
            print(check)
            print(trial_8[0:4])
            break
        else:
            print(trial_8[0:4], check)
    elif attempt == 9:
        trial_9 = [int(x) for x in input().split()]
        mychecker = gameclasses.check
        check = mychecker.check(trial_9, code)
        attempt += 1
        if check == 'You Got the Code!!!':
            print(check)
            print(trial_9[0:4])
            break
        else:
            print(trial_9[0:4], check)"""
            #print(code)
