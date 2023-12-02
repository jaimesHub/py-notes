#  The purpose of this code is to demonstrate how nested functions work in Python.
def print_message(message):
    "Enclosing Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()
    
print_message("Some random message")