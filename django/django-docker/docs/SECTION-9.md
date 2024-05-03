# Create User Model

## The Django user model

### Django authentication
- Built in authentication system
- Framework for basic features
    - Registration
    - Login
    - Auth
- Integrates w Django admin

### Django user model
- Foundation of the Django auth system
- Default user model
    - Username instead of email
    - Not easy to `customise`
- Create a custom model for new projects
    - Allows for using email instead of username
    - Future proof project for later changes to user model

### How to customise user model
- Create model
    - Base from `AbstractBaseUser` and `PermissionsMixin`
- Create custom manager
    - Used for CLI integration
- Set `AUTH_USER_MODEL` in `settings.py`
- Create and run migrations

### AbstractBaseUser
- Provides features for authentication
- Doesn't include fields

### PermissionsMixin
- Support for Django permission system
- Includes fields and methods

### Common issues
- Running migrations before setting custom model
    - Set custom model first
- Typos in config
- Indentation in manager or model

## Design custom user model
- User fields
- User model manager
    - Used to manage objects
    - Custom logic for creating objects
        - Hash password
    - Used by Django CLI
        - Create superuser
- BaseUserManager
    - Base class for managing users
    - Useful helper methods
        - `normalize_email`: for storing emails consistently
    - Methods we'll define
        - `create_user`: called when creating user
        - `create_superuser`: used by the CLI to create a superuser (admin)

## Add user model tests
- Adding unit test -> Test custom user model
- `app/core/tests/test_models.py`
- command: `docker-compose run --rm app sh -c "python manage.py test"`
- [django.contrib.auth](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#django.contrib.auth.get_user_model)
- [django.contrib.auth.models.AbstractBaseUser.check_password](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser.check_password)

## Implement user model
- [auth-user-model](https://docs.djangoproject.com/en/4.2/ref/settings/#auth-user-model)
- define models on `app/core/models.py`
    - UserManager class
    - User class
- define the customize user model on `settings.py`
    - `AUTH_USER_MODEL`
- Make migrations for project
    - command: `docker-compose run --rm app sh -c "python manage.py makemigrations"`
    - This is going to create the migrations for our new custom user model that we've added to the project.
    - check on `app/core/migrations`
- Apply to database and see what happens -> Test
    - command: `docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"`
    - `error`: django.db.migrations.exceptions.`InconsistentMigrationHistory`: Migration admin.0001_initial is applied before its dependency core.0001_initial on database 'default'.
    - `reason`: this is because we apply migrations previously with the default migrations that come in the background of Django that would use the default Django user model.
    - `solution`: what we need to do is we need to clear the data for our database. -> refreshing our DB
        - in order to clear the volume: `docker volume ls` -> this will list all of the volumes on our system.
        - find the volume that relates to our system's database -> `docker volume rm recipe-app-api_dev-db-data`
        - make sure: `docker-compose down`
        - command: `docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"`
- Run test to check that they pass
    - command: `docker-compose run --rm app sh -c "python manage.py test"`

## Normalize email addresses
- `app/core/models.py`
## Require email input
- `app/core/models.py`
- `app/core/tests/test_models.py`

## Add supperuser support
- `app/core/models.py`
- `app/core/tests/test_models.py`

## Test user model
- command: `docker-compose run --rm app sh -c "python manage.py createsuperuser"`
- admin@example.com / admin