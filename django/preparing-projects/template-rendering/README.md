# Template Rendering w Context Processors

- [Templates](https://docs.djangoproject.com/en/5.0/topics/templates/)
- [Class based views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
- [Django Tutorials](https://www.pythontutorial.net/django-tutorial/)
- [Realpython w django](https://realpython.com/tutorials/django/)

- Objectives
    - how to simplify template rendering with context processors
    - [context processors](https://docs.djangoproject.com/en/stable/topics/templates/#context-processors): `how` it works & `why` it's worth using
        - They allow following DRY principle in the template rendering
        - Keeping your code more maintainable

## Get some context
- [Context](https://docs.djangoproject.com/en/5.0/ref/templates/api/#playing-with-context) is a dictionary-like object that a [template](https://docs.djangoproject.com/en/5.0/ref/templates/api/#django.template.Template) renders together with a request.
- In most cases we pass it as a standard dictionary to the `render()` shortcut.
- `What if` we have information that should be available for every template.
    - How do we inject them without `rewriting` everything and `repeating` ourselves?
    - `Context processors` are helpers designed for `exactly` this.
        - They are functions that accept a request and return a dictionary that is populated to the template context when any template is rendered.
        - The list of used context processors is controlled by the `"context_processors"` option of the `TEMPLATES` setting.
- [Built-in context processors](https://docs.djangoproject.com/en/stable/ref/templates/api/#context-processors)

## Example

- convention
    - Django projects' name using `snake_case`
- `template_context_process/settings.py`
    - Environment can be defined as a `setting`
    - [settings in django](https://docs.djangoproject.com/en/5.0/ref/settings/)
    - [urls.py](./hello-django/template_context_process/urls.py)
    - [settings.py](./hello-django/template_context_process/settings.py)
- `template_context_process/__init__.py`
    - version is stored in the project
    - [`__init__.py`](./hello-django/template_context_process/__init__.py)
- Define a new context processor called `metadata()` that will add both information to the template context
    - [template_context_process/context_processors.py](./hello-django/template_context_process/context_processors.py)
    - the dotted Python path to it (`my_project.context_processors.metadata`) to the list of context processors
        - [template_context_process/settings.py](./hello-django/template_context_process/settings.py)
        - `version` and `environment` are now available for `all` templates
- After setting context processors for all template
    - Display a header about the `current version`

### Inital Setup
- [Way 1](https://fly.io/docs/django/getting-started/#initial-set-up)
- [Way 2](https://www.djangoproject.com/start/)

## References
- [DRY: Template Rendering with Context Processors](https://fly.io/django-beats/dry-template-rendering-with-context-processors/)