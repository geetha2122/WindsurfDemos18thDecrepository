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

## Testing

To run the unit tests:

```bash
pytest
```

## Deployment

The application is configured for deployment using Docker or platforms like Heroku/Render.

### Docker

1.  Build the image:
    ```bash
    docker build -t ecommerce-app .
    ```

2.  Run the container:
    ```bash
    docker run -p 5000:5000 ecommerce-app
    ```

### Production (Windows/Linux)

The project is configured to use **Waitress**, a production-quality WSGI server that works on both Windows and Linux.

To run locally in production mode:
```bash
waitress-serve --listen=*:5000 wsgi:app
```

### Heroku / Render

The repository includes a `Procfile` and `requirements.txt` ready for PaaS deployment.
1.  Connect your repository to the service.
2.  The service should automatically detect the Python app and `Procfile`.
