from tkinter import *
import tkinter as tk

phonebook = {'Andrew Parson':8806336, \
'Emily Everett':6784346, 'Peter Power':7658344, \
'Lewis Lame':1122345}

class AddressBook:
    def __init__(self):      
        window = Tk() #create a window
        window.title("Phone Book") #set title

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

        frame4 = Frame(window)
        frame4.pack()
        btAdd = Button(frame4, text = "Add", 
            command = self.processAdd).grid(row = 1, column = 1)
        btDelete = Button(frame4, text = "Delete", 
            command = self.processDelete).grid(row = 1, column = 2)
        btSeeAll = Button(frame4, text = "See All", 
            command = self.processSeeAll).grid(row = 1, column = 3)
        btExit = Button(frame4, text = "Exit", 
            command = self.processExit).grid(row = 1, column = 4)

        window.mainloop() #create an event loop

    def processAdd(self):
    	pass

    def processDelete(self):
        pass

    def processSeeAll(self):
        window = Tk()
        window.title("Contacts")
        window.geometry("300x200") 
        frame5 = Frame(window)       
        frame5.pack()
        listbox = Listbox(window)
        listbox.pack ()
        scrollbar = Scrollbar(window)
        scrollbar.pack(side = RIGHT, fill = BOTH) 
        listbox.config(width=25, xscrollcommand = scrollbar.set) 
        scrollbar.config(command = listbox.yview)
        for key in phonebook:
        	listbox.insert(END, '{}: {}'.format(key, phonebook [key]))
       
    def processExit(self):
    	quit()

AddressBook()

