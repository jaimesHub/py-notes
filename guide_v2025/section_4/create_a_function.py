def greet(): # define function
    print('Hello')
    print('-----')

greet() # using function
greet()
greet()

from datetime import datetime

def show_time():
    now: datetime = datetime.now()
    print(f'Time: {now:%H:%M:%S}')

show_time()

import time
time.sleep(2)
show_time()