# Setup FastAPI w Redis w Docker

- keyword yt: fastapi with redis
- [Setup FastAPI w Docker](https://www.youtube.com/watch?v=NH4VZaP3_9s&t=0s)
- [Setup Redis-Docker](https://www.youtube.com/watch?v=mA5cp5FcqeE)
- Others
    - keyword `celery fastapi`
        - https://testdriven.io/blog/fastapi-and-celery/
        - https://www.fastapitutorial.com/blog/fastapi-celery-getting-started/
    - keyword `microservice w fastapi`
        - https://www.youtube.com/watch?v=Cy9fAvsXGZA&t=1s
    - FastAPI Redis Tutorial
        - https://www.youtube.com/watch?v=reNPNDustQU

## Do some experiments
- [fastapi w redis-json](https://github.com/lemoncode21/fastapi-redisjson/tree/master)
    - setup redis container
    - setup fastapi app
        - [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
        - [error pydantic w hashmodel](https://stackoverflow.com/questions/77071277/fastapi-error-invalid-args-for-response-field-with-redis-hashmodel-pydantic-i)
        - build image: `docker build -t fastapi-service .`
        - create container: `docker run --name fastapi_ctn -p 8000:8000 fastapi-service`