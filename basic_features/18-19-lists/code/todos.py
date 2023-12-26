print('''
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \\ / _` |/ _ \\/ __|
   | | (_) | (_| | (_) \\__ \\
   |_|\\___/ \\__,_|\\___/|___/
''')

print("*************************************")

current_tasks = []
finished_tasks = []

while True:
    command = input("Enter a command. Type 'h' for help:\n > ")
    
    if command == "q":
        print(f"Today you completed {len(finished_tasks)} todos")
        if len(finished_tasks) > 0:
            for task in finished_tasks:
                print(f"* {task}")
        break

    if command == "h":
        print('''
        TODO LIST HELP\nType 'q' to quit\nTo add a todo to the list, type it and hit enter\nTo complete a todo enter its number
        ''')
        continue

    if command.isnumeric():
        done_task = current_tasks.pop(int(command) - 1)
        finished_tasks.append(done_task)
    else:
        current_tasks.append(command)

    for idx in range(len(current_tasks)):
        print(f"{idx + 1}) {current_tasks[idx]}")
    print("*************************************")


