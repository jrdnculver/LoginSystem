import tkinter as tk


class Gui():

    def __init__(self, userName="", password="", access="NO ACCESS"):
        self.UserName = userName
        self.Password = password
        self.access = access
        self.root = tk.Tk()

    # Will set UserName for Login
    def setUserName(self):

        self.UserName = self.entryUserName.get()

    # WIll set Password for Login
    def setPassword(self):

        self.Password = self.entryPassword.get()

    # Will getUserName for Login
    def getUserName(self):

        return self.UserName

    # Will get Password for Login
    def getPassword(self):

        return self.Password

    # WIll set UserDefined UserName for sign up
    def setCreateUserName(self):
        self.CreateUserName = self.suEntryUserName.get()

    # WIll set UserDefined Password for sign up
    def setCreatePassword(self):
        self.CreatePassword = self.suEntryPassword.get()

    # WIll get UserDefined Login for sign up
    def getCreateUserName(self):
        return self.CreateUserName

    # Will get UserDefined Login for sign up
    def getCreatePassword(self):
        return self.CreatePassword

    # Root window properties
    def rootProperties(self):

        self.root.configure(background="Blue")
        self.root.geometry("500x500")
        self.root.title("LoginSystem")
        self.root.resizable(width=0, height=0)

    # Will create and post labels to root window
    def rootLabels(self):

        self.labelHeader = tk.Label(
            self.root, background="black", foreground="blue", text="PLEASE LOGIN", font=("Times New Roman", 20))
        self.labelHeader.place(relx=.5, rely=.1, anchor="center")

        self.labelUserName = tk.Label(
            self.root, background="black", foreground="blue", text="UserName: ", font=("Courier New", 14))
        self.labelUserName.place(relx=.2, rely=.3, anchor="center")

        self.labelUserName = tk.Label(
            self.root, background="black", foreground="blue", text="Password: ", font=("Courier New", 14))
        self.labelUserName.place(relx=.2, rely=.4, anchor="center")

        self.labelAccess = tk.Label(
            self.root, background="black", foreground="blue", text=self.access, font=("Courier New", 14))
        self.labelAccess.place(relx=.5, rely=.9, anchor="center", width=450)

    # Will create and post entries to root window
    def rootEntries(self):

        self.entryUserName = tk.Entry(
            self.root, background="black", foreground="blue")
        self.entryUserName.place(
            relx=.4, rely=.3, anchor="w", width=190, height=28)

        self.entryPassword = tk.Entry(
            self.root, background="black", foreground="blue")
        self.entryPassword.place(
            relx=.4, rely=.4, anchor="w", width=190, height=28)

    # Will create and post buttons to root window
    def rootButtons(self, gui, log, pro, sys):

        self.buttonLogin = tk.Button(
            self.root, background="black", foreground="blue", text="Login", command=lambda: [sys.authentification(gui, log), pro.tierOne()])
        self.buttonLogin.place(
            relx=.7, rely=.7, anchor="center", width=80, height=45)

        self.buttonLogin = tk.Button(
            self.root, background="black", foreground="blue", text="Sign Up", command=pro.tierTwo)
        self.buttonLogin.place(
            relx=.3, rely=.7, anchor="center", width=80, height=45)

    # Create a frame for sign up window
    def rootSignUpFrame(self):
        self.frameSignUp = tk.Frame(self.root, background="black")
        self.frameSignUp.place(width=500, height=500)

    # Will create and post labels to sign up frame window
    def signUpLabels(self):

        self.suLabelHeader = tk.Label(
            self.frameSignUp, background="black", foreground="blue", text="PLEASE SIGN UP", font=("Times New Roman", 20))
        self.suLabelHeader.place(relx=.5, rely=.1, anchor="center")

        self.suLabelUserName = tk.Label(
            self.frameSignUp, background="black", foreground="blue", text="UserName: ", font=("Courier New", 14))
        self.suLabelUserName.place(relx=.2, rely=.3, anchor="center")

        self.suLabelUserName = tk.Label(
            self.frameSignUp, background="black", foreground="blue", text="Password: ", font=("Courier New", 14))
        self.suLabelUserName.place(relx=.2, rely=.4, anchor="center")

        self.sulabelAccess = tk.Label(
            self.frameSignUp, background="black", foreground="blue", text=self.access, font=("Courier New", 14))
        self.sulabelAccess.place(relx=.5, rely=.9, anchor="center", width=450)

    # Will create and post entries to sign up frame window
    def signUpEntries(self):

        self.suEntryUserName = tk.Entry(
            self.frameSignUp, background="black", foreground="blue")
        self.suEntryUserName.place(
            relx=.4, rely=.3, anchor="w", width=190, height=28)

        self.suEntryPassword = tk.Entry(
            self.frameSignUp, background="black", foreground="blue")
        self.suEntryPassword.place(
            relx=.4, rely=.4, anchor="w", width=190, height=28)

    # Will create and post buttons to sign up frame window
    def signUpButtons(self, gui, log, pro, sys):

        self.suButtonLogin = tk.Button(
            self.frameSignUp, background="black", foreground="blue", text="Create", command=lambda: [sys.createNewUser(gui, log), self.frameSignUp.destroy(), pro.tierTwo()])
        self.suButtonLogin.place(
            relx=.7, rely=.7, anchor="center", width=80, height=45)

        self.suReturnToMenu = tk.Button(
            self.frameSignUp, background="black", foreground="blue", text="Menu", command=lambda: [self.frameSignUp.destroy(), pro.tierOne()])
        self.suReturnToMenu.place(
            relx=.3, rely=.7, anchor="center", width=80, height=45)
