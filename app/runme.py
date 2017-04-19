# Programming by Reading Installation Menu
# by Jonathan D Peterson
#
# This is a program to help setup the webserver to run.
#
# Credit
# Replacing words in a File
# Thomas Watnedal - http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python

from tempfile import mkstemp
from shutil import move
from os import close, remove
import os
import fileinput

class InstallationMenu(object):
    def __init__(self):
        self.menu_options = ["Programming by Reading Installation Menu",
                             "Purge Old Data and Create New Database",
                             "Set Client ID",
                             "Install modules",
                             "Run Server",
                             "Quit"]
        self.old_client_id = "844476090512-hq31f24hb62jg757e22im6hnjp513k37"
        self.menu()



    # Deletes the books.db then creates and populates a new books.db
    def purge_db(self):
        os.system("del books.db")
        os.system("python database_setup.py")
        print "Populating database with default books."
        os.system("python add_books_to_db.py")
        self.menu()


    # This will change the old client id (self.old_client_id) and replace it
    # with the one you input.  It will then save the one you inputed into the
    # old client Id so it can easily be changed at a later date.
    def set_client_id(self):
        print "Client ID is currently on ", self.old_client_id
        client_id = raw_input("Enter your client id: ")
        file_path = 'templates/base.jinja2'
        fh, abs_path = mkstemp()
        with open(abs_path,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(self.old_client_id, client_id))
        self.old_client_id = client_id
        close(fh)
        #Remove original file
        remove(file_path)
        #Move new file
        move(abs_path, file_path)
        self.menu()


    def install(self):
        os.system('pip install -r requirements.txt')
        self.menu()


    def runserver(self):
        os.system('python run.py')


    def menu(self):
        selection = {1 : self.purge_db,
                     2 : self.set_client_id,
                     3 : self.install,
                     4 : self.runserver,
                     5 : exit}

        for x in range(0,len(self.menu_options)):
            if x > 0:
                print x,
            print self.menu_options[x]
        choice = int(raw_input("Enter your choice: "
                    ))
        if choice < 1 or choice > len(self.menu_options):
            print "Invalid Choice!"
            self.menu()
        selection.get(choice)()

menu = InstallationMenu()
