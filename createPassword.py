import random as rnd


class CreatePassword:

    def __init__(self):

        self.__upperCharacter = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".upper().split(",")
        self.__lowerCharacter = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(
            ",")
        self.__integer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.__symbol = "!, @,#,$,%,^,&,*,_,-,+,=".split(",")
        self.__password = ""
        self.errorMessage = "Invalid Username/Password"

    # Getters and Setters

    def setUpperCharacter(self):

        self.UpperCharacter = self.__upperCharacter

    def setLowerCharacter(self):

        self.LowerCharacter = self.__lowerCharacter

    def setInteger(self):

        self.Integer = self.__integer

    def setSymbol(self):

        self.Symbol = self.__symbol

    def setPassword(self):

        self.Password = self.__password

    def getUpperCharacter(self):

        return self.UpperCharacter

    def getLowerCharacter(self):

        return self.LowerCharacter

    def getInteger(self):

        return self.Integer

    def getSymbol(self):

        return self.Symbol

    def getPassword(self):

        return self.Password

    # Will return an uppercase letter if called.

    def generateUpper(self):

        try:

            randomNumber = rnd.randint(0, len(self.__upperCharacter) - 1)
            self.__password = self.__password + \
                self.__upperCharacter[randomNumber]

        except:

            print(self.errorMessage)

    # Will return a lowercase letter if called.

    def generateLower(self):

        try:

            randomNumber = rnd.randint(0, len(self.__lowerCharacter) - 1)
            self.__password = self.__password + \
                self.__lowerCharacter[randomNumber]

        except:

            print(self.errorMessage)

    # Will return an integer letter if called.

    def generateInteger(self, gui):

        try:

            randomNumber = rnd.randint(0, len(self.__integer) - 1)
            self.__password = self.__password + \
                str(self.__integer[randomNumber])

        except:

            print(self.errorMessage)
            gui.access = self.errorMessage

    # Will return a symbol letter if called.

    def generateSymbol(self, gui):

        try:

            randomNumber = rnd.randint(0, len(self.__symbol) - 1)
            self.__password = self.__password + self.__symbol[randomNumber]

        except:

            print(self.errorMessage)
            gui.access = self.errorMessage

    # Will loop through and call functions to generate password of 10 characters.

    def createPassword(self):

        i = 0
        while i < 10:

            randomNumber = rnd.randint(0, 4)

            if randomNumber == 0:
                self.generateUpper()
            elif randomNumber == 1:
                self.generateLower()
            elif randomNumber == 2:
                self.generateInteger()
            else:
                self.generateSymbol()

            i += 1
        self.setPassword()

    # Will shuffle the final result password to promote more randomness with outcome.

    def shufflePassword(self):

        passwordShuffle = [x for x in self.__password]
        rnd.shuffle(passwordShuffle)
        self.__password = "".join(passwordShuffle)
        self.setPassword()
