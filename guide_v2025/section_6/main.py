# def main() -> None:
#     ...
#
# if __name__ == "__main__":
#     main()

# import connection # run script first
#
# connection.connect() # run script second
# # -> calling twice
#
# # Output
# # Connecting to internet...
# # Connected!
# # Connecting to internet...
# # Connected!

import connection # after adding if __name__ == '__main__': instead of running while importing

# connection.connect() # out one

if __name__ == '__main__':
    connection.connect()