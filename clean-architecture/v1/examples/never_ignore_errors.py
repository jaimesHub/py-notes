def division(dividend, divisor):
    try:
        quotient = dividend / divisor
    except ZeroDivisionError:
        pass
    return quotient