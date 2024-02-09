"""This file for my experiment of setting up scratch project
"""

GREETING = "Hello world"
print(GREETING)

for i in range(1, 11):
    print(i)


def increment(input_number):
    """Increasing a number with 1"""
    data = {
        "a": 0,
        "b": [[1, 2], [3, 4]],
        "c": 5,
        "d": 1,
    }

    print(data)

    return input_number + 1


def decremnt(input_number):
    """Decreasing a number with 1"""
    return input_number - 1


def test_doc_string():
    """test_doc_string _summary_"""
