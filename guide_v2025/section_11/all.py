wifi_enabled: bool = True
has_electricity: bool = False
has_subscription: bool = True

requirements: list[bool] = [wifi_enabled, has_electricity, has_subscription]

# if wifi_enabled and has_subscription and has_electricity:
#     print('Connected to internet!')

if all(requirements):
    print('Connected to internet!')

people_voted: list[int] = [1, 1, 1, 0, 1, 0, 1, 1, 1, 0]

if not all(people_voted):
    print('Some people did not vote...')
else:
    print('Everyone has voted!')