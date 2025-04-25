class Connections:
    def __init__(self, connect_type: str) -> None:
        self.connect_type = connect_type

    def connect(self) -> None:
        print(f'Connecting to {self.connect_type}')


def connect(connect_type: str) -> None:
    print('Connecting to ' + connect_type)

# what difference ???