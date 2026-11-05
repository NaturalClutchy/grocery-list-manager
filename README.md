Grocery List Manager
A beginner-friendly Python command-line application for maintaining a grocery list and saving it between sessions.
Features
- Add grocery items from the terminal.
- View a numbered list of saved items.
- Remove an item by its number.
- Exit through a four-option menu.
- Read items from and write items to grocery_list.txt for persistence between runs.
Built with
Python 3 and standard-library file input/output. No third-party packages are required.
How to run
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Make sure grocery_list.txt is in that directory (it is included in the repository).
4. Run:
   python "Grocery List Manager.py"
5. Select a menu option by typing 1, 2, 3, or 4.
Example menu
==== Grocery List Manager ====
1. Add Item
2. Remove Item
3. View List
4. Exit
How the data is saved
The script loads the list from grocery_list.txt at startup and rewrites that file with the current list after each menu action. Item names are converted to lowercase when added.
Current limitations and next steps
This is a learning project. The text file is opened using a path relative to the current working directory, so run the script from the project folder. Currently, the program expects grocery_list.txt to exist; entering a non-numeric value when removing an item can raise an error. Planned improvements could include input validation and automatic file creation. These are suggestions, not implemented features.
Author
Rene Garcia — GitHub profile
