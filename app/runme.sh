# ~/bin/bash
#
# Author: Jonathan D. Peterson
#
# This is a file which will help set up the client to run this software
# under the vagrant machine. It will load up the necessary files requirements
# to run the program, and launch it.
#

echo "Program by Reading Installation Process beginning..."

# Check and remove books.db if it exists
if ls books.db 1> /dev/null 2>&1; then
    echo "Removing old books.db file"
else
    echo "No books.db to remove"
fi

# Create a new database
echo "Creating new books.db file."
python database_setup.py

# Add books to database
python add_books_to_db.py
echo "Filling up the database with books"

# Check to see if pip exists, if not then download it.
if ! foobar_loc="$(type -p "$pip")"; then
  echo "Python module 'pip' does not exist. Retrieving it."
  sudo apt-get install python-pip python-dev build-essential
  sudo pip install --upgrade pip
fi

echo "Attempting to update the needed Python modules"
sudo pip install -r requirements.txt

echo "Initial installation complete. Edit config.py to update 0.0.0.0"
