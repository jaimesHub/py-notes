# Pydantic Models

- [Pydantic vs ORM Models](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=19701s)
    - pydantic model: schema, shape of a request
        - `main.py`: Post, BaseModel
    - sqlalchemy model: it defines our database or our specific table looks like
        - `models.py`
        
- [Pydantic Models Deep Dive](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=19941s)
    - `Schema (Pydantic) Models`
        - Schema/Pydantic Models define the `structure` of a `request` & `response`
        - This `ensure` that when a user wants to create a post, the request will only go through
        if it has a `title` and `content` in the body
        - What exactly Schema/Pydantic models do? They (middlewares in below image) just `ensure` 
        that the `request` and `response` are `shaped` in a `specific` way.

        ![Schema Models](./assets/schema_models.png)

    - `Sqlalchemy (ORM) Models`
        - Responsible for defining the columns of our `posts` table within postgres
        - It is used to `query`, `create`, `delete`, and `update` entries within the database

- [Response Model](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=20337s)
    - Pydantic Model vs ORM Model
    - Using Pydantic Model
        - `schemas.py`
        - to handle incoming request from client
            - Define what the request look like
            - Example: `schemas.PostCreate`, `schemas.PostUpdate`
        - to handle outcoming response from server
            - Define what the response look like
                - `main.py`: @app.post("/posts", status_code=status.HTTP_201_CREATED, `response_model=schemas.Post`)
                    - [response_model parameter](https://fastapi.tiangolo.com/tutorial/response-model/#response_model-parameter)
                - [Use Pydantic's orm_mode - orm_mode=True](https://fastapi.tiangolo.com/tutorial/sql-databases/#use-pydantics-orm_mode)
                - `from typing import List`
            - Example: `schemas.Post(BaseModel)`

# References
- [response_model parameter](https://fastapi.tiangolo.com/tutorial/response-model/#response_model-parameter)
- [Use Pydantic's orm_mode - orm_mode=True](https://fastapi.tiangolo.com/tutorial/sql-databases/#use-pydantics-orm_mode)
- [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/)