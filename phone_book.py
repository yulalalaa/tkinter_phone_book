from tkinter import *
from phones  import * #import excisting contacts

class AddressBook:
    def __init__(self):      
        window = Tk() # Create a window
        window.title("Phone Book") # Set title

        self.nameVar = StringVar()
        self.phoneVar = StringVar()
        self.cityVar = StringVar()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text = "Name").grid(row = 1, 
            column = 1, sticky = W)
        Entry(frame1, textvariable = self.nameVar, 
            width = 40).grid(row = 1, column = 2)

        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text = "Phone").grid(row = 1, 
            column = 1, sticky = W)
        Entry(frame2, textvariable = self.phoneVar, 
            width = 40).grid(row = 1, column = 2)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text = "City", width = 5).grid(row = 1, 
            column = 1, sticky = W)
        Entry(frame3, 
            textvariable = self.cityVar).grid(row = 1, column = 2)

        frame4 = Frame(window)
        frame4.pack()
        btAdd = Button(frame4, text = "Add", 
            command = self.processAdd).grid(row = 1, column = 1)
        btDelete = Button(frame4, text = "Delete", 
            command = self.processDelete).grid(row = 1, column = 2)
        btSeeAll = Button(frame4, text = "See All", 
            command = self.processSeeAll).grid(row = 1, column = 3)

        window.mainloop() # Create an event loop

    def processAdd(self):
        pass

    def processDelete(self):
        pass

    def processSeeAll(self):
        pass

AddressBook()
