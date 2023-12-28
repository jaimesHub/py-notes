# PART 1
## Creating a project
- Linux/MacOS: `$ django-admin startproject mysite`
- Windows: `...\> django-admin startproject mysite`

## Structure
- `mysite/` : is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
    - `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in [django-admin and manage.py](https://docs.djangoproject.com/en/5.0/ref/django-admin/).
    - `mysite/` : is a directory that is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. `mysite.urls`).
        - `__init__.py`: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read [more about packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) in the official Python docs.
        - `settings.py`: Settings/configuration for this Django project. `Django settings`(https://docs.djangoproject.com/en/5.0/topics/settings/) will tell you all about `how settings work`.
        - `urls.py` : The URL declarations for this Django project; a *`table of contents`* of your Django-powered site. You can read more about URLs in [URL dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/).
        - `asgi.py` : An entry-point for ASGI-compatible web servers to serve your project. See [How to deploy with ASGI](https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/) for more details.
        - `wsgi.py` : An entry-point for WSGI-compatible web servers to serve your project. See [How to deploy with WSGI](https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/) for more details.

## The depoloyment server
- Run the following commands: 
    - `cd myapp/`
    - `python3 manage.py runserver`

## Creating the Polls app
- Each application you write in Django consists of a Python package that follows a certain convention.
- [Projects vs. apps](https://docs.djangoproject.com/en/5.0/intro/tutorial01/#creating-the-polls-app)
- Your apps can live anywhere on your [Python path](https://docs.python.org/3/tutorial/modules.html#tut-searchpath)
- Creating `polls` app: `$ python3 manage.py startapp polls` -> check `~./django/myapp/polls`

## Write your first view
- `polls/views.py`
- URLconf
- `polls/urls.py`
- `myapp/urls.py`
    - django.urls.include 
        - [include()](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.include)
        - The `include()` function allows referencing other URLconfs.
        - The idea behind `include()` is to make it easy to `plug-and-play URLs`.
        - [When to use `include()`](https://docs.djangoproject.com/en/5.0/intro/tutorial01/#write-your-first-view)
        - The [path()](https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.path) function is passed four arguments, two required: `route` and `view`, and two optional: `kwargs`, and `name`. 

# PART 2
- set up the database
- create your first model
- a quick introduction to Django’s automatically-generated admin site.

## Database setup
- `mysite/settings.py`
    - ENGINE
    - NAME
- Using other DB instead of sqlite3
    - USER, PASSWORD, and HOST must be added
    - [For more details](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-DATABASES)
    - We need to create the tables in the database before we can use them
        - `$ python manage.py migrate`
- The `migrate` command looks at the `INSTALLED_APPS` setting and creates any necessary database tables according to the database settings in your `mysite/settings.py` file
- The database migrations shipped with the app (we’ll cover those later). 

## Creating models
- A model is the single, definitive source of information about your data.
- The goal is to define your data model in one place and automatically derive things from it.
- Models: `polls/models.py`
    - Question
    - Choice

## Activating models
- To include the app in our project, we need to add a reference to its configuration class in the `INSTALLED_APPS` setting. 
- The `PollsConfig` class is in the `polls/apps.py` file, so its dotted path is `polls.apps.PollsConfig`.
    - add "polls.apps.PollsConfig" into `INSTALLED_APPS` in `myapp/settings.py`
    - Now Django knows to include the `polls` app
- Run command: `python manage.py makemigrations polls`
    - By running `makemigrations`, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) 
    - And that you’d like the changes to be stored as a migration.
- Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk.
- There’s a command that will run the migrations for you and manage your database schema automatically - that's called [migrate](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-migrate)
- Let's see what SQL that migration would run using `sqlmigrate`
    - [sqlmigrate](https://docs.djangoproject.com/en/5.0/ref/django-admin/#django-admin-sqlmigrate) command takes migration names and returns their SQL
    - Run command: `python manage.py sqlmigrate polls 0001`
    - It (sqlmigrate) doesn’t actually run the migration on your database
    - Instead, it prints it to the screen so that you can see what SQL Django thinks is required.
    - It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.
- Command: `python3 manage.py check`
- Run migrate to create thod model tables in your database
    - Command: `python3 manage.py migrate`
        - Tracking all themigraions that haven't been applied using a special table called `django_migraions`
        - And synchronizing the changes you made to your models with the schema in the database.

- Recap
    - Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones 
    - it specializes in upgrading your database live, without losing data
    - The three-step guide to making model changes:
        - Change your models (in `models.py`).
        - Run `python3 manage.py makemigrations` to create migrations for those changes
        - Run `python3 manage.py migrate` to apply those changes to the database.
    - [Full information on what the `manage.py` utility can do](https://docs.djangoproject.com/en/5.0/ref/django-admin/)

## Playing with the API
- To invoke the Python shell, use this command: `python3 manage.py shell`
- Editing the `Question` model (in the `polls/models.py` file) and adding a `__str__()` method to both `Question` and `Choice`
    - It’s important to add `__str__()` methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.
- Customizing method to `Question` model
- [For more information on model relations - `Accessing related objects`](https://docs.djangoproject.com/en/5.0/ref/models/relations/)
- [How to use double underscores to perform field lookups via the API - `Filed lookups`](https://docs.djangoproject.com/en/5.0/topics/db/queries/#field-lookups-intro)
- [For full details on the database API - `Database API reference`](https://docs.djangoproject.com/en/5.0/topics/db/queries/)

## Introducing the Django Admin
- The admin isn’t intended to be used by site visitors. It’s for site managers.

### Creating an admin user
1. Creating a user who can login to the admin site
    - Command: `python3 manage.py createsuperuser` and following the instructions

2. Start the development server
- The Django admin site is activated by default
- Start the server: `python3 manage.py runserver`

3. Enter the admin site
- A few types of editable content: `groups` and `users`.
- They are provided by `django.contrib.auth`, the authentication framework shipped by Django

4. Make the poll app modifiable in the admin
- At first, our poll app is not displayed on the admin index page
- We need to tell the admin that `Question` objects have an admin interface
    - `polls/admin.py`

5. Explore the free admin functionality
- Note: If the value of “Date published” doesn’t match the time when you created the question in Tutorial 1, it probably means you forgot to set the correct value for the TIME_ZONE setting. Change it, reload the page and check that the correct value appears.

# Part 3
## Overview
- Web pages and other content are delivered by views
- Each view is represented by a Python function (or method, in the case of class-based views)
- Django will choose a view by examining the URL that's requested
- To get from a URL to a view, Django uses what are known as `URLconfs`. A URLconf maps URL patterns to views
- This part provides
    - basic instruction in the use of URLconfs
    - refer to [URL dispatcher](https://docs.djangoproject.com/en/5.0/topics/http/urls/) for more information

## Writing more views
- Add a few more views to `polls/views.py`
- Wire these new views into `poll.urls` module by adding the following `path()` calls: `polls/urls.py`
- When somebody requests a page from your website – say, “/polls/34/”, Django will load the `myapp.urls` Python module because it’s pointed to by the `ROOT_URLCONF` setting
    - How it works

## Write views that actually do something
- Each view is responsible for doing one of two things:
    - Returning an [HttpResponse](https://docs.djangoproject.com/en/5.0/ref/request-response/#django.http.HttpResponse) object containing the content for the requested page
    - Raising an exception such as [Http404](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404)
- Your view can read records from a database or not
- All Django wants is that `HttpResponse` or an exception
- Let's Django's own database API (From Part 2)
    - `polls/views.py`: index()
    - `templates` directory
        - `polls` directory
- Your project’s [TEMPLATES](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES) setting describes how Django will load and render templates.
    - [More](https://docs.djangoproject.com/en/5.0/intro/tutorial03/#write-views-that-actually-do-something)
    - Your template should be at `polls/templates/polls/index.html`.
    - app_directories -> polls/index.html
    - A shorcut: [render()](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.render)
        - a very common idiom to load a template
        - fill a context and return an `HttpResponse` object with the result of the rendered template.
        - Input: The `render()` function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument.
        - Output: It returns an `HttpResponse` object of the given template rendered with the given context.

## Raising a 404 error
- `polls/views.py`: detail()
    - The view raises the [Http404](https://docs.djangoproject.com/en/5.0/topics/http/views/#django.http.Http404) exception if a question with the requested ID doesn’t exist.
- `polls/detail.html` template
- A shortcut: [get_object_or_404()](https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#django.shortcuts.get_object_or_404)
    - The `get_object_or_404()` function takes a Django `model` as its first argument and an arbitrary number of keyword arguments, which it passes to the `get()` function of the model’s manager.
    - It raises `Http404` if the object doesn’t exist.
    - Question: `Why` do we use a helper function `get_object_or_404()` instead of automatically catching the `ObjectDoesNotExist` exceptions at `a higher level`, or having the model API raise `Http404` instead of `ObjectDoesNotExist`?

## Use the template system
- Back to the `detail()` view for our poll application.
- Refactoring the `polls/detail.html` template
    - The template system uses `dot-lookup` syntax to access variable attributes.
    - [How it works?](https://docs.djangoproject.com/en/5.0/intro/tutorial03/#use-the-template-system)
- See the [template guide](https://docs.djangoproject.com/en/5.0/topics/templates/) for more about templates.

## Removing hardcoded URLs in templates
- problem: tightly-coupled approach
- However, since you defined the name argument in the `path()` functions in the `polls.urls` module, you can remove a reliance on specific URL paths defined in your url configurations by using the `{% url %}` template tag
    - `polls/index.html`
    ```
    <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    ```

## Namespacing URL names
- How does one make it so that Django knows which app view to create for a url when using the `{% url %}` template tag?
    - add namespaces to your URLconf
    - In the `polls/urls.py` file, go ahead and add an app_name to set the application namespace
    - change your `polls/index.html` template from
        ```
            <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
        ```