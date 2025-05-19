# wsaa-project
Repository for the Web Services and Application project

## 📖 Project Overview
This readme documents the WSAA project, showing the use of RESTFUL APIs using Flask. It contains a web interface which enables a user to perform CRUD operations to enter details for a workout, add a client to the client table and details to track the changes in weight of a client throughout their workout journey. 

### Project requirements
- Implement RESTful API
- Connect to at least one database table
- Perform full CRUD operations
- Web interface to interact with data

### Features Implemented
- ✔️ RESTful API for workout session data
- ✔️ Web interface with AJAX for front-end interaction
- ✔️ Full CRUD functionality
- ✔️ Multiple database tables (`users`, `workouts`, `weight_management`)
- ✔️ Online hosting via Pythonanywhere
- ✔️ UI/UX improvements

## Project Setup

### Cloning repository from GitHub

1. Copy the following URL:
https://github.com/Ange-Dvs/wsaa-project.git

2. Open CMDER or if using VS Code open the terminal pane

3. Navigate to the folder where you want to clone the repository to on your machine and type git pull
``git clone https://github.com/Ange-Dvs/wsaa-project.git``

4. Set merge as the mode for the pull
``git config pull.rebase false``

5. Initiate the pull of the GitHub repository
``git pull``

6. If the pull has been successful, you should see 6 files pulled from GitHub. The ``readme.md``, the ``.gitignore`` file, the XXX files contained within.

### Running the project
1. Ensure Python and necessary libraries are installed
  - ``requirments.txt`` can be used to install necessary libraries: 
   ``pip install -r requirements.txt``
2. Set up the database using `db_setup.sql`
3. Run the app locally:
  ```bash
  python server.py
  ```

### Software used
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript (AJAX)
- **Database:** MySQL
- **Local Development Server:** WAMP
- **Online hosting:** Pythonanywhere

## Walkthrough of project

### Project Structure
- `dao` – folder containing all the DAO files containing the interactions with the database
- `html` – folder containing the html files for the web interface
- `sql_setup` - folder containing two SQL files. One containing the logic for creating the tables (`db_setup.sql`) and another containing command to insert some sample dummy data for testing if needed (`seed_data.sql`)
- `server.py` – Flask application
- `requirements.txt` – details of the packages used in the project
- `README.md` – project documentation
- `dbconfig.py` - config file containing details for connecting to SQL database

### Database Design
Tables: `users`, `workouts`, `weight_management`

![ER Diagrams for tables](docs/sql_er_diagram.png)
The above shows the details and relationship between the tables. The green line indicates the keys which are linked, both workouts and weight_management have foreign key constraints with the userID within the users table. 

If a user is deleted from the users table it will delete the entries tied to that used in the other tables. This is keep the database clean and only keep data for active users. 

### 


## Libraries used 

Within the assignments various libraries are used including: 
- ``flask`` send_from_directory
- ``LIB2``
- ``LIB3``
- ``LIB4``
- ``LIB5``
- Built-in/Standard library

<font size="4"><b>Library Name</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Summary of library and context for project

The following are methods used throughout the assignments from `LIB1`: 

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

### Template for libraries used 

<font size="4"><b>Library Name</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Summary of library and context for project

The following are methods used throughout the assignments from `LIB1`: 

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]

> ``.XXXX`` (Function/Method/Module/Class from `XXX` module ) - Summary and how used.[^reference]


***
End 

**Author:**   
Angela Davis