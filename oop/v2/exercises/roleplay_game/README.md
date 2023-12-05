# Roleplaying Game Classes

## Let's pretend we're building an RPG (roleplaying game) in Python. Side note: check out these games actually built in Python!

1. Define a base class "Character" that has the following properties:

    name  - String
    hp  - an Integer value representing health (aka hitpoints)
    level  - an integer value representing experience level

2. Define a subclass "NPC" (which stands for Non-Player Character) that inherits from Character , and has an additional instance method called speak  which prints the speech that character would say when a player interacts with them. 

Example:

    villager = NPC("Bob", 100, 12)
    villager.name  # Bob
    villager.hp  # 100
    villager.level  # 12
    villager.speak()  # "I heard there were monsters running around last night!".