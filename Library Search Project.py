"""
Library Book Search
Group 4
7/15/2023
A user enters the book they want to find 
Then the program finds if the library carries the book 
If the library carries the book, the program also finds the books location
"""
import tkinter
from breezypythongui import EasyFrame
import random
import os
import pandas as pd

# getting the path to the current directory, then setting that as the working directory
os.chdir(os.path.realpath(os.path.dirname(__file__)))

def create_checklist(file_path):
    data = pd.read_csv(file_path)
    checklist = data['Title'].tolist()
    return checklist
class LibrarySearch(EasyFrame):

    def __init__(self):
        """Setting up the main labels and buttons"""
        EasyFrame.__init__(self, title="Library Search", resizable="True")
        self.addLabel(text="Library Book Search", row=0, column=0, sticky="NSEW", columnspan=2)
        imageLabel = self.addLabel(text="", row=0, column=3, sticky="NSEW") # Creates first image
        self.addLabel(text="What book do you want to search for? (Case Sensitive)",
                        row=1, column=0, sticky="NSEW", columnspan=2)
        self.inputField = self.addTextField(text="", row=2, column=0,
                                            sticky="NSEW", columnspan=2) # Creates and replaces text box
        self.addLabel(text="If we carry your book, click the find button to find the book in the library.",
                        row=3, column=0, sticky="NSEW", columnspan=3)
        supplyCheck = self.addTextField(text="", row=4, column=0, 
                                        sticky="NSEW", columnspan=2, state="readonly") # Creates and replaces read only text box
        findBook = self.addButton(text="Find", row=4,
                                    column=3, command=self.bookArea, state="disabled") # Creates button to find where book is if book is in library
        self.addButton(text="Search", row=5,
                                       column=0, command=self.callSearch)
        self.addButton(text="Reset", row=5,
                                       column=1, command=self.searchReset)
        self.addButton(text="Exit", row=5, column=3, 
                       command=lambda: EasyFrame.quit(self))

        # Creates an image
        self.image = tkinter.PhotoImage(file = "open-book-doodle.gif") # Finds first image to display
        imageLabel["image"] = self.image


        file_path = 'books.csv'
        self.checklist = create_checklist(file_path)

    def callSearch(self):
        self.book = self.inputField.getText() # reads what book user entered for input validation
        
        while True:
            if self.book == "":
                bookName = self.prompterBox(title="Error", 
                                            promptString="Error. Please fill out the search field or use this field.") # Error message if user did not enter any information
                self.inputField = self.addTextField(text=bookName, row=2, column=0,
                                                sticky="NSEW", columnspan=2)
            elif self.book == " ":
                bookName = self.prompterBox(title="Error", 
                                            promptString="Error. Please fill out the search field or use this field.") # Error message if user did not enter any information
                self.inputField = self.addTextField(text=bookName, row=2, column=0,
                                                sticky="NSEW", columnspan=2)
            else:
                break
            self.book = self.inputField.getText()

        
        book_search = bookSearch(self.checklist) # Random function for bookSearch
        book = book_search.search(self.book)
        
        if book == 0:
            supplyCheck = self.addTextField(text="Your book is not carried at this library", row=4, column=0, 
                                        sticky="NSEW", columnspan=2, state="readonly")
            findBook = self.addButton(text="Find", row=4,
                                    column=3, command=self.bookArea, state="disabled")
        elif book == 1:
            supplyCheck = self.addTextField(text="Your book is carried at this library", row=4, column=0, 
                                        sticky="NSEW", columnspan=2, state="readonly")
            findBook = self.addButton(text="Find", row=4,
                                    column=3, command=self.bookArea, state="normal")

    def searchReset(self):
        """Erasing all input in text field"""
        self.inputField = self.addTextField(text="", row=2, column=0,
                                            sticky="NSEW", columnspan=2)

    def bookArea(self):
        book_area = bookArea() # Random function for bookArea
        areaSearch = book_area.area(self.book)
        self.messageBox(title="Book Location", message=(areaSearch))

class bookSearch(LibrarySearch):
    """Checking to see if the library carries the book"""
    def __init__(self, checklist):
        self.checklist = checklist

    def search(self, search_book):
        if search_book in self.checklist:
            return 1
        else:
            return 0
    
class bookArea:
    """Finding where exactly in the library the book is located"""
    def area(self, search_book):
        searchArea = random.randint(1,25) # Randomly generates a row to find the book in
        sectionDivider = random.randint(0,1) # Randomly generates a section to find the book in

        if sectionDivider == 0:
            sectionDivider = "Fiction"
        elif sectionDivider == 1:
            sectionDivider = "Non-Fiction"

        return f"{search_book} is located in row {searchArea} of the {sectionDivider} area."

def main():
    """Runs the program"""
    LibrarySearch().mainloop()

if __name__ == "__main__":
    main()