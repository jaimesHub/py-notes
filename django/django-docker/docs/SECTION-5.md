# Section 5: Project Setup

## 1. New project overview
- `Objectives`
    - Introduction to using `Docker` for development
    - Create a `new` project
    - Using `Docker` with `Django`
    - `Setup` new Django project
    - `Linting` and `Testing`
    - Using `Docker Compose`

- `Why` use Docker?
    - `Consistent` dev and prod environment
    - `Easier` collaboration
        - Problems
            - Different version of Python
            - Different version of database
            - Different version of SDK
        - Solution: Using Docker
    - Capture all `dependencies` as code
        - Python requirements
        - Operating system dependencies
    - Easier cleanup

- `How` we'll use Docker?
    - Define `Dockerfile`
        - Contains all the operating system level dependencies that our project needs
    - Create Docker Compose `configuration`
        - Tells Docker `how` to run the images that are created from our Dockerfile configuration
    - Run all commands via `Docker Compose`

- Docker on `Github Actions`
    - Docker Hub introduced `rate limit`
        - Rate limit is basically limiting the amount of access that you have so that you need to upgrade to pay for that pipeline if you want to use more.
        - For example: 100 pulls / 6hr for unauthenticated users
        - For example: 200 pulls / 6hr authenticated users
    - Github Actions is `a shared service`
        - 100 pulls / 6hr applied for all users
    - `Authenticate` with `Docker Hub`
        - Create account
        - Setup credentials
        - Login before running job
        - Get 200 pulls / 6hr for free

## 2. Create Github Project
- Start
    - [Github](https://github.com/jaimesHub/recipe-app-api)
    - [Codechecker](https://codechecker.app/checker/londonappdev/start/recipe-app-api-2/s-05-project-setup-02-create-github-project/)

- Follow along
    - Github account
    - Project repository in Github
        - create a repo: recipe-app-api (Recipe API project)
        - clone on local computer
    - Dockerhub account: create access token
        - account settings > security > new access token > recipe-app-api > copy & close
        - github project: Settings > Security > Secrets and variables > Actions > Repository secrets > New repository secret
            - creating `DOCKERHUB_USER`: for doing Github Actions job
            - creating `DOCKERHUB_TOKEN`: for using in our code

## 3. Project setup
- `Objective`: How to use Docker and Django together
- `Commit`: https://github.com/jaimesHub/recipe-app-api/commit/06c0a3ad47ee57a3cb724dc771e9146d085e04ee

- Start
    - [Dockerfile best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- Many benefits
    - Consistent dev and prod environment
    - Easier collaboration
    - Capture all dependencies as code
    - Easier cleanup
    - Save a LOT of time
- Drawbacks
    - VSCode unable to access interpreter Python
    - More difficult to use intergrated features
        - Linting tools
        - Interactive debugger
    - Recommendation
        - Using the terminal to run all of the linting and debugging
- Configure Docker (`How` - Steps)
    - Create a Dockerfile
    - Lists steps for creating image
        - Choose a base image (python)
        - install dependencies
        - setup users
- Docker Compose (Define & Setup)
    - How our Docker image(s) should be used
    - Define our `services`
        - Name (eg: app)
        - Port mapping
        - Volume mappings
- Using Docker Compose
    - Run all commands through Docker Compose
        - `docker-compose run --rm app sh -c "python manage.py collectstatic"`
        - Docker compose syntax
            - `docker-compose`: runs a Docker Compose command
            - `run`: will start a specific container defined in config
            - `--rm`: removes the container
            - `app`: is the name of the service
        - Command that runs on the container
            - `sh -c`: passes in a shell command
            - `rest string`: Command to run insde container

### Define Python Requirements
- Start
    - [Diff](https://github.com/LondonAppDeveloper/c2-recipe-app-api-2/compare/s-05-project-setup-02-create-github-project...s-05-project-setup-04-create-python-requirements-file)
    - [Codechecker](https://codechecker.app/checker/londonappdev/start/recipe-app-api-2/s-05-project-setup-04-create-python-requirements-file/)
- Follow along
    - create `requirements.txt`

### Create project Dockerfile
- Start
    - [Diff](https://github.com/LondonAppDeveloper/c2-recipe-app-api-2/compare/s-05-project-setup-04-create-python-requirements-file...s-05-project-setup-05-create-project-dockerfile)
    - [Codechecker](https://codechecker.app/checker/londonappdev/start/recipe-app-api-2/s-05-project-setup-05-create-project-dockerfile/)
- Follow along
    - Creating `Dockerfile`
    - Adding `.dockerignore`
    - Building image

### Create Docker Compose configuration
- [Diff](https://github.com/LondonAppDeveloper/c2-recipe-app-api-2/compare/s-05-project-setup-05-create-project-dockerfile...s-05-project-setup-07-create-docker-compose-config)
- [Codechecker](https://codechecker.app/checker/londonappdev/start/recipe-app-api-2/s-05-project-setup-07-create-docker-compose-config/)

### Linting and Tests
- What is Linting?
    - Tool to check code formatting
    - Highlights errors, typos, formatting issues
- How we'll handling Linting
    - Install `flake8` package
    - Run it through Docker Compose
        - For ex: `docker-compose run --rm app sh -c "flake8"`
- Testing
    - Django test suite
    - Setup tests per Django app
    - Run tests through Docker Compose
        - For example: `docker-compose run --rm app sh -c "python manage.py test"`

### Configure flake8
- [Diff](https://github.com/LondonAppDeveloper/c2-recipe-app-api-2/compare/s-05-project-setup-07-create-docker-compose-config...s-05-project-setup-10-configure-flake8)
- [Codechecker](https://codechecker.app/checker/londonappdev/start/recipe-app-api-2/s-05-project-setup-10-configure-flake8/)

- Follow along

### Create Django project
- [Diff](https://github.com/LondonAppDeveloper/c2-recipe-app-api-2/compare/s-05-project-setup-10-configure-flake8...s-05-project-setup-11-create-django-project)
- [Codechecker](https://codechecker.app/checker/londonappdev/start/recipe-app-api-2/s-05-project-setup-11-create-django-project/)

- Follow along

### Run project with Docker Compose
- Follow along

### Project setup overview

### Quiz 2: Docker and Docker Compose


