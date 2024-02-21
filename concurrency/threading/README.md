# Section: Threading

## Threading in Python
- [main.py](./threading_in_python/main.py)
- Example of sequential program
    - calculate_sum_squares(n)
    - sleep_a_little(seconds)
- Adding some concurrency: Using `threading`
    - create `thread` object
    - init it: `t.start()`
    - checking which thread is running?
        - nothing happends util that thread finishes: `t.join()`
        - what would happen when we call `t.join()` right after `t.start()`?
    - argument: daemon=True

## Creating a Threading Class
- creating `workers` directory