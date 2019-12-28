# exercise 13 (Some built-in functions)

> We really recommend you check out the [python doc](https://python.org), see the library reference and click on the built-in functions.

In the previous chapter we looked into function and we created a couple of our own. Python comes packaged with some function and these functions are known the built-in functions.

## Some built-in functions
1. abs(x)
1. divmod(a, b)
1. float(x)
1. int(x)
1. input(prompt)
1. len(x)
1. list(x)
1. max(x)
1. min(x)
1. pow(a, b)
1. print(a)
1. range(start, end, step)
1. reversed(x)
1. round(x)
1. sorted(x)
1. str(x)
1. sum(x)
1. type(x)
1. chr(i) and ord(s)

## Examples
```python
# abs - returns an absolute value of a number
print(abs(2.34), abs(-23.4))

# round - take a number x, rounds it to y decimal places
print(round(23.23567, 2))

# divmod - Take two args and return their quotient and remainder
print(divmod(23, 6))

# pow - take 2 args and returns x raised to the power y
print(pow(2, 3))

# max, min, sum, sorted, reversed
# the above functions are used on iterables
my_list = [7, 2, 4, 5, 1]

print(f"The largest number is: {max(my_list)}")
print(f"The smallest number is: {min(my_list)}")

print(f"The sum of the numbers is: {sum(my_list)}")

print(f"sorted list: {sorted(my_list)}")

print(f"reversed list: {reversed(my_list)}")

# these function does not alter the object

# chr and ord
# chr - returns a character when a number is passed as arg
print(chr(65))  # this are unicode related

# ord does the opposite of chr
print(ord('A'))

# float, int, str, list, dict, set
# these converts objects to their types
# type returns the ( data) type of an object
# len, range
# we have seen these two before, for the size and also looping

# input, print
# we have also seen them before
```
## Practicals
* Implement a function known as `all(iterable)`. This function returns `True` if all the elements of the `iterable` is `True` or the `iterable` is empty, else `False`.
* Implement a function known as `any(iterable)`. This function returns `True` if all the elements of the `iterable` is `True`. If the iterable is empty, return False.
* Implement the `abs(x)` function where `x`, is a number.
* Implement a function that returns the minimum and maximum numbers in given list. Don't use the built-in function `min` and `max`.

## Summary
* Python came with some functions know as the built-in functions
* These functions makes working in python much more easier and flexible without you having to implement your own version of that function.
* Built-in functions does not change the object