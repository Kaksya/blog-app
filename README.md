# Blog Application

A simple Django-based blog application for creating, managing, and displaying blog posts.

## Overview

This is a lightweight blog platform built with Django 6.0.5. It provides a clean interface for managing blog content with basic CRUD operations and user-friendly views for reading blog posts.

## Features

- **Blog Management**: Create, read, and manage blog posts
- **Admin Interface**: Django admin panel for easy content management
- **Dynamic Content**: Store and display blog posts with timestamps
- **About Page**: Dedicated about page for site information
- **Responsive Templates**: Built-in template system for consistent presentation

## Tech Stack

- **Framework**: Django 6.0.5
- **Database**: SQLite (default, configurable)
- **Language**: Python 3.x
- **Frontend**: HTML/Django Templates

## Project Structure

```
blog/
├── blog/                  # Project configuration
│   ├── __init__.py
│   ├── settings.py       # Django settings
│   ├── urls.py           # URL routing
│   ├── asgi.py           # ASGI config
│   └── wsgi.py           # WSGI config
├── core/                 # Main application
│   ├── migrations/       # Database migrations
│   ├── __init__.py
│   ├── models.py         # Data models
│   ├── views.py          # View functions
│   ├── urls.py           # App URL routing
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   └── tests.py          # Unit tests
├── templates/            # HTML templates
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database
└── README.md             # This file
```

## Models

### Blog

- **title** (CharField, max_length=200): The blog post title
- **content** (TextField): The main blog post content
- **created_at** (DateTimeField): Automatic timestamp for post creation

## Views

- **blog()**: Displays the main blog page
- **about()**: Displays the about page

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone the repository**

    ```bash
    cd blog
    ```

2. **Create a virtual environment** (recommended)

    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**
    - On Windows:
        ```bash
        env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```

4. **Install dependencies**

    ```bash
    pip install django==6.0.5
    ```

5. **Apply migrations**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser** (for admin access)
    ```bash
    python manage.py createsuperuser
    ```

## Running the Application

1. **Start the development server**

    ```bash
    python manage.py runserver
    ```

2. **Access the application**
    - Blog page: http://localhost:8000/blog/
    - About page: http://localhost:8000/about/
    - Admin panel: http://localhost:8000/admin/

## Usage

### Adding Blog Posts

1. Go to the admin panel (http://localhost:8000/admin/)
2. Log in with your superuser credentials
3. Navigate to the Blog section
4. Click "Add Blog" to create a new post
5. Enter the title and content
6. Save the post

### Accessing Blog Posts

- Visit http://localhost:8000/blog/ to view all blog posts
- Visit http://localhost:8000/about/ to view the about page

## Configuration

### Key Settings (blog/settings.py)

- **DEBUG**: Set to `False` in production
- **ALLOWED_HOSTS**: Add your domain names here for production
- **INSTALLED_APPS**: Currently includes the 'core' app
- **DATABASES**: SQLite by default; modify for PostgreSQL or MySQL

## Security Notes

⚠️ **Important for Production**:

- Change the `SECRET_KEY` in settings.py
- Set `DEBUG = False`
- Configure `ALLOWED_HOSTS` with your domain
- Use environment variables for sensitive data
- Set up a proper database (PostgreSQL recommended)
- Use HTTPS
- Configure CSRF and CORS properly

## Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

After modifying models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Shell Access

For interactive Python shell with Django context:

```bash
python manage.py shell
```

## Deployment

### Using Gunicorn

1. Install Gunicorn:

    ```bash
    pip install gunicorn
    ```

2. Run with Gunicorn:
    ```bash
    gunicorn blog.wsgi:application --bind 0.0.0.0:8000
    ```

### Using other servers

- Refer to Django's [deployment documentation](https://docs.djangoproject.com/en/6.0/howto/deployment/)

## Troubleshooting

### Database Issues

If you encounter database errors:

```bash
python manage.py migrate --run-syncdb
```

### Static Files

For production static files:

```bash
python manage.py collectstatic
```

## Future Enhancements

- User authentication for blog authors
- Comment system for readers
- Search functionality
- Categories and tags
- Pagination for blog listing
- Rich text editor (TinyMCE, CKEditor)
- API endpoints for content

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Contact

For questions or suggestions, please contact the project maintainer.

---

**Last Updated**: 2026-05-25
