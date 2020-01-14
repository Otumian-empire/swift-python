# Exercise 22 (Unit Testing)

Unit testing is an important part of software engineering. We do unit testing to check the correctness of our program. Usally in most firms, unit tests are written before the code is written - this is known as the Test Driven Development. We shall write the tests after we write the code. We shall use the built-in `unittest` module. There are many testing concepts but we shall basically look at `TestCase` .

## Some testing methods

``` html
<table border="2">

    <colgroup>
        <col width="48%">
        <col width="34%">
        <col width="18%">
    </colgroup>
    <thead>
        <tr>
            <th>Method</th>
            <th>Checks that</th>
            <th>New in</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <code>
                    <span>assertEqual(a, </span>
                    <span>b)</span>
                </code>
            </td>
            <td>
                <code><span>a</span>
                    <span>==</span>
                    <span>b</span>
                </code>
            </td>
            <td>&nbsp; </td>
        </tr>
        <tr>
            <td>
                <code>
                    <span>assertNotEqual(a, </span>
                    <span>b)</span>
                </code>
            </td>
            <td>
                <code>
                    <span>a</span>
                    <span>!=</span>
                    <span>b</span>
                </code>
            </td>
            <td>&nbsp; </td>
        </tr>
        <tr class="row-even">
            <td>
                <code>
                    <span>assertTrue(x)</span>
                </code>
            </td>
            <td>
                <code>
                    <span>bool(x)</span>
                    <span>is</span>
                    <span>True</span></code>
            </td>
            <td>&nbsp; </td>
        </tr>
        <tr>
            <td><a href="assertFalse" title=".assertFalse"><code><span>assertFalse(x)</span></code>
            </td>
            <td><code><span>bool(x)</span> <span>is</span> <span>False</span></code>
            </td>
            <td>&nbsp; </td>
        </tr>
        <tr class="row-even">
            <td><a href="assertIs" title=".assertIs"><code><span>assertIs(a, </span> <span>b)</span></code>
            </td>
            <td><code><span>a</span> <span>is</span> <span>b</span></code>
            </td>
            <td>3.1</td>
        </tr>
        <tr>
            <td><a href="assertIsNot" title=".assertIsNot"><code><span>assertIsNot(a, </span> <span>b)</span></code>
            </td>
            <td><code><span>a</span> <span>is</span> <span>not</span> <span>b</span></code>
            </td>
            <td>3.1</td>
        </tr>
        <tr class="row-even">
            <td>
                <code>
                    <span>assertIsNone(x)</span>
                </code>
            </td>
            <td><code><span>x</span> <span>is</span> <span>None</span></code>
            </td>
            <td>3.1</td>
        </tr>
        <tr>
            <td><a href="assertIsNotNone" title=".assertIsNotNone"><code><span>assertIsNotNone(x)</span></code>
            </td>
            <td><code><span>x</span> <span>is</span> <span>not</span> <span>None</span></code>
            </td>
            <td>3.1</td>
        </tr>
        <tr>
            <td>
                <code>
                    <span>assertIn(a, </span> <span>b)</span>
                </code>
            </td>
            <td>
                <code>
                    <span>a</span>
                    <span>in</span>
                    <span>b</span></code>
            </td>
            <td>3.1</td>
        </tr>
        <tr>
            <td>
                <code>
                    <span>assertNotIn(a, </span>
                    <span>b)</span>
                </code>
            </td>
            <td>
                <code>
                    <span>a</span>
                    <span>not</span>
                    <span>in</span>
                    <span>b</span>
                </code>
            </td>
            <td>3.1</td>
        </tr>
        <tr>
            <td>
                <code>
                    <span>(a,</span>
                    <span>b)</span>
                </code>
            </td>
            <td><code><span>isinstance(a, </span> <span>b)</span></code>
            </td>
            <td>3.2</td>
        </tr>
        <tr>
            <td>
                <code>
                    <span>(a, </span>
                    <span>b)</span>
                </code>
            </td>
            <td>
                <code>
                    <span>not</span>
                    <span>isinstance(a, </span>
                    <span>b)</span>
                </code>
            </td>
            <td>3.2</td>
        </tr>
    </tbody>

</table>
```

## Example

Consider that we have a program that does some mathematical operations - addition, multiplication and division. We shall use the `assertEqual` and `assertIsNone` method to test if our methods actually are returning the same value as we expect.

``` python
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

``` python
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

## Practicals

Write a unit test - TestCases - for the programs you have written since `exercise 12` .

## Summary
* UnitTesting is very important in the world of software engineering
* It checks the correctness of our code
* to use pythons built-in unit testing package, import it, `import unittest`
* create a class, `ModuleTest` and subclass `unittest.TestCase`
* add `if __name__ == "__main__": unittest.main()` to actually run the test when called.