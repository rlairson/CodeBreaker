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
