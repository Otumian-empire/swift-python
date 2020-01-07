# Exercise 18 (Execptions)
An exception is an error one gets when the code is esecuted. Sometimes, this is also know as runtime error.

## Some types of exceptions

There are a lot of Exceptions and We'd just list some of the mostly seen ones.

* ZeroDivisionError
* AttributeError
* EOFError
* ImportError
* IndexError
* KeyError
* NameError
* RuntimeError
* ValueError
* TypeError

## Handling exceptions

We can handle these errors with a `try` and `except` clauses.

### Try and catch structure

``` python
try:
    # code to check
except (exceptions to handle):
    # message
```

### Example 1

``` python
# lets catch a ZeroDivisionError
# we shall perform some simple division
#  where by we take 2 int inputs from the user
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

### Example 2

Lets try to catch any kind of execption using the `Exception` .

``` python
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

Lets catch multiple exceptions - as a tuple

``` python
try:
    numerator = int(input('Enter the numerator: '))
    denominator = int(input('Enter the denominator: '))

    result = numerator / denominator

    print(f"The result is {result}")
except (ZeroDivisionError, NameError, ValueError) as e:
    print(f'error: {e}')
```

## Raising exceptions

We can raise our own exception using the `raise` keyword.

``` python
# let raise our own exception
# so we take an input from the user and we expect an even number else,
#  we raise the exception

try:
    user_input = int(input('Enter an even number: '))
    if user_input % 2 != 0:
        raise ValueError('Even number expected.')
        # if you don't know what kind of exception to raise
        # just raise Exception
    else:
        print(f"Cool, you entered, {user_input}")
except Exception as e:
    print(f"error: {e}")

```

## Practicals

Fix this code:

``` python
try:
    numerator = input('Enter the numerator: ')
    denominator = int(input('Enter the denominator: '))

    result = numerator / denominator + rate

    print(f"The result is {result}")
except Exception as z:
    print(f'error: {z}')
```

## Summary

* Exceptions are error we get at runtime
* BaseException is the Base class of all the exceptions
* Use `try` and `catch` to handle exceptions
* Raise exception using, `raise Exception_type(message` )

