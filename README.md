# E-Commerce Registration Module

This is a Flask-based registration module for an e-commerce application.

## Setup

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the application:
    ```bash
    python run.py
    ```

3.  Open your browser and navigate to `http://127.0.0.1:5000/`.

## Features

*   User Registration
*   User Login
*   User Authentication Management (Login/Logout)
*   Form Validation (WTForms)
*   Password Hashing (Bcrypt)
*   Database Integration (SQLAlchemy)
*   Bootstrap UI

## Project Structure

*   `app/`: Contains the application code.
    *   `templates/`: HTML templates.
    *   `static/`: CSS and other static files.
    *   `forms.py`: WTForms definitions.
    *   `models.py`: Database models.
    *   `routes.py`: URL routes and view functions.
*   `config.py`: Configuration settings.
*   `run.py`: Entry point for running the application.
