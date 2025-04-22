while True:
    user_input = input("Please enter a number: ")

    try:
        number: float = float(user_input)
        print(f'You entered: {number}')
    except ValueError:
        print('You entered an invalid number.')
    except Exception as e:
        # it provides for dev to specify error
        print('Program encountered a new exception')
        print(f'Type: {type(e)}')
        print(f'Error: {e}')

