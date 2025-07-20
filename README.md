Django Login System
This project is a Django-based web application that provides a robust system for user signup, login, and profile management. It includes functionalities such as user registration, user data retrieval, updating user details, and deleting user accounts. The API endpoints for these operations have been thoroughly tested with Postman to ensure reliability and functionality.

Key Features
User Authentication: Implements views for user signup and login functionality.

User Data Management: Provides full CRUD (Create, Read, Update, Delete) operations for user data.

API Endpoints: CRUD operations are exposed via a set of API endpoints, testable with a tool like Postman.

Models
The core of the project is the UserDetails model, defined in Loginify/models.py.

Field	Type	Description
username	CharField	Unique identifier for the user; serves as the primary key.
email	EmailField	The user's email address, which must be unique.
password	CharField	The user's password.

Export to Sheets
Getting Started
Follow these steps to set up and run the project locally.

Prerequisites
Python (3.7+)

Git

Installation
Clone the repository:

Bash

git clone https://github.com/YourUsername/YourRepoName.git
cd YourRepoName
Create and activate a virtual environment:

Bash

python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows
Install dependencies:

Bash

pip install -r requirements.txt
(Note: You will need to create a requirements.txt file from your environment)

Run migrations:

Bash

python manage.py makemigrations Loginify
python manage.py migrate
Create a superuser (optional):

Bash

python manage.py createsuperuser
Start the development server:

Bash

python manage.py runserver
The server will be running at http://127.0.0.1:8000/.

API Endpoints
You can test the following API endpoints using Postman.

Method	Endpoint	Description
POST	/users/create/	Creates a new user account.
GET	/users/	Retrieves a list of all users.
GET	/users/<email>/	Retrieves a single user's details by email.
PUT	/users/<email>/update/	Updates an existing user's details by email.
DELETE	/users/<email>/delete/	Deletes a user by email.
