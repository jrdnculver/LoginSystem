from gui import Gui
from login import Login
from createPassword import CreatePassword
from systemAccess import SystemAccess


class Program:

    def tierOne(self):

        print("I am tier One")
        gui.rootProperties()
        gui.rootLabels()
        gui.rootEntries()
        gui.rootButtons(gui, log, pro, sys)

        gui.root.mainloop()

    def tierTwo(self):

        print("I am tier Two")
        gui.rootSignUpFrame()
        gui.signUpLabels()
        gui.signUpEntries()
        gui.signUpButtons(gui, log, pro, sys)

        gui.root.mainloop()


if __name__ == "__main__":
    gui = Gui()
    log = Login()
    passw = CreatePassword()
    sys = SystemAccess()
    pro = Program()
    pro.tierOne()
