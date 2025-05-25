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
``python server.py``

### Software used
- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript (AJAX)
- **Database:** MySQL
- **Local Development Server:** WAMP
- **Online hosting:** Pythonanywhere

## Walkthrough of project
The project is setup with the idea being an app for personal trainers to help their clients track their fitness journey. 

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

### DAO files

There are 3 DAO files, ``usersDAO``, ``weightDAO`` and ``workoutsDAO``.
The DAO files contain the logic for interactions with the MySQL database and performing CRUD operations on the different database tables.
The credentials for connecting to the database are imported from the ``dbconfig.py`` file. 
The SQL queries are parameterized to avoid SQL injection, which allows for the executions to be reused as needed when called, ``cursor.execute()`` fills the placeholders (represented by ``%s``) with data provided by the user in the UI.

The ``getcursor()`` method handles establishing the connection to the MySQL database, it returns a cursor object which is used for executing the SQL queries.

The ``closeAll()`` method is used to close the cursor after the SQL query is executed, preventing leaks. 

### HTML files

#### ``index.html``
The ``index.html`` page is used as the homepage offering different routes to navigate to and a view of some summary statistics.

<u>Features</u>  

Navigation:
- User Management
- Workout Logs
- Weight Tracker

Live summary cards: 
- Total workouts, average duration of the exercise, most popular workout types
- Total users, average age of users and most popular fitness goal

#### ``users.html``

The ``users.html`` page allows to view and manage users within the database.

<u>Features</u>

- Displays the list of users in a table
- Add new users via form
- Edit existing users
- Delete users 
- Filter by a User ID

<u>Backend Endpoints Used</u>

- `GET /api/users`
- `POST /api/users`
- `PUT /api/users/<id>`
- `DELETE /api/users/<id>`

#### ``workoutsviewer.html``

The ``workoutsviewer.html`` page allows the user to manage workout session entries for all users. 
There is also the possibility to filter the workouts by a particular user ID. 

<u>Features</u>

- View workout logs in a dynamic table
- Add new sessions
- Edit or delete sessions
- Filter logs by user
- Display session types, location, duration, difficulty, and rating

<u>Backend Endpoints Used </u>

- `GET /api/workouts`
- `POST /api/workouts`
- `PUT /api/workouts/<id>`
- `DELETE /api/workouts/<id>`

#### ``weightviewer.html``

The ``weightviewer.html`` page allows the changes in a users weight over time to be tracked. 

<u>Features</u>

- View current, starting, and target weight
- Add new weight entries
- Update or delete existing entries
- Sortable table display

<u>Backend Endpoints Used</u>

- `GET /api/weights`
- `POST /api/weights`
- `PUT /api/weights/<id>`
- `DELETE /api/weights/<id>`

#### Technologies
- jQuery 3.4.1
- Bootstrap 4.3.1
- Flask backend API

### Current limitations & Area's for improvement
While this use case is selected for demonstration purposes for the project, it is important to acknowledge some limitations that would need to be addressed before this could be utilized with real data.

- **User Authentication**:  
Current any user logged in can perform CRUD operations on the tables. There is no distinction between a regular user and admins. 
If this was to be used by an array of users i.e. personal trainers and clients, it would be better to have different roles and access to tables based on the logged in user.

- **Data privacy & GDPR**:  
Personally Identifiable Information like User IDs, workout logs and sensitive fitness goals are openly handled and available with the current set up. While enhanced user restrictions would improve this, there would like need to be a data retention policy with the information accessible to the user. 
If any information did qualify as PII the necessary actions would need to be taken to ensure that the usage is compliant with GDPR laws. 

- **Metrics**:  
Currently the landing page is showing general metrics across all users for the users and workouts table. If user based authentication and access was introduced the metrics displayed the metrics could be enhanced so that a personal trainer could see the overall system view and client only seeing metrics relevant for their user ID, using the dates entered for weights it would be possible to track a users weight overtime to visualise the data.

- **Accessibility**:  
Certain aspects of the HTML files would need to be enhanced from an accessibility perspective. Currently navigation works using mouse and keyboard and in Chrome, the native tabbing works for moving throughout the pages. This would help users would could not use a mouse. In terms of users would may rely on a screen reader ARIA labels would be a potential path forward to help with screen reader compatibility.

## Frameworks, Libraries, and Tools Used

Within the assignments various libraries are used including: 
- ``Flask``
- ``Flask-CORS``
- ``mysql-connector-python``
- ``jQuery``
- ``Bootstrap 4``
- Built-in/Standard library
- Pythonanywhere

<font size="4"><b>Flask</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flask is a lightweight WSGI web application framework used to build the backend REST API for handling requests related to users, workouts, and weight logs. It also serves static HTML pages. Used in `server.py`

The following are components are used throughout the assignments from `Flask`: 

> ``Flask()`` (Class) -  Initializes the app: ``app = Flask(...)``.[^1]

> ``@app.route()`` (Decorator) - Defines API and HTML routes like ``/api/users``, ``/workouts``, etc..[^2]

> ``send_from_directory()`` (Function) - Used to return HTML files stored in a folder (e.g., ``index.html``)..[^3]

> ``jsonify()`` (Function) - Retrieves JSON data from POST/PUT requests.[^4]

> ``abort()`` (Function) - Raises an HTTP Exception for given status code.[^5]

> ``CORS(app)`` (Function) - From the ``Flask-CORS`` extension. This function enables CORS on the app instance so that the frontend is able to make requests to the backend in ``server.py``.[^6]

<font size="4"><b>mysql-connector-python</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Used for interacting with the MySQL database across all DAO files (users, workouts, weight), used in DAO files.

