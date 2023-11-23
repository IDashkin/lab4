from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import string

#About author info
def aboutAuthor():
    tkinter.messagebox.showinfo('About author', 'My name is Dashkin Ilya and my name is M Avdiyev.\nI\'m a student of KSTU.\nThis program was created specifically for the course project.')
#About version info
def version():
    tkinter.messagebox.showinfo('Version', 'Program version: 1.0.0')
#Open file
def browseFile():
    global filename
    filename = filedialog.askopenfilename()
    infoBar['text'] = filename
#Execute calculation
def executeFile():
    try:
        file = open(filename, "r")                                                #Open file
        d = dict()                                                                #Empty dictionary
        for line in file:                                                         #loop through each line
            line = line.strip()                                                   #Remove spaces
            line = line.lower()                                                   #Convert all characters to lowercase to avoid mistakes
            line = line.translate(line.maketrans("", "", string.punctuation))     #Remove punctuations
            words = line.split(" ")                                               #Split the line into words
            words.sort()                                                          #Sort words by alphabet
            for word in words:                                                    #Iterate over each word in line
                if word in d:                                                     #Check if the word is already in dictionary
                   d[word] = d[word] + 1                                          #Increment count of word by 1
                else:
                    d[word] = 1                                                   #Add the word to dictionary with count 1
        for key in list(d.keys()):                                                #Print the content of dictionary
            print(key, ":", d[key])
    except:
        infoBar['text'] = 'Please select the .txt file (File>Open file...)'       #Message error if the file didn't select or wrong

root = Tk()
#Title name
root.title('Text analyzer')
root.geometry('400x200')
#Main menu bar
menu = Menu(root)
root.config(menu=menu)
#Fill menu button
fileMenu = Menu(menu)
menu.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open file...', command=browseFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)
#About menu button
aboutMenu = Menu(menu)
menu.add_cascade(label='About', menu=aboutMenu)
aboutMenu.add_command(label='Author', command=aboutAuthor)
aboutMenu.add_command(label='Version', command=version)
#Execute button
executeButton = Button(root, text="Execute", command=executeFile)
executeButton.pack(side=TOP, padx=3, pady=2)

#Information bar
infoBar = Label(root, text="", bd=1, relief=SUNKEN, anchor=W)
infoBar.pack(side=BOTTOM, fill=X)

root.mainloop()
