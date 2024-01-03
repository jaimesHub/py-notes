# Customizing User Model - Authentication that comes with Django
- Customizing authentication in your projects requires understanding `what points` of the provided system are `extensible` or `replaceable`.
- How the auth system can be customized.

## Objectives
- The difference between `AbstractUser` and `AbstractBaseUser`
- Why we should set up a custom user model when `starting` a new Django project
- Start a new Django project with a custom user model
- *Use an email address as the primary user identifier instead of a username for authentication*
- Practice test-first development while implementing a custom user model

## Steps' Notes

### `AbstractUser` vs `AbstractBaseUser`
- `AbstractUser`: Use this option if you are happy with the existing fields on the user model and just want to remove the username field.
- `AbstractBaseUser`: Use this option if you want to start from scratch by creating your own, completely new user model.

### Project Setup
- To do list
```
$ mkdir django-custom-user-model && cd django-custom-user-model
$ python3 -m venv env
$ source env/bin/activate
(env)$ python3 -m pip install Django
(env)$ django-admin startproject hello_django .
(env)$ python3 manage.py startapp users
```

- Notes
    - `DO NOT` apply the migrations
    - You must create the custom user model `before` you apply your first migration.

- Add the new app to the `INSTALLED_APPS` list in *`settings.py`*
    - `hello_django/settings.py`

### Tests
- Let's take a test-first approach
- Making sure that these tests are failure
- `users.tests.py`
- Run test: `python3 manage.py test users`

### Model Manager
- `users/managers.py`
- [a custom `Manager`](https://docs.djangoproject.com/en/5.0/topics/db/managers/)
- [BaseUserManager]() that uses an email as the unique identifier instead of a username.

### User Model
- Decide which option we'd like to to use: subclassing `AbstractUser` or `AbstractBaseUser`
- `users/models.py`

#### AbstractUser
- [More detail](https://testdriven.io/blog/django-custom-user-model/#abstractuser)

#### AbstractBaseUser
- [More detail](https://testdriven.io/blog/django-custom-user-model/#abstractbaseuser)

### Settings
- `hello_django/settings.py`
    - adding `AUTH_USER_MODEL`
    - Django knows to use the new custom user class
- We can create and apply the `migrations`, which will create a new database that uses the `custom user model`.
    - look at what the migration will actually look like `without` creating the migration file: 
        - `python3 manage.py makemigrations --dry-run --verbosity 3`
    - Make sure the migration does not include a `username`
    - create and apply the migration:
        - `(env)$ python3 manage.py makemigrations`
        - `(env)$ python3 manage.py migrate`
    - View the schema:
        - `$ sqlite3 db.sqlite3`
        - `sqlite> .schema users_customuser`
- Question: If you went the `AbstractBaseUser` route, why is `last_login` part of the `model`?
- create a superuser: `(env)$ python3 manage.py createsuperuser`
- Make sure the tests pass: `(env)$ python3 manage.py test`

### Forms
- subclass the `UserCreationForm` and `UserChangeForm` forms so that they use the new `CustomUser` model.
- `users/forms.py`

### Admin
- Tell the admin to use these forms by subclassing `UserAdmin` in *users/admin.py*

## Run application
- `python3 manage.py runserver`

## References
- [specifying a custom user model](https://docs.djangoproject.com/en/5.0/topics/auth/customizing/#specifying-a-custom-user-model)
- [django custom user model](https://testdriven.io/blog/django-custom-user-model/)
- [--dry-run](https://docs.djangoproject.com/en/5.0/ref/django-admin/#cmdoption-makemigrations-dry-run)
- [Django Custom User Model: Log in & Sign up](https://learndjango.com/tutorials/django-custom-user-model)