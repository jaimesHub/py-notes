def division(dividend, divisor):
    try:
        quotient = dividend / divisor
    except ZeroDivisionError:
        print("An error occurred")
    return quotient