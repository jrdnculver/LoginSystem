class Login:

    def __init__(self):

        self.UserName = ""
        self.Password = ""

    def setUserName(self, gui):

        gui.setUserName()
        self.UserName = gui.getUserName()
        return self.UserName

    def setPassword(self, gui):

        gui.setPassword()
        self.Password = gui.getPassword()
        return self.Password

    def getUserName(self):

        return self.UserName

    def getPassword(self):

        return self.Password

    def setCreateUserName(self, gui):

        gui.setCreateUserName()
        self.CreateUserName = gui.getCreateUserName()
        return self.CreateUserName

    def setCreatePassword(self, gui):

        gui.setCreatePassword()
        self.CreatePassword = gui.getCreatePassword()
        return self.CreatePassword

    def getCreateUserName(self):

        return self.CreateUserName

    def getCreatePassword(self):

        return self.CreatePassword

    def getLogin(self, gui):

        self.setUserName(gui)
        self.setPassword(gui)

    def createLogin(self, gui):
        self.setCreateUserName(gui)
        self.setCreatePassword(gui)