> ``mysql.connector.connect()`` (Function) -  Establishes a database connection, the function contains the details to be used to initiate the connection including the ``host``, ``user``, ``password`` and ``database``.[^7]

> ``cursor.execute(...)`` (Method) - Executes a given SQL query. Within the DAO files, .[^8]

> ``cursor.fetchall()`` / ``cursor.fetchone()`` (Method) - Retrieves query results, ``fetchall`` will return multiple lines while ``fetchone`` returns one.[^9]

> ``db.commit()`` (Method) - Commits changes for INSERT/UPDATE/DELETE operations. This method should be called after every transaction that is expected to modify data for a table.[^10]

<font size="4"><b>jQuery</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Used in the HTML files to make asynchronous API calls and manipulate the DOM

> ``$.ajax()`` (Function) - Sends asynchronous requests to endpoints like ``/api/users``, ``/api/workouts``, etc.[^11]

> ``document.getElementById(...).innerText`` / ``.innerHTML`` (DOM Properties) - Used to update the content of HTML elements dynamically.[^12]

> ``$(document).ready()`` (Function) - Initializes fetches like fetchAllUsers() when the page loads.[^13]

<font size="4"><b>Bootstrap 4</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CSS framework used for responsive and styled HTML UI components like buttons, tables and form inputs, used within all HTML files for the project. It improves  the user interface aesthetics and responsiveness without custom CSS code.

Some examples used in the HTML files for the project:

> ``.btn``/ ``.btn-primary`` (Class) - To be used with ``<button>`` to create styled buttons with consistent padding, borders, and hover effects. [^14]

> ``.form-control``  (Class) – Used to style form input fields, ensuring consistent height, padding, and border appearance. [^15]

> ``.table`` (Class) – Provides a styled base for HTML tables with spacing, borders, and typography. [^16]

> ``.card`` (Class) – Creates a boxed content container with padding, border, and shadow; used for UI panels and summaries. [^17]

> ``.container`` (Class) – A responsive layout wrapper that centres content and provides horizontal padding. [^18]

> ``.thead-dark`` (Class) – Styles table headers with a dark background and light text for contrast. [^19]

<font size="4"><b>Python Standard Library</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Used throughout the Python files for the project.

The following are methods used throughout the assignments from `Python Standard Library`: 

> ``json`` (Module) - Used to convert data from Python dictionaries and JSON format in Flask routes. This allows an API to receive request bodies using ``.get_json()`` and return a structured responses using ``jsonify()``. [^20]

> ``datetime`` (Module) - Used to handle or parse dates, particularly for ``workout_date`` and ``logDate`` values within the project to ensure the dates are in the desired format of YYYY-MM-DD.[^21]

<font size="4"><b>Pythonanywhere</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This project is hosted on PythonAnywhere, a web-based platform for running Python applications. The Flask backend and serve the HTML pages, making the app publicly accessible for testing and demonstration.

URL for project hosted on Pythonanywhere: https://adproject.pythonanywhere.com/

**Steps for setting up Pythonanywhere:**
1. Create an account:  
Sign up at https://www.pythonanywhere.com

2. Import the project:  
Using the ``BASH`` console the GitHub repo was cloned. 

3. Install dependencies:   
Run ``pip3 install --user -r requirements.txt`` in the ``BASH`` console.

4. Configure the web app:  
In the "Web" tab, click "Add a new web app", chose Flask and select the correct Python version. Set ``server.py`` as the file to use for the Flask app.

5. Update WSGI file:  
Edit the WSFI configuration file to ensure it imports the app from the correct module:   
&nbsp;&nbsp;&nbsp;``from server import app as application`` 

6. Confirm the directory: 
Within the **Code** section of the "Web" tab, validate that the directory is set to the correct folder where the ``server.py`` file is located.  

7. Reload the app:  
Click the "Reload" option at the top of the page, the site will then be live with the desired configuration. 

***
End 

**Author:**   
Angela Davis

[^1]: https://flask.palletsprojects.com/en/latest/api/#module-flask
[^2]: https://flask.palletsprojects.com/en/latest/api/#flask.Flask.route
[^3]: https://flask.palletsprojects.com/en/latest/api/#flask.send_from_directory
[^4]: https://flask.palletsprojects.com/en/latest/api/#flask.json.jsonify
[^5]: https://flask.palletsprojects.com/en/latest/api/#flask.abort
[^6]: https://flask-cors.readthedocs.io/en/latest/#simple-usage
[^7]: https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
[^8]: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
[^9]: https://www.geeksforgeeks.org/querying-data-from-a-database-using-fetchone-and-fetchall/
[^10]: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html
[^11]: https://api.jquery.com/jQuery.ajax/#jQuery-ajax-url-settings
[^12]: https://www.w3schools.com/jsref/prop_html_innerhtml.asp#:~:text=Try%20it%20Yourself%20%C2%BB-,The%20Differences%20Between%0AinnerHTML%2C%20innerText%20and%20textContent,-The%20innerHTML%20property
[^13]: https://api.jquery.com/ready/
[^14]: https://getbootstrap.com/docs/4.3/components/buttons/#button-tags
[^15]: https://getbootstrap.com/docs/4.3/components/forms/#form-controls
[^16]: https://getbootstrap.com/docs/4.3/content/tables/
[^17]: https://getbootstrap.com/docs/4.3/components/card/
[^18]: https://getbootstrap.com/docs/4.3/layout/overview/#containers
[^19]: https://getbootstrap.com/docs/4.3/content/tables/#table-head-options
[^20]: https://docs.python.org/3/library/json.html
[^21]: https://www.geeksforgeeks.org/python-datetime-module/
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]:
[^1]: