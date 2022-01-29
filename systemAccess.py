class SystemAccess:

    def __init__(self, maxLoginAttempts=3):

        self.Database = {}
        self.loginAttempts = 0
        self.maxLogins = maxLoginAttempts
        self.maxLogError = "You have too many attempted logins!"
        self.errorMessage = "Invalid Username/Password"
        self.userMessage = "User created Successfully"
        self.userFail = "That UserName already exist!"

    def accessGranted(self):

        return "You've Gained Access"

    def maxLoginError(self, gui):

        try:
            if self.loginAttempts >= 3:
                raise Exception
        except:

            print(self.maxLogError)
            gui.access = self.maxLogError

    def createNewUser(self, gui, log):
        log.createLogin(gui)

        doesExist = (log.CreateUserName in self.Database)
        print(doesExist)
        try:
            if log.CreateUserName != "" and log.CreatePassword != "":
                if doesExist == False:
                    self.Database[log.CreateUserName] = log.CreatePassword
                    gui.access = self.userMessage
                else:
                    raise Exception
        except:
            gui.access = self.userFail

    def authentification(self, gui, log):
        log.getLogin(gui)

        while self.loginAttempts <= 3:
            if self.loginAttempts >= 3:
                gui.access = self.maxLogError
                exit()
            try:
                if log.UserName != "" and log.Password != "":
                    if self.Database == {}:
                        self.loginAttempts += 1
                        self.maxLoginError()
                        gui.access = self.errorMessage
                        break
                    elif self.Database[log.UserName] == "":
                        self.loginAttempts += 1
                        self.maxLoginError()
                        gui.access = self.errorMessage
                        break
                    elif self.Database[log.UserName] == log.Password:
                        gui.access = self.accessGranted()
                        break
                    else:
                        print("hello")
                        self.loginAttempts += 1
                        self.maxLoginError()
                        gui.access = self.errorMessage
                        break

                else:
                    self.loginAttempts += 1
                    self.maxLoginError()
                    print(self.errorMessage)
                    break

            except:
                print(self.errorMessage)
