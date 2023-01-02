
from tkinter import *


class User:

    def __init__(self, countriesList):
        self.countries = countriesList
        self.selected = "x"

    def getSelection(self):
        return self.selected

    def create_UI(self):
        def send_data():
            label.config(text="Sent " + clicked.get())
            self.selected = clicked.get()
            print(self.selected)

        root = Tk()
        root.geometry("300x300")

        clicked = StringVar()

        clicked.set("Click to select Country Options")

        # Create Dropdown menu
        drop = OptionMenu(root, clicked, *self.countries)
        drop.pack()

        # Create button, it will change label text
        button = Button(root, text="Send and exit out of GUI please!", command=send_data).pack()

        # Create Label
        label = Label(root, text=" ")
        label.pack()

        # Execute tkinter
        root.mainloop()
