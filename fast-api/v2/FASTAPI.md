# Introduction to FastAPI

- [Starting FastAPI](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=2181s)
    - Create: `main.py`
    - Run application: `uvicorn main:app --reload`
    - keyword: `async`, `path operation`, `http methods`
    - decorator: `@app.get()`
        - just understanding when you apply a decorator to a function, it's going to perform a little magic to this function
        - for example: try to remove the decorator `@app.get("/")`
        - these decorators help functions act like APIs

- [Path Operations](https://youtu.be/0sOvCWFmrtA?si=a9aR-CmOSWN8hj8G&t=2856)
    - Recap: How `path operations work`
    - Create a new path operation
    - The order does matter

- [Introduction to Postman](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=3202s)

- [HTTP Requests](https://youtu.be/0sOvCWFmrtA?si=pj8ieK5F0wlSS-d3&t=3464)
    - HTTP GET vs POST Requests
    - how to send data in the body: `@app.post()`
        - how we extract the data that we sent in the `body`? How do we retrieve that body data?
            - `from fastapi.params import Body`
            - in `path operation function`: payload: dict = Body(...)

- [Schema Validation with Pydantic](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=4049s)
    - Why We need `Schema`?
        - It's a pain to get all the values from the body
        - The client can send whatever data they want
        - The data isn't getting validated
        - We ultimately want to force the client to send data in a schema that we expect
    - Using `Pydantic`
        - [Standard Library Types](https://docs.pydantic.dev/latest/api/standard_library_types/)
        - Check performing all of validations
            - field required
        - optional fields
            - way 1: `published: bool = True`
            - way 2: `from typing import Optional`
        - the `payload` stores it as a `pedantic model`
            - each pedantic model has a method called `dict` or `model_dump`

- [CRUD Operations](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=4965s)
    - POST, GET, PUT/PATCH, DELETE
    - best practice and naming for an API

- [Storing posts in Array](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=5384s)
    - using local memory
    - `@app.get("/posts")`

- [Creating posts](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=5646s)
    - `@app.post("/posts")`
    - how to create a collection of apis in Postman

- [Retrieve One Post](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=5987s)
    - keyword: `path parameter`
    - `@app.get("/posts/{id}")`
    - int(id)
    - validation: random `id` parameter 

- [Path order Matters](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=6490s)
    - how routes work
    - how order matters
    - be careful while structuring your API

- [HTTP Response Status Codes](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=6766s)
    - keyword: `http status codes`
    - manipulating the response
        - way 1:
            - pass it (response: Response) as a parameter into our path operation function
            - `from fastapi import Response`
            - `from fastapi import status`
        - way 2:
            - using `raise`
            - `from fastapi import FastAPI, Response, status, HTTPException`
    - change response status 201 for post.create_posts

- [Deleting Posts](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=7309s)
    - You should do that
        - `return Response(status_code=status.HTTP_204_NO_CONTENT)`

- [Updating Posts](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=7831s)
    - using the `PUT` method
    - create `UpdatePost` class

- [Automatic Documentation](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=8282s)
    - [Swagger UI](http://127.0.0.1:8000/docs)
    - [Redoc](http://127.0.0.1:8000/redoc)

- [Python packages](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=8494s)
    - concept of `packages`
    - `app` folder
        - dummy file: `__init__.py`
        - restart server: `uvicorn app.main:app --reload`
            - It means `uvicorn` finds `app` folder, then it references to `main.py` file
            - After that, it finds `app`(app = FastAPI()) instance in `main.py`

# References
- [Standard Library Types](https://docs.pydantic.dev/latest/api/standard_library_types/)