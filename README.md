# Flask Project Template
This is a basic Flask project template that includes the following features:

-Flask-SQLAlchemy for handling database connections and ORM
-Flask-Session for handling user sessions
-File upload functionality using the Flask-Uploads module
## Getting Started
To get started with this template, follow these steps:

1. Clone the repository: git clone https://github.com/<your-username>/flask-template.git
2. Navigate to the project directory: cd flask-template
3. Install the required packages: pip install -r requirements.txt
4. Create the database: python and then from routes import *, db.create_all(), db.session.commit()
5. Run the app: python app.py
## File Structure
The project has the following file structure:

Copy code
- flask-template/
 - ├── app.py
 - ├── models.py
 - ├── routes.py
 - ├── static/
  - │   └── uploads/
 - ├── templates/
  - │   └── index.html
 - └── requirements.txt
***app.py***: This is the main script that runs the Flask app. It includes the app configuration and routes.
***models.py***: This file contains the database models for the app.
***routes.py***: This file contains the app routes and associated functions.
***static/***: This directory contains static assets such as images, CSS, and JavaScript files.
***templates/***: This directory contains the HTML templates for the app.
***requirements.txt***: This file lists the required packages for the app.
## Configuration
The app can be configured by modifying the following variables in app.py:

***SQLALCHEMY_DATABASE_URI***: This is the URI for the database connection.
***SECRET_KEY***: This is the secret key used for encrypting user sessions.
***UPLOAD_FOLDER***: This is the directory where uploaded files will be stored.
***ALLOWED_EXTENSIONS***: This is a list of allowed file extensions for uploaded files.
