# Python & Raw SQL

- [Setup App Database](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=14028s)

- [Connecting to database w/ Python](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=14301s)

    - Working with Postgres
        - [Psycopg 3 driver](https://www.psycopg.org/psycopg3/docs/)
            - [Installing](https://www.psycopg.org/psycopg3/docs/basic/install.html)
            - [Setup our connection]()
            - [Basic module usage](https://www.psycopg.org/psycopg3/docs/basic/usage.html)

        - [[x] Psycopg 2 driver](https://www.psycopg.org/docs/)
            - [Installing](https://www.psycopg.org/docs/install.html)

            - [Setup our connection](https://www.psycopg.org/docs/module.html)
                - [Solution issue `psql-fatal-role-postgres-does-not-exist`](https://stackoverflow.com/questions/15301826/psql-fatal-role-postgres-does-not-exist)
                - [Connecting w/ Postgres](https://www.psycopg.org/docs/module.html)
                    - keywords: `cursor_factory=RealDictCursor`
                        - [psycopg2.connect()](https://www.psycopg.org/docs/module.html#psycopg2.connect)
                        - [conn.cursor()](https://www.psycopg.org/docs/cursor.html#cursor)
                        - [cursor_factory=RealDictCursor](https://www.psycopg.org/docs/extras.html#psycopg2.extras.RealDictCursor)
                        
                    - setting up retry connection if it fails: `time.sleep(2)`

            - [Basic module usage](https://www.psycopg.org/docs/usage.html)
                - The function [connect()](https://www.psycopg.org/docs/module.html#psycopg2.connect) creates a new database session and returns a new [connection](https://www.psycopg.org/docs/connection.html#connection) instance.

                - The class [connection](https://www.psycopg.org/docs/connection.html#connection) encapsulates a database session. It allows to:
                    - create new [cursor](https://www.psycopg.org/docs/cursor.html#cursor) instances using the [cursor()](https://www.psycopg.org/docs/connection.html#connection.cursor) method to execute database commands and queries,
                    - terminate transactions using the methods [commit()](https://www.psycopg.org/docs/connection.html#connection.commit) or [rollback()](https://www.psycopg.org/docs/connection.html#connection.rollback).

                - The class [cursor](https://www.psycopg.org/docs/cursor.html#cursor) allows interaction with the database:
                    - send commands to the database using methods such as [execute()](https://www.psycopg.org/docs/cursor.html#cursor.execute) and [executemany()](https://www.psycopg.org/docs/cursor.html#cursor.executemany),
                    - retrieve data from the database by [iteration](https://www.psycopg.org/docs/cursor.html#cursor-iterable) or using methods such as [fetchone()](https://www.psycopg.org/docs/cursor.html#cursor.fetchone), [fetchmany()](https://www.psycopg.org/docs/cursor.html#cursor.fetchmany), [fetchall()](https://www.psycopg.org/docs/cursor.html#cursor.fetchall).
    
    - Adaptation of Python values to SQL types
        - [Adaptation of Python values to SQL types](https://www.psycopg.org/docs/usage.html#adaptation-of-python-values-to-sql-types)

- [Database CRUD](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=14880s)
    - Retrieving Posts: `@app.get("/posts")`
    - Creating Post: `@app.post("/posts", status_code=status.HTTP_201_CREATED)`
    - Get One Post: `@app.get("/posts/{id}")`
    - Delete Post: `@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)`
    - Update Post: `@app.put("/posts/{id}")`

# References

- [Psycopg 2 driver](https://www.psycopg.org/docs/)
- [Psycopg 3 driver](https://www.psycopg.org/psycopg3/docs/)