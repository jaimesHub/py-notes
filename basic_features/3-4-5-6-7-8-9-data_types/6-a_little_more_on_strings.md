# A Litlle More On Strings

- String `slices`: msg[start:stop]
- Examples
    ```
    In [62]: animal = "catdog"

    In [63]: animal
    Out[63]: 'catdog'

    In [64]: animal[2:4]
    Out[64]: 'td'

    In [65]: animal[3:5]
    Out[65]: 'do'

    In [66]: animal[3:6]
    Out[66]: 'dog'

    In [67]: animal[3:99]
    Out[67]: 'dog'

    In [68]: animal
    Out[68]: 'catdog'

    In [69]: animal[3:]
    Out[69]: 'dog'

    In [70]: animal[0:4]
    Out[70]: 'catd'

    In [71]: animal[0:3]
    Out[71]: 'cat'

    In [72]: animal[:3]
    Out[72]: 'cat'
    ```
- Examples
    ```
    In [74]: pn1 = "(310) 448 8712"

    In [75]: pn2 = "(212) 696 9912"

    In [76]: pn1[1:4]
    Out[76]: '310'

    In [77]: pn2[1:4]
    Out[77]: '212'

    In [78]: sns = "#2523598274"

    In [79]: sns[1:]
    Out[79]: '2523598274'
    ```
- Slices with a Step: `msg[start: stop: step]`
- Examples
    ```
    In [81]: msg = 'ha!ha!ha!ha!'

    In [82]: msg[0:10]
    Out[82]: 'ha!ha!ha!h'

    In [83]: msg[0:10:3]
    Out[83]: 'hhhh'

    In [84]: msg[0:10:2]
    Out[84]: 'h!ah!'

    In [85]: msg[0:10:5]
    Out[85]: 'h!'
    ```
- Revisiting `Print()`
- Escape Characters
    - Newline: `\n` -> a new line character that will be displayed when we `print` this string
    ```
        In [87]: "hello \n world"
        Out[87]: 'hello \n world'

        In [88]: print("hello \n world")
        hello 
        world

        In [89]: phrase = "hello\nworld"

        In [90]: print(phrase)
        hello
        world
    ```
    - Tab: `\t`
    ```
    In [91]: print("hello\tworld")
    hello	world
    ```
    - Double: `\"`
    ```
        In [92]: "she said \"lol\""
        Out[92]: 'she said "lol"'

        In [93]: 'she said "lol"'
        Out[93]: 'she said "lol"'
    ```
    - Single Quote: `\'`
    - Backslash: `\\`
    ```
    In [94]: print("\")
    Cell In[94], line 1
        print("\")
            ^
    SyntaxError: unterminated string literal (detected at line 1)

    In [95]: print("\\")
    \
    ```
- Triple Quoted Strings
    ```
    In [97]: """hello"""
    Out[97]: 'hello'

    In [98]: '''
        ...: hello
        ...: world
        ...:     python is a new language
        ...:     it's greate to learn it now
        ...:     "python" is a snake!!!!
        ...: '''
    Out[98]: '\nhello\nworld\n    python is a new language\n    it\'s greate to learn it now\n    "python" is a snake!!!!\n'

    In [99]: print('''
        ...: hello
        ...: world
        ...:     python is a new language
        ...:     it's greate to learn it now
        ...:     "python" is a snake!!!!
        ...: ''')

    hello
    world
        python is a new language
        it's greate to learn it now
        "python" is a snake!!!!


    In [100]: address = '''
        ...: Chicken Little
        ...: 123 Chicken wing lane
        ...: Denver Colorado 21736
        ...: '''

    In [101]: address
    Out[101]: '\nChicken Little\n123 Chicken wing lane\nDenver Colorado 21736\n'

    In [102]: print(address)

    Chicken Little
    123 Chicken wing lane
    Denver Colorado 21736
    ```
- Assignment
    - Check `String_Basics_Starter.py`
