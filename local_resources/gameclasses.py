import random
#from colorama_master.colorama import Fore, init
class check:
    def __init__(self):
        pass

    def check(self,checkThis,againstThis,):
        checkThis = checkThis[0:4]
        correctplace = 0
        incode = 0
        for n in range(0,4):
            if checkThis[n] in againstThis:
                if checkThis[n] == againstThis[n]:
                    correctplace += 1
                else:
                    incode += 1
        if correctplace == 4:
            return 'You Got the Code!!! '

        else:
            return [correctplace, incode]
    def checkhard(self,checkThis,againstThis,):
        checkThis = checkThis[0:5]
        correctplace = 0
        incode = 0
        for n in range(0,5):
            if checkThis[n] in againstThis:
                if checkThis[n] == againstThis[n]:
                    correctplace += 1
                else:
                    incode += 1
        if correctplace == 4:
            return 'You Got the Code!!! '

        else:
            return [Fore.Red + str(correctplace), Fore.White + str(incode)]


    def storyCheck(self,checkThis, AgainstThis, Level):
        if Level in range(0, 5):
            checkThis = checkThis[0]
            againstThis = AgainstThis[0]
            correctplace = 0
            incode = 0
            if checkThis in againstThis:
                if checkThis[0] == againstThis[0]:
                    correctplace += 1
                else:
                    incode += 1
            else:
                pass
            if correctplace == 1:
                return 'You got the code!'
            else:
                return checkThis,[correctplace, incode]
        elif Level in range(5, 11):
            checkThis = checkThis[0:1]
            againstThis = AgainstThis[0:1]
            correctplace = 0
            incode = 0
            for n in range(0, 1):
                if checkThis[n] in againstThis:
                    if checkThis[n] == againstThis[n]:
                        correctplace += 1
                    else:
                        incode += 1
            if correctplace == 2:
                return 'You got the code!'
            else:
                return [correctplace, incode]
        elif Level in range(11, 16):
            checkThis = checkThis[0:2]
            againstThis = AgainstThis[0:2]
            correctplace = 0
            incode = 0
            for n in range(0, 3):
                if checkThis[n] in againstThis:
                    if checkThis[n] == againstThis[n]:
                        correctplace += 1
                    else:
                        incode += 1
            if correctplace == 3:
                return 'You got the code!'
            else:
                return [correctplace, incode]
        elif Level in range(16, 21):
            checkThis = checkThis[0:4]
            againstThis = AgainstThis[0:4]
            correctplace = 0
            incode = 0
            for n in range(0, 4):
                if checkThis[n] in againstThis:
                    if checkThis[n] == againstThis[n]:
                        correctplace += 1
                    else:
                        incode += 1
            if correctplace == 4:
                return 'You got the code!'
            else:
                return [correctplace, incode]


class storyMode:
    def __init__(self):
        pass
    def LevelOne(self, level, attempt):
        code = random.randint(0, 4)
        level = level
        trial = [int(x) for x in input('>>>').split()]
        print(trial)
        while attempt != 11:
           mychecker = check.storyCheck(self, trial, code, level)
           if mychecker == 'You got the code!':
               print(mychecker)
               print(trial)
               level += 1
           else:
               print(trial, mychecker)
               attempt += 1
    def LevelTwo(self, level, attempt):
        code = random.randint(0,4)
        trial = [int(x) for x in input('>>>').split]
        while attempt != 6:
            mychecker = check.storyCheck(trial, code, level)
            if mychecker == 'You got the code!':
                print(mychecker)
                print(trial)
                level += 1
            else:
                print(trial, mychecker)
                attempt += 1
    def LevelThree(self, level, attempt):
        code = random.randint(0,9)
        trial = [int(x) for x in input('>>>').split]
        while attempt != 11:
            mychecker = check.storyCheck(trial, code, level)
            if mychecker == 'You got the code!':
                print(mychecker)
                print(trial)
                level += 1
            else:
                print(trial, mychecker)
                attempt += 1
    def LevelFour(self, level, attempt):
        code = random.randint(0,9)
        trial = [int(x) for x in input('>>>').split]
        while attempt != 11:
            mychecker = check.storyCheck(trial, code, level)
            if mychecker == 'You got the code!':
                print(mychecker)
                print(trial)
                level += 1
            else:
                print(trial, mychecker)
                attempt += 1
