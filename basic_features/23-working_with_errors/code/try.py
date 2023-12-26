try: 
    num = int(input("enter a number: "))
except ValueError:
    print("except block running!")
except EOFError:
    print("You didn't enter anything!")
print(f"you entered {num}")