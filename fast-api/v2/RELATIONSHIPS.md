# Section: Relationships

- [SQL Relationship Basics](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=28233s)
    - Why we need relationships
    - One to Many Relationship

- [Postgres Foreign Keys](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=28499s)
    - Creating & Setting up foreign key `manually` within Postgres & PGAdmin
        - Creating one more key: `user_id`
        - Creating key constraint/foreign key
    - CASCADE
    - Creating some records that relates to `users` and `posts`
    - Deleting foreign key `manually`
        
- [SQLAlchemy Foreign Keys](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=29240s)
    - Creating & Setting up foreign key using `SQLAlchemy`
    - Using SQLAlchemy to generate
        - All the tables
        - All the columns for each table
        - All the defferent properties
        - The foreign keys - Relations between tables
            - Keyword: `Defining Constraints and Indexes`
            - `owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)`
            - There is no actual owner ID column
                - [Reason](https://youtu.be/0sOvCWFmrtA?si=0-YGt06FFrInquE7&t=29426)
                - There's already a table named `posts`, then SQLAlchemy is not going to do anything
                - It means if we update any properties for a pre-existing table, it's not going to change that
                - We have to use a database migration tool like `alembic`
                - Currently, we just drop the `posts` table, then restart the application again.
    - Create a few entries
        - Creating some post-records with user
        - CASCADE testing: delete user.id = 11

- [Update Post Schema to include User](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=29620s)
    - Login
    - Get posts
        - schemas: `class Post(PostBase)`
    - Get post
        - schemas: `class Post(PostBase)`
    - Update a post
        - schemas: `class Post(PostBase)`

- [Assigning Owner id when creating new](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=29879s)
    - Create Posts
        - schemas: `class PostCreate(PostBase)`
        - route: `@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)`
            - `new_post = models.Post(owner_id=current_user.id, **post.dict())`

- [Delete and Update only your own](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=30061s)
    - Delete a post
        - adding permission to delete a post: `only author can delete his own`
        - `@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)`
    - Update a post
        - updating permission to update a post: `only author can update his own`
        - `@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)`

- [Only Retrieving Logged in User's](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=30468s)
    - Get Posts: `@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Post])`
    - Get post: `@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)`
        - add permission to read

- [Sqlalchemy Relationships](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=30817s)
    - When query post, we need to know more about who created it
    - models.py
        - Set up a relationship
        - It tell to SQLAlchemy to automatically fetch some piece of information based off of the relationship
        - We're referencing the acutal SQLAlchemy class
            - `owner = relationship("User")`
        - Then we need to update `schemas`
            - `class Post(PostBase)`: UserOut # return pydantic model

- [Query Parameters](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=31112s)
    - Example: https://www.yelp.com/search?`find_desc=&find_loc=San+Francisco%2C+CA`
    - A query parameter is an optional key-value pair that appears to the right of the `question` mark
    - These query parameters allow us to kind of `filter` the results of a request
    - A lot of other operations that are necessary in an API, things like `pagination`, those are all going to be done with query parameters
    - Practice
        - `routers/post.py`
            - We want to let the user be able to kind of filter down on the post that they want to see
            - Pagination: `@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Post])`
                - `limit: int = 10`
                - `skip: int = 10`
                    - `posts = query_statement.limit(limit=limit).offset(offset=skip).all()`
            - Search: `@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Post])`
        - How to use `spaces` in your search query: `%20`

- [Cleanup our main.py file](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=31846s)
    - Moving script help connecting to DB driver to `database.py` file
        - `psycopg2.connect`

- [Env Variables](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=32033s)
    - Migrate environment variables into our application
    - [Window env](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=32033s)
        - `example.py`
    - [Mac env](https://youtu.be/0sOvCWFmrtA?si=z2pSS64jQi8UcTOM&t=32573)
        - export MY_DB_URL="localhost:5432"
        - prinenv
        - echo $MY_DB_URL
        - we can use pydantic to perform all of that validation for our environment variables for application to run.
            - `main.py`
            - providing a list of all of the environment variables that we need set as properties on the class itself
            - `app/config.py` file
                - tell `Pydantic` to actually import it from our `.env` file
                - `class Config`
            - `env` file
        - [BaseSettings has moved to pydantic-settings](https://docs.pydantic.dev/2.5/migration/#basesettings-has-moved-to-pydantic-settings)
        - update using .env
            - `database.py`
            - `oauth2.py`

# References
- [Defining Constraints and Indexes](https://docs.sqlalchemy.org/en/20/core/constraints.html#defining-constraints-and-indexes)
- [Handling Multiple Join Paths](https://docs.sqlalchemy.org/en/20/orm/join_conditions.html)
- [Relationship Configuration](https://docs.sqlalchemy.org/en/14/orm/relationships.html)
- [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
- [Query Parameters and String Validations](https://fastapi.tiangolo.com/tutorial/query-params-str-validations/)
- [SQLAlchemy Limit](https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#sqlalchemy.orm.Query.limit)
- [SQLAlchemy Offset](https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#sqlalchemy.orm.Query.offset)
- [BaseSettings has moved to pydantic-settings](https://docs.pydantic.dev/2.5/migration/#basesettings-has-moved-to-pydantic-settings)