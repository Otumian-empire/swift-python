# Exercise 22 (Unit Testing)

Open the python console (REPL) on the command line (terminal).

```
Python 3.8.5 (default, Jan 27 2021, 15:41:15)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

That is how mine looks like. On windows, if you can see something like this, then you have to go back to `exercise 0 (Set up)` and add the python to the environmental variable path.

## assert

`assert` keyword raises an error, an `AssertionError` when the assertion fails. Consider the snippet below on how to use `assert`.

```Python
assert 1 == 1

```

The above assertion passes because `1 == 1` is True. There won't be an error since the assertion passed.

> Try out for a false assertion.

```sh
Python 3.8.5 (default, Jan 27 2021, 15:41:15)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> assert 1 == 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>>

```

If you want to use `assert` in our code, we would have to `try and except` it - we have to catch the error raised. We discussed `try and except` in `exercise 18 (Exceptions)`. Consider the code below where we catch the raised exception.

```Python
try:
    assert 1 == 2
    print("Hoo, we are safe now")

except:
    print("Haa, we are not safe, man. The assertion failed!!")

# output
# Haa, we are not safe, man. The assertion failed!!

```

Have you seen a problem that we shall face when we work on huge or complicated projects? We should use a Unit testing module. Python comes with a unit testing module, `unittest`.

## unittest module

Testing is an important part of software engineering. We do unit testing to check the correctness of our program - the individual components (functions). Usually, in most firms, unit tests are written before the code is written - this is known as Test-Driven Development. We shall write the tests after we write the code. We shall use the built-in `unittest` module. There are many testing concepts but we shall look at `TestCase`.

## Some testing methods

| Method                 |          Checks that |
| ---------------------- | -------------------: |
| `assertEqual(a, b)`    |             `a == b` |
| `assertNotEqual(a, b)` |             `a != b` |
| `assertTrue(x)`        |    `bool(x) is True` |
| `assertFalse(x)`       |   `bool(x) is False` |
| `assertIs(a, b)`       |             `a is b` |
| `assertNotIs(a, b)`    |         `a is not b` |
| `assertIsNone(x)`      |          `x is None` |
| `assertIsNotNone(x)`   |      `x is not None` |
| `assertIn(a, b)`       |             `a in b` |
| `assertNotIn(a, b)`    |         `a not in b` |
| `isinstance(a, b)`     | `type(a) == type(b)` |
| `isNotinstance(a, b)`  | `type(a) != type(b)` |

## Example 1

Let's look at a basic example of a unit test. Our testing will be solely done on the individual functions that we have. We shall write a unit test to check if a function returns `1`.

```Python
# test_one.py
import unittest


# extend the unittest.TestCase
class TestOne(unittest.TestCase):

    def test_int_1_is_int_1(self):
        self.assertEqual(1, 1)

    def test_int_1_is_float_1_pt_0(self):
        self.assertEqual(1, 1.0)

    def test_int_1_is_str_1(self):
        self.assertEqual(1, '1')


if __name__ == "__main__":
    unittest.main()

```

The method names start with `test`. This indicates it is a test. Now to run the test, `python3 test_one.py` will work as well as `python3 -m unittest test_one.py`. There are instances where the latter is better. Where should the latter be used?

## Example 2

Consider that we have a program that does some mathematical operations - addition, multiplication and division. We shall use the `assertEqual` and `assertIsNone` method to test if our methods are returning the same value as we expect.

```Python
# mathsy.py
class Mathsy:
    def __init__(self, operator, first_operand, second_operand):
        self.operator = operator
        self.first_operand = first_operand
        self.second_operand = second_operand

    def add(self):
        return self.first_operand + self.second_operand

    def mult(self):
        return self.first_operand * self.second_operand

    def div(self):
        if self.second_operand == 0:
            return None
        else:
            return self.first_operand / self.second_operand

    def evaluate(self):
        if self.operator == '+':
            return self.add()
        elif self.operator == '*':
            return self.mult()
        elif self.operator == '/':
            return self.div()
        else:
            raise Execption(f"{self.operator} not known")

```

Now the test.

```Python
# test.py
import unittest
from mathsy import Mathsy


# extend the unittest.TestCase
class MathsyTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Mathsy('+', 2, 4).evaluate(), 6)
        self.assertEqual(Mathsy('+', 1000, 4).evaluate(), 1004)

    def test_mult(self):
        self.assertEqual(Mathsy('*', 2, 4).evaluate(), 8)
        self.assertEqual(Mathsy('*', 1000, 4).evaluate(), 4000)

    def test_div(self):
        self.assertEqual(Mathsy('/', 2, 4).evaluate(), 0.5)
        self.assertEqual(Mathsy('/', 1000, 4).evaluate(), 250)
        self.assertEqual(Mathsy('/', 0, 4).evaluate(), 0)
        self.assertEqual(Mathsy('/', 4, 0).evaluate(), None)

        # the expected value is None - so we check if it actually does return the None
        self.assertIsNone(Mathsy('/', 4, 0).evaluate())


if __name__ == "__main__":
    unittest.main()

```

Check [this][test] out about testing.

## Practicals

Complete the program below. This is an implementation of a function that returns the factorial of a given integer value.

```Python
# practical.py
import unittest


def factorial(n: int) -> int:
    pass


class TestFactorial(unittest.TestCase):

    def test_zero_factorial_is_one(self):
        pass

    def test_one_factorial_is_one(self):
        pass

    def test_five_factorial_is_120(self):
        pass


if __name__ == "__main__":
    unittest.main()

```

## Summary

- UnitTesting is very important in the world of software engineering
- It checks the correctness of our code
- to use pythons built-in unit testing package, import it, `import unittest`
- create a class, `ModuleTest` and subclass `unittest.TestCase`
- add `if __name__ == "__main__": unittest.main()` to actually run the test when called.

#

[test]: https://github.com/Otumian-empire/sicp-python
