# PCsSystem

# medicalSystem
A user-friendly application designed for efficient management of personal computers within a system. It offers a range of functionalities, including searching for computers based on specific criteria, deleting entries, adjusting prices, and verifying devices existence using attributes. Powered by a PostgreSQL database, this project enables seamless storage, retrieval, and manipulation of computer-related data. With its intuitive design and comprehensive features, it provides an effective and streamlined solution for computer management.

<p align="center">
  <br>
  <img src="https://i.imgur.com/y2V8fIb.png" alt="pic" width="400">
  <br>
</p>
<p align="center" >
  <a href="#Files">Files</a> •
  <a href="#Features">Features</a> •
  <a href="#how-to-use">How To Use</a> 
</p>

## Files

- src: the file that implements de solution.
  - PCsSystem.py: A Python script that implements a GUI application called "PCs System" using the Tkinter library. It allows users to search, delete, adjust prices, and check PCs in a system. The application connects to a PostgreSQL database and provides a user-friendly interface for managing PCs.
  - PCsSystemTables.sql: Database tables information.

## Features
The main features of the application include:
- GUI Application: The script creates a graphical user interface (GUI) application using the tkinter library. It provides a user-friendly interface for interacting with the PCs System.
- Database Connectivity: The script establishes a connection to a PostgreSQL database using the psycopg2 library. It enables the application to interact with the database for performing various operations.
- Menu UI: The application displays a menu with different options for managing the PCs System. It includes buttons for searching PC, deleting PC, adjusting PC price, and checking PC existence.
- Search PC Function: The script implements a function for searching PCs based on their velocity and RAM specifications. It retrieves matching PCs from the database and displays the results using message boxes.
- Delete PC Function: The script implements a function for deleting a PC from the system. It prompts the user to enter the model number of the PC to be deleted and removes the corresponding records from the database.
- Adjust Price Function: The script provides a function for adjusting the price of a PC. It subtracts $100 from the price of the PC with a given model number and updates the database accordingly.
- Check PC Function: The script implements a function for checking the existence of a PC in the system. It validates if a PC with the specified attributes (maker, model, velocity, RAM, disc size, and price) already exists in the database and displays an appropriate message.


## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

...
```bash
# Clone this repository
$ git clone https://github.com/bl33h/PCsSystem

# Install dependencies
$ pip install tkinter #

# Open the folder
$ cd src

# Run the app
$ python PCsSystem.py

```
