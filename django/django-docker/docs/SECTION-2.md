# Section 2: App Design

## App overview
- Targeted Application: Recipe API
- Focusing on the back-end and the database of the app
- A fully functioning RestAPI
- Features: 
    - 19 API Endpoints: Managing users, recipes, tages, ingredients
    - User Authentication
    - Browseable Admin INterface (Django Admin)
    - Browseable API (Swagger)

## Technologies
- Python
- Django
    - Web Framework
    - Handles
        - URL Mappings
        - Object Relational Mapper
        - Admin Site
- Django REST Framework
    - Django add-on
    - Build REST APIs
- PostgreSQL
- Docker
    - Development environment
    - Deployment
- Swagger
    - Documentation
    - Browsable API (testing)
- Github Actions
    - Automation
        - Testing and Linting

## Django project structure
- Apps
    - `app/` - Django project
    - `app/core/` - Code shared between multiple apps such as Database definition
    - `app/user/` - User related code such as User registration & auth tokens
    - `app/recipe/` - Recipe related code
