# Exercise 18 (Exceptions)

An exception is an error. These errors are generated when the code is executed. Sometimes, these are also known as Runtime errors because we only get these errors when the code is executed.

## Some types of exceptions and how they occur

There are a lot of [Exceptions][py-exceptions] and we'd just list some of the most seen ones.

### ZeroDivisionError

This error occurs when a number (integer and float) is divided by zero.

#### Sample code

```python
print("First line")  # this will be printed
print(1.0 % 0)       # there will be an error (halts the program execution)
print("Third line")  # this will not be printed

# the output
# First line
# Traceback (most recent call last):
#   File "s.py", line 2, in <module>
#     print(1.0%0)         # there will be an error (halts the program execution)
# ZeroDivisionError: float modulo

```

### IndexError

This error occurs when a sequence is out of range. When we try to access an index that does not exist.

#### Sample code

```python
even_nums = [2, 4, 6, 8]

# there is no 4th indexed element
print(even_nums[4])

# output
# Traceback (most recent call last):
#   File "sample.py", line 3, in <module>
#     print(even_nums[4])
# IndexError: list index out of range

```

### ImportError

This error occurs when an imported module can not load or does not exist. We shall discuss more about modules later. Let's say we created a file called `sample.py` with the function, `def hi()` that just prints `hi` and then we used (imported) it in another file, `app.py`.

#### sample code

`sample.py`

```python
def hi():
    print("hi")

```

`app.py`

```python
from sample import hello

# output
# Traceback (most recent call last):
#   File "sample.py", line 5, in <module>
#     from sample import hello
# ImportError: cannot import name 'hello' from 'sample'

```

This will raise an `ImportError`. `hello` can not be loaded because it does not exist in `sample.py` as a function (Attribute).

### AttributeError

Consider the sample code for `ImportError`. We import `sample` as an object. Objects have attributes and if we try to access or call an attribute that does not exist, we shall get `AttributeError`.

#### Sample code

Here we import `sample.py` as an object.

```python
import sample

sample.hi()

sample.hello()


# hello  # hello from sample.hi()
# Traceback (most recent call last):
#   File "s.py", line 4, in <module>
#     sample.hello()
# AttributeError: module 'sample' has no attribute 'hello'

```

Consider a case, where we create a class (an object and we give it an attribute).

```python
class Sample:

    def __init__(self):
        self.attr = "Here you, an attribute"


obj = Sample()

print(obj.attr)
print(obj.b)

# output
# Here you, an attribute
# Traceback (most recent call last):
#   File "sample.py", line 10, in <module>
#     print(obj.b)
# AttributeError: 'Sample' object has no attribute 'b'

```

### NameError

This error occurs when we try to access an undefined variable or object.

#### Sample code

```python
print(x)
# Where was x defined


# output
# Traceback (most recent call last):
#   File "sample.py", line 1, in <module>
#     print(x)
# NameError: name 'x' is not defined

```

In the case of an object.

```python
s = Home()

# output
# Traceback (most recent call last):
#   File "sample.py", line 1, in <module>
#     s = Home()
# NameError: name 'Home' is not defined

```

### ValueError

This error mostly occurs when dealing with types, casting an inappropriate to another type. You can not cast a character (alphabetic or alphanumeric) string to an `int`.

#### Sample code

casting integer string to `int`. This is still a string but numeric.

```python
print(int("12"))  # 12

```

casting float string to `int`. This is still a string, not numeric or alphanumeric which made up of numbers and alphabets then an underscore.

```python
print(int("12.0"))

# output
# Traceback (most recent call last):
#   File "sample.py", line 1, in <module>
#     print(int("12.0"))
# ValueError: invalid literal for int() with base 10: '12.0'

```

### TypeError

This error occurs when certain operations such as addition, multiplication, etc are done on objects of different (inappropriate) types. Such as trying to add an `int` to an `str`.

#### Sample code

```python
print(4 + "John Doe")

# output
# Traceback (most recent call last):
#   File "sample.py", line 1, in <module>
#     print(4 + "John Doe")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

```

## Handling exceptions

It is important to handle exception in our code as it will prevent the abrupt halting of the program when running. We can handle these errors with `try` and `except` clauses.

### Try and catch structure

```Python
try:
    # code to check
except (exceptions to handle):
    # message
```

#### Example 1

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

#### Example 2

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

#### Example 3

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

We can forcefully raise an exception using the `raise` keyword.

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

Fix this code based on the error message generated. Fix the ambiguity of the operator precedence. Update the code to catch specific exceptions.

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
- The `Exception class catches all exceptions in general
- Use `try` and `catch` to handle exceptions
- Raise exception using, `raise Exception_type(message)`

#

[py-exceptions]: https://docs.python.org/3/library/exceptions.html
