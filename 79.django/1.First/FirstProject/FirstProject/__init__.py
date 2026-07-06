# Run server on a custom port
'''python manage.py runserver 8001'''

# Check all available Django commands
'''python manage.py help'''

'''
FirstProject/
│
├── manage.py                  # Command-line utility to manage the Django project
│
├── FirstProject/              # Main project package
│   │
│   ├── __init__.py            # Marks this directory as a Python package
│   │
│   ├── settings.py            # Project configuration (database, apps, middleware, etc.)
│   │
│   ├── urls.py                # Main URL routing file
│   │
│   ├── asgi.py                # Entry point for ASGI-compatible web servers
│   │
│   └── wsgi.py                # Entry point for WSGI-compatible web servers
│
└── db.sqlite3                 # Default SQLite database (created after migration)'''

### manage.py
# Used to execute Django management commands.
# Examples:
# python manage.py runserver
# python manage.py migrate
# python manage.py createsuperuser


### settings.py
# Contains project settings such as:
# - Installed applications
# - Database configuration
# - Middleware
# - Templates
# - Static files
# - Security settings
# - Language and Time Zone


### urls.py
# Maps URLs to views.
# Example:
# /home/ -> home() view
# /about/ -> about() view

### wsgi.py
# Used when deploying the Django application using WSGI servers
# such as Gunicorn or uWSGI.

### asgi.py
# Used for asynchronous applications.
# Supports WebSockets, async views, and real-time communication.

### __init__.py
# Indicates that the folder is a Python package.
# Usually remains empty.

### db.sqlite3
# Default SQLite database created by Django.
# Stores application data during development.