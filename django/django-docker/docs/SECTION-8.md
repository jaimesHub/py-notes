# Configure Database
- [reference code](https://github.com/LondonAppDeveloper/c2-recipe-app-api-2/compare/s-08-configure-database-07-create-core-app...s-08-configure-database-08-write-tests-for-wait-for-db-command)

## Database architecture overview
- Database
    - PostgreSQL
        - popular open source DB
        - Integrates well with Django
    - Docker Compose
        - Define w project (re-usable)
        - Persistent data using volumes
        - Handles network configration
        - Environment variable configuration
- Architecture
```
        -Docker compose-
        Database <---> App
```
- Network connectivity - How ?
    - Set `depends_on` on `app` service to start `db` first
    - Docker Compose creates a network
    - The `app` service can use `db` hostname

- Volumes
    - Persistent data
    - Maps directory in container to local machine

## Add database service [Follow Along]
- Update `docker-compose.yml` file
    - define `db` service
        - docker hub -> postgres -> tags -> search: 13-alpine (lightweight version)
    - define `volumes` for `postgresql`
    - setup `environment` to create `database`, `user`, `password` for `postgresql` container
    - tell the `app` service how to connect to the `db` service by using same `environment` variables
    - setup `depends_on` for `app` service
- Running `docker-compose up -d`

## Database configuration w Django
- Steps for configuring database
    - Configure Django: `tell Django how to connect`
    - Install database adaptor dependencies: `install the tool Django uses to connect`
    - Update Python requirements: Postgres adapter
- Before Django can connect to DB, it needs to know...
    - Engine (type of database)
    - Hostname (IP or domain name for DB)
    - Port (5432)
    - Database Name
    - Username
    - Password
- Defined in `settings.py`
    - `DATABASES` variable
    - `os.environ.get('DB_HOST')`
- Environment variables
    - Pull config values from environment variables
    - Easily passed to Docker
    - Used in local dev or prod
    - Single place to configure project
- Psycopg2
    - The package that you need in order for Django to connect to our DB
    - Most popular Postgresql adapter for Python
    - Supported by Django
    - Installation Options
        - psycopg2-binary
            - ok for dev
            - not good for prod
        - psycopg2 --> use in this course
            - compiles from source
            - required additional dependencies
            - easy to install w Docker
    - Installing
        - List of package dependencies in docs
            - C compiler
            - python3-dev
            - libpq-dev
        - Equivalent packages for Alpine
            - postgresql-client
            - build-base
            - postgresql-dev
            - musl-dev
        - Found by searching and trial and error
        - Docker best practice:
            - Clean up build dependencies

## Install PostgreSQL database adaptor
- Update `Dockerfile` file
- Update `requirements.txt` file
- `docker-compose down` -> remove all services
- `docker-compose build` -> rebuild Dockerfile

## Configure database in Django
- Updating `app/settings.py` file -> `DATABASES` variable
- Compare `docker-compose.yml`>app>environment file's configuration with `app/settings.py`>`DATABASES`

## Fixing database race condition
- Problem w Docker compose
    - Using `depends_on` ensures `service` starts
        - Does not ensure application is running
    - Docker services timeline [37]
- Solution
    - Make Django `wait-to-db`
    - Check for db availability
    - Continue when db ready
- Create custom Django management command
    - New timeline
- When is this an issuse ?
    - Running `docker-compose` locally
    - Running on deployed environment

## Create core app
- Command: `docker-compose run --rm app sh -c "python manage.py startapp core"` --> create `core` app
- Update `app/settings.py` file > `INSTALLED_APPS` > `core`

## Write tests for `wait_for_db` command
- `core` app
    - create `management` dir
        - create `management/commands` dir
            - `__init__.py`
            - `wait_for_db.py`
    - update `management/commands/wait_for_db.py` file
        - Class `Command`: Django command to wait for database.
        - def `handle`
    - writing the first test case
        - `tests/test_commands.py` -> `test_wait_for_db_ready()`
        - starting writing testcases: class `CommandTests`
    - running the first test case
        - command: `docker-compose run --rm app sh -c "python manage.py test"`
        - result: `FAILED (failures=1)`
        - reason: `it's been called zero times because we haven't implemented that code yet.`
    - writing the second test case
        - that is testing what happens or what should happen if the database isn't ready.
        - this means the database returns some exceptions or the check method returns some exceptions that indicate that the database isn't ready yet.
        - `tests/test_commands.py` -> `test_wait_for_db_delay()`
            - check the db
            - wait a few seconds
            - check again
            - adding `@patch("time.sleep")`
    - running test case
        - command: `docker-compose run --rm app sh -c "python manage.py test"`
    - references
        - [Writing custom django-admin commands](https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/)
        - [side_effect](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.side_effect)
        - [SimpleTestCase](https://docs.djangoproject.com/en/3.2/topics/testing/tools/#django.test.SimpleTestCase)
        - [original code](https://github.com/LondonAppDeveloper/c2-recipe-app-api-2/commit/14db901e6a096f65733fe24205f46af7486f916a)

## Add `wait_for_db` command
- Update `wait_for_db.py`
    - Update `handle` method
    - Update `logging` on the screen using `sdtout` from `BaseCommand` class
- Running test
    - command: `docker-compose run --rm app sh -c "python manage.py test"`
- Running test by calling specific testing function's name
    - command: `docker-compose run --rm app sh -c "python manage.py wait_for_db"`
    - command: `docker-compose run --rm app sh -c "python manage.py wait_for_db && flake8"`

## Database migrations
- Overview what database migrations are 
    - Django ORM
        - Object Relational Mapper
        - Abstraction layer for data
            - Django handles database structure and changes for us 
            - Focus on Python code
            - Use any database (within reason)
    - Using ORM & steps
        - Define models
        - Generate migration files
        - Setup database
        - Store data
    - Models
        - Each model maps to a table
        - Models contain
            - Name
            - Fields
            - Other metadata (for ex: relationship)
            - Custom Python logic (for ex: validation)
    - Creating migrations
        - Ensure app is enabled in `settings.py`
        - Use Django CLI: `python manage.py makemigrations`
    - Applying migrations
        - Use Django CLI: `python manage.py migrate`
        - Run it after waiting for database

- Jump into setting them up for project later

## Update docker-compose for running application
- `docker-compose.yml` -> update `command`
- `docker-compose down`
- `docker-compose up`
