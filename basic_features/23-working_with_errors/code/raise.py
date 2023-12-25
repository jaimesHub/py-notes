# print("hello")
# "lol"[9] # IndexError
# print("goodbye")

def get_user_name():
    inp = input('please enter your name: ')
    if not inp.isalpha():
        raise ValueError('alpha chars only')
    return inp

def register_user():
    user = get_user_name()
    # Database.save(user) # Database does not exist