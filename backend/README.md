# Utibu Health App Backend

- This is the backend component of the Utibu Health mobile application, designed to cater to patients with chronic conditions. The backend is responsible for managing user authentication, medication orders, and customer statements, as well as integrating with the legacy database system of Utibu Health.

## Technologie Used
- **Python Flask**
    - The backend is built using Flask, a lightweight WSGI web application framework in Python.
- **SQLAlchemy**
    - SQLAlchemy is used as the Object-Relational Mapping (ORM) tool to interact with the SQL database.
- **MySQL**
    - MySQL  is used as the temporary database system for storing user data, medication orders, and customer statements.
    - We will migrate to MIcrosoft SQL server in future


## Getting Started
- To set up the backend locally, follow these steps:
    1. **Clone the Repository**
        git clone https:://github.com/vincent-mugendi/utibu_app.git

    2. **Install Dependancies**
        'cd backend' and then 'pip install -r requirements.txt'

    3. **Set Environment Variables**
        Create a `.env` file in the root directory and add the following variables:

            ```makefile
            FLASK_APP=app.py
            FLASK_ENV=development
            DATABASE_URL=mysql://username:password@localhost/utibu_db
            ```
        - Replace username and password with your MySQL credentials.

    4. **Initialize the Database**
        - Run `flask db upgrade` to initiliaze database

    5. **Apply Migrations**
        - Run flask db upgrade to apply the initial database migrations.

    6. **Start Server: `flask run`**
        - The backend server should now be running locally
    

## API ENDPOINTS
- **POST /order:** Place a new medication order.
- **GET /statement/<customer_id>:** Get customer statements for the specified customer ID.
- **POST /statement/<customer_id>:** Create a new customer statement.

## Migration to Microsoft SQL Server
- The migration to Microsoft SQL Server will involve updating the DATABASE_URL in the .env file to point to the new database.
- You will also need to update the SQLAlchemy configuration in app.py to use the SQL Server dialect and driver.

## Contributors
- Vincent Mugendi (@vincent-mugendi)