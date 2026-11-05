# Grocery List Manager

**Python Command-Line Application**

## Overview

A beginner-friendly Python application that allows users to create and manage grocery lists through a command-line interface.

The application uses text-file storage to save grocery items between sessions.

I developed this project while learning Python fundamentals, including loops, functions, lists, file handling, and user input.

## Features

- Add grocery items.
- Display a numbered grocery list.
- Remove grocery items by number.
- Save grocery items to a text file.
- Load previously saved items.
- Navigate through a four-option menu.

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Text Files | Persistent data storage |
| File I/O | Reading and writing data |

## Installation

### 1. Download or Clone the Repository

Download the project files to your computer.

### 2. Open the Project Directory

Make sure `grocery_list.txt` exists in the same folder as the Python program.

### 3. Run the Application

```bash
python "Grocery List Manager.py"
```

## Example Menu

```text
==== Grocery List Manager ====

1. Add Item
2. Remove Item
3. View List
4. Exit
```

## How It Works

1. The application loads grocery items from `grocery_list.txt`.
2. Users select an option from the menu.
3. The application performs the requested operation.
4. Changes are saved to the text file.

## What I Learned

- Working with Python lists.
- Reading and writing text files.
- Building menu-driven applications.
- Using loops and conditional statements.
- Managing user input.

## Current Limitations

- The program expects the grocery list file to exist.
- Some invalid inputs may cause errors.
- File paths are relative to the current working directory.

## Future Improvements

- Improve input validation.
- Automatically create missing files.
- Add item quantities and prices.
- Improve error handling.

These improvements are planned rather than currently implemented.

## Author

**Rene Garcia**

Computer Science/Engineering Student at UCNJ
