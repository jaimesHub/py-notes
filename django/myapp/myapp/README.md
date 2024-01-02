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

## Recap
- the basic request and response flow

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

## Recap
- the models API
- having familiarized with the admin site

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
## Recap
- Writing views

# Part 4

## Write a minimal form
- Update detail template `(“polls/detail.html”)`
- Create a Django view that handles the submitted data and does something with it.
    - `polls/urls.py`
    - `polls/views.py` -> vote()
        - request.POST, request.GET, 
        - request.POST['choice'], KeyError
        - HttpResponseRedirect / HttpResponse, reverse() 
    - [More detail](https://docs.djangoproject.com/en/5.0/intro/tutorial04/#write-a-minimal-form)
    - [For more on HttpRequest objects](https://docs.djangoproject.com/en/5.0/ref/request-response/)
- After somebody votes in a question, the `vote()` view redirects to the results page for the question.
    - `polls/views.py` -> `results()`
- Create a `polls/results.html` template
- Problem:
    - If two users of your website try to vote at exactly the same time, this might go wrong -> `a race condition`
    - [Avoiding race conditions using F()](https://docs.djangoproject.com/en/5.0/ref/models/expressions/#avoiding-race-conditions-using-f)

## Use generic views: Less cod is better
- These views represent a common case of basic web development 
    - getting data from the database according to a parameter passed in the URL
    - loading a template and returning the rendered template
- Django provides a shortcut, called the `generic views` system
    - Generic views abstract common patterns to the point where you don’t even need to write Python code to write an app. For example:
        - [ListView](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView) views abstract the concepts of `display a list of objects`
            - IndexView
        - [DetailView](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView) views abstract the concepts of `display a detail page for a particular type of object`
            - DetailView
            - ResultsView
    - Steps to use the generic views system
        - [Convert the URLconf](https://docs.djangoproject.com/en/5.0/intro/tutorial04/#amend-urlconf)
            - `polls/urls.py`
            - IndexView.as_view(), DetailView.as_view(), ResultsView.as_view()
            - `polls/views.py`
        - Delete some of the old, unneeded views
            - `polls/views.py`
        - [Introduce new views based on Django's generic views](https://docs.djangoproject.com/en/5.0/intro/tutorial04/#amend-views)
- [For full details on generic views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)

## Recap
- Forms processing
- Generic views

# Part 5
- create some automated tests for it

## Introducing automated testing
- What are automated tests?
    - Tests are routines that check the operation of your code.
    - Testing operates at different levels.
    - What’s different in automated tests is that the testing work is done for you by the system.
- Why you need to create tests?
    - Tests will save your time
        - Up to a certain point, `checking that it seems to work` will be a satisfactory test. 
        - Checking that it still `seems to work` could mean running through your code’s functionality with twenty different variations of your test data to make sure you haven’t broken something
        - If something’s gone wrong, automated tests will also assist in identifying the code that’s causing the unexpected behavior.
    - Tests don’t just identify problems, they prevent them
        - Without tests, the purpose or intended behavior of an application might be rather opaque.
        - Tests change that; they light up your code from the inside, and when something goes wrong, they focus light on the part that has gone wrong
    - Tests make your code more attractive
        - `Code without tests is broken by design.` - Jacob Kaplan-Moss
    - Tests help teams work together
        - Tests guarantee that colleagues don’t inadvertently break your code (and that you don’t break theirs without knowing).
        - If you want to make a living as a Django programmer, you must be good at writing tests!

## Basic testing strategies
- [Test driven development](https://en.wikipedia.org/wiki/Test-driven_development) discipline
    - they actually write their tests `before` they write their code. 
    - they describe a problem, then create some code to solve it
    - Test-driven development formalizes the problem in a Python test case.
- A newcomer to testing will create some code and later decide that it should have some tests. 
- Sometimes it’s difficult to figure out where to get started with writing tests.
    - several thousand lines of Python
    - it’s fruitful to write your first test the next time you make a change, either when you add a new feature or fix a bug

## Writing our first test
### We identify a bug
- the `Question.was_published_recently()` method returns `True` if the `Question` was published within the `last` day (which is correct) but also if the `Question’s pub_date` field is in the `future` (which certainly isn’t).
- Confirm the bug
    - `python3 manage.py shell`

### Create a test to expose the bug
- let’s turn into an automated test.
- A conventional place for an application’s tests is in the application’s `tests.py` file
    - `polls/tests.py`
    - the testing system will automatically find tests in any file whose name begins with `test`.
- Running tests
    - In the terminal: `python3 manage.py test polls`
    - The test informs us which test failed and even the line on which the failure occurred.

### Fixing the bug
- Amend the method in `polls/models.py/was_published_recently`
- After identifying a bug, we wrote a test that exposes it and corrected the bug in the code so our test passes.

### More comprehensive tests
- Add two more test methods to the same class, to test the behavior of the method more comprehensively
- `polls/tests.py`
- Now we have 3 tests that confirm that `Question.was_published_recently()` returns sensible values for `past, recent, fututre` questions

## Test a view

### A test for a view
- For this test, we want to check its behavior as it would be experienced by a user through a web browser.
- Before we try to fix anything, let’s have a look at the tools at our disposal.

### The Django test client
- Django provides a test [Client]() to simulate a user interacting with the code at the view level. 
- We can use it in `polls/tests.py` or even in the shell.
- First, we set up the test environment in the `shell`: 
    - Terminal: `python3 manage.py shell`
    - [Steps](https://docs.djangoproject.com/en/5.0/intro/tutorial05/#the-django-test-client)
        - [setup_test_environment](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#django.test.utils.setup_test_environment)
        - response.context
        - `TIME_ZONE` in `settings.py`
        - You might get unexpected results if your TIME_ZONE in settings.py isn’t correct. If you don’t remember setting it earlier, check it before continuing. (`Part 2`)

### Improving our view
- The list of polls shows polls that aren’t published yet (i.e. those that have a `pub_date` in the future). Let’s fix that.
- In `Part 4`, a class-based view based on [ListView](https://docs.djangoproject.com/en/5.0/intro/tutorial05/#improving-our-view)
- Checking `get_queryset() method` and change it so that it also checks the date by comparing it with `timezone.now()`
    - `polls/views.py`
    - `def get_queryset(self)`

### Testing our new view
- Create a test, based on our `shell` session
- `polls/tests.py`
    - creating a shorcut function to create questions as well as a new test class
    - create_question()
    - class QuestionIndexViewTests()
    - [django.test.TestCase](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TestCase) class provides:
        - [assertContains()](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.SimpleTestCase.assertContains)
        - [assertQuerySetEqual()](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.TransactionTestCase.assertQuerySetEqual)

### Testing the `DetailView`
- even though future questions don’t appear in the index, users can still reach them if they know or guess the right URL
    - `polls/views.py/DetailView/get_queryset()`
- We should then add some tests, to check that a `Question` whose `pub_date` is in the past can be displayed, and that one with a `pub_date` in the future is not
    - `polls/tests.py/QuestionDetailViewTests/test_future_question`
    - `polls/tests.py/QuestionDetailViewTests/test_past_question`

### Ideas for more tests
- add get_queryset -> ResultView
- Improve our app in other ways, adding tests along the way
- logged-in admin users should be allowed to see unpublished `Questions`, but not ordinary visitors.

## When testing, more is better
- When our tests are growing out of control
    - `It doesn’t matter`. Let them grow.
    - you can write a test once and then forget about it.
- Sometimes tests will need to be updated.
- in testing redundancy is a good thing.
- Good rules-of-thumb include having
    - a separate `TestClass` for each model or view
    - a separate test method for each set of conditions you want to test
    - test method names that describe their function
## Further testing
- This guide introduces some of the basics of testing
- you can use an `in-browser` framework such as [Selenium](https://www.selenium.dev/) to test the way your HTML actually renders in a browser.
    - Django includes [LiveServerTestCase](https://docs.djangoproject.com/en/5.0/topics/testing/tools/#django.test.LiveServerTestCase) to facilitate integration with tools like Selenium.
- A good way to spot untested parts of your application is to check `code coverage`.
    - If you can’t test a piece of code, it usually means that code should be refactored or removed. 
    - Coverage will help to identify dead code
    - See [Integration with coverage.py](https://docs.djangoproject.com/en/5.0/topics/testing/advanced/#topics-testing-code-coverage) for details.

## What's next?
- [Testing in Django](https://docs.djangoproject.com/en/5.0/topics/testing/) has comprehensive information about testing.
- learn about `static files management` in the next guide

# Part 6
- we'll now add a stylesheet and an image
- web applications generally need to serve additional files — such as images, JavaScript, or HTML, CSS — necessary to render the complete web page.
- In Django, we refer to these files as `static files`.
- small projects -> we can keep the static files somewhere your web server can find it
- big projects (multiple apps) -> dealing with the multiple sets of static files provided by each application starts to get tricky.
- `django.contrib.staticfiles`
    - it collects static files from each of your applications (and any other places you specify) into a single location that can easily be served in production.

## Customize your app's look and feel
- Creating a diractoru called `static` in `polls` directory
    - `polls/static`
    - Django will look for static files there
    - similarly to how Django finds templates inside polls/templates/.
- Django’s [STATICFILES_FINDERS](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STATICFILES_FINDERS) setting contains a list of finders that know how to discover static files from various sources.
    - `AppDirectoriesFinder` (default): looks for a `static` subdirectory in each of the `INSTALLED_APPS`
    - The admin site uses the same directory structure for its static files.
- `polls/static/polls/style.css`
    - Because of how the `AppDirectoriesFinder` staticfile finder works, you can refer to this static file in Django as `polls/style.css`
    - similar to how you reference the path for `templates`.
- add code css & add them at `polls/templates/polls/index.html`
    - The `{% static %}` template tag generates the absolute URL of static files.

## Adding a background-image
- we’ll create a subdirectory for images
- Create an `images` subdirectory in the `polls/static/polls/` directory.
    - add any image file
    - `polls/static/polls/images/background.png`
- add a reference to your image in your stylesheet ((polls/static/polls/style.css))

- Note:
    - The `{% static %}` template tag is not available for use in static files which aren’t generated by Django

## References
- [the static files howto](https://docs.djangoproject.com/en/5.0/howto/static-files/) details on settings
- [the staticfiles reference](https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/) 
- [Deploying static files]() discusses how to use static files on a real server.

## Next
- learn how to customize Django’s automatically-generated admin site.

# Part 7

## Customize the admin form
- By registering the `Question` model with `admin.site.register(Question)`, Django was able to construct a default form representation.
- reordering the fields on the edit form
    `polls/admin.py`
- this pattern
    - create a model admin class
    - pass it as the second argument to `admin.site.register()`

## Adding related objects
- The first is to register `Choice` with the admin just as we did with `Question`
    - `Question` field select box: Django knows that a `ForeignKey` should be represented in the admin as a `<select>` box.
    - the `Add another question` link next to `Question`
- But, really, this is an `inefficient` way of adding `Choice` objects to the system
    - It’d be better if you could add a bunch of `Choices` directly when you create the `Question` object.
    - Remove the `register()` call for the `Choice` model. 
    - edit the `Question` registration code to read
- Problem
    - It takes a lot of screen space to display all the fields for entering related `Choice` objects
- Solution
    - Django offers a tabular way of displaying inline related objects.
    - change the `ChoiceInline` declaration to read
- [Steps](https://docs.djangoproject.com/en/5.0/intro/tutorial07/#adding-related-objects)

## Customize the admin change list
- make some tweaks to the `change list` page
- By default, Django displays the str() of each object.
- sometimes it’d be more helpful if we could display individual fields.
    - `list_display` attr
    - using the `display()` decorator: `polls/model.py`
    - [For more information](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)
- Filter
    - `polls/admin.py`: 
        - filters using the `list_filter`. Add to `QuestionAdmin`
        - add some search capability
- Change lists give you free pagination. The default is to display 100 items per page. 
    - [Change list pagination](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_per_page), 
    - [search boxes](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields), 
    - [filters](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter), 
    - [date-hierarchies](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.date_hierarchy)
    - [column-header-ordering](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)

## Customize the admin look and feel
- [Check here](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display)

### Customizing your project's templates
- Create `templates` directory: `/myapp/templates`
- Templates can live anywhere on your filesystem that Django can access
- Open `myapp/settings.py`
    - add `DIRS` option in `TEMPLATES` setting
    - [DIRS](https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-TEMPLATES-DIRS) is a list of filesystem directories to check when loading Django templates; it’s a `search path`.
- create a directory called `admin` inside `templates`
    - this approach to teach you how to override templates
    - In an actual project, you would probably use the `django.contrib.admin.AdminSite.site_header` attribute to more easily make this particular customization.

### Customizing your application's templates
- Question: if DIRS was empty by default, how was Django finding the default admin templates? 
- See the [template loading documentation](https://docs.djangoproject.com/en/5.0/topics/templates/#template-loading) for more information about how Django finds its templates.

## Cusomize the admin index page
- [Customize the admin index page](https://docs.djangoproject.com/en/5.0/intro/tutorial07/#customize-the-admin-index-page)

## Next
- learn how to use third-party packages