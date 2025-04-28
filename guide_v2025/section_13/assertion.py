def start_program(db: dict[int, str]) -> None:
    assert db, 'Database is empty' # useful during development process

    print('Loaded: ', db)
    print('Program started successfully!')

def main() -> None:
    # db1: dict[int, str] = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
    db1: dict[int, str] = {}
    start_program(db1)

if __name__ == '__main__':
    var: int = -5
    assert var > 0, f'{var} is not more than 0'
    main()