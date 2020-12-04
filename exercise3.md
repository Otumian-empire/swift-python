# Exercise 3 ( More on data types and comments)

There are other data types other than those mentioned earlier in `Exercise 2 (Data Types)`. We shall discuss the `boolean` data type.

This data type can only be `True` or `False`. Boolean values are generated when values are compared or when there is a condition. `Eg 1 < 2 is True, 1 > 2 is False` .

## Examples

```python
is_online = True
is_swift = True
is_human = False
```

### Note

Boolean values are case sensitive. Upper-case `T` for `True` and `F` for `False` , in python.

## Comment

A comment is a piece of text that mostly should tell why or what we are trying to achieve. The `#` symbol, placed ( inserted) at the beginning of the line, comments the line ( the line is ignored by the interpreter).

## Examples

```python
# Hello world program
# Display Hello world for the user to see
# Using the print function
print("Hello world")
```

The first three lines starting with `#` are comments. A comment is ignored during execution. You can also comment out some lines during debugging.

### Note

Whatever that comes after the `#` would be ignored.
`print('hello world') # greetings` , _greetings_ would be ignored.

## Practicals

1. In `Exercise 2 (Data Types)`, add comments to your solutions to give the why/what the line is doing or meant to do ( remember that not all lines need a comment if the code is descriptive itself).

1. - How many comments are there in the code below?
   - Which line numbers, would be displayed and why?

   ```python
   1 # John Doe - profile
   2 print("My name is John Doe") # yes that's my name
   3 print("He washes my hair")
   4 # i like to dance in the rain print("This costs $25.00")
   5 my_name = "Danny Doe Dan"
   6
   7
   ```

## Summary

- A boolean value is `True` or `False`.
- These values are generated during the comparison of two or more values.
- A comment is supposed to explain, "the" what or why in the code ( line)
- We can also use it to state how we want to reach our solution
- Use `#` to create a comment
