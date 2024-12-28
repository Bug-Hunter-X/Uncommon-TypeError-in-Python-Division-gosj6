def function_with_uncommon_error_solution(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

# This will raise a TypeError
result1 = function_with_uncommon_error_solution(10, "hello")
print(result1)  # Output: Error: Unsupported operand type(s) for /  None

# This will raise a ZeroDivisionError
result2 = function_with_uncommon_error_solution(10, 0)
print(result2) # Output: Error: Division by zero None

# This will work fine
result3 = function_with_uncommon_error_solution(10, 2)
print(result3) # Output: 5.0