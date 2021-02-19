# Exercise 18 (Exceptions)

An exception is an error. These errors are generated when the code is executed. Sometimes, these are also known as Runtime errors because we only get these errors when the code is executed.

## Some types of exceptions

There are a lot of [Exceptions][py-exceptions] and we'd just list some of the most seen ones.

- ZeroDivisionError
- AttributeError
- EOFError
- ImportError
- IndexError
- KeyError
- NameError
- RuntimeError
- ValueError
- TypeError

## Handling exceptions

It is important to handle exception in our code as it will prevent the abrupt halting of the program when running. We can handle these errors with `try` and `except` clauses.

### Try and catch structure

```Python
try:
    # code to check
except (exceptions to handle):
    # message
```

### Example 1

```Python
# catch ZeroDivisionError
# error generated when dividing by zero
# we shall perform some simple division
# where by we take 2 int inputs from the user
try:
    numerator = int(input('Enter the numerator: '))
    denominator = int(input('Enter the denominator: '))

    result = numerator / denominator

    print(f"The result is {result}")
except ZeroDivisionError as z:
    print(f'error: {z}')

# with this approach, our program would not crash badly.

# we can also catch this in another hack
numerator = int(input('Enter the numerator: '))
denominator = int(input('Enter the denominator: '))

if denominator == 0:
    print(f'ZeroDivisionError: can not divide by zero')
else:
    result = numerator / denominator
    print(f"The result is {result}")
```

In the above example, it will be best if try and except is used instead.

### Example 2

Let's try to catch any kind of exception using the `Exception` class.

```Python
# Lets catch an Exception without being specific

try:
    numerator = input('Enter the numerator: ')
    denominator = int(input('Enter the denominator: '))

    result = numerator / denominator + rate
    # note that the name, rate, is not defined

    print(f"The result is {result}")
except Exception as z:
    print(f'error: {z}')
```

### Example 3

Let's catch multiple exceptions - as a tuple

```Python
try:
    numerator = int(input('Enter the numerator: '))
    denominator = int(input('Enter the denominator: '))

    result = numerator / denominator

    print(f"The result is {result}")
except (ZeroDivisionError, NameError, ValueError) as e:
    print(f'error: {e}')
```

## Raising exceptions

We can force raise an exception using the `raise` keyword.

```Python
# let raise an exception
# so we take an input from the user and we expect an even number else,
#  we raise the exception

try:
    user_input = int(input('Enter an even number: '))
    if user_input % 2 != 0:
        raise ValueError('Even number expected.')
        # if we don't know what kind of exception to raise
        # just raise Exception
    else:
        print(f"Cool, you entered, {user_input}")
except Exception as e:
    print(f"error: {e}")
```

## Practicals

Fix this code base on the error message generated:

```Python
try:
    numerator = input('Enter the numerator: ')
    denominator = int(input('Enter the denominator: '))

    result = numerator / denominator + rate

    print(f"The result is {result}")
except Exception as z:
    print(f'error: {z}')
```

## Summary

- Exceptions are error we get at runtime
- `Execption` class catches all exceptions in general
- Use `try` and `catch` to handle exceptions
- Raise exception using, `raise Exception_type(message)`

#

[py-exceptions]: https://docs.python.org/3/library/exceptions.html
