# exercise 9 (Logical and relational operators)
We advice you skim through exercise 3. How are boolean values generated? Logical operators with the use of Relation Operators generate Boolean Values.


## Relational Operators
Relational Operators, a binary operators just like the Arithmatic Operators. These are used for comparison. `Eg: <, >, <=, >=, ==, !=`. Thus are sometimes referred to as Comparison Operators.

### Example
```python
# let a and b be two non-zero integers of value 5 and 7 repectively
a = 5
b = 7

# Pay much attension to the Truth values generated

# greater than
print(a > b)
print(b > a) 

# less than
print(a < b)
print(b < a) 

# greater than or equal to
print(a >= b)
print(b >= a) 

# greater than or equal to
print(a <= b)
print(b <= a) 

# equal to
print(a == b)
# Not the double equal to. Unlike the assignment operator, which is just a character.

# not equal to
print(a != b)
# `!`, means `not`
```


## Logical Operators
Logical operators, combine two or more expressions to generate a boolean value. `Eg: and, or, not`. This combines more relational expressions to generate a truth value.

### Example
```python
# let a and b be two non-zero integers of value 5 and 7 repectively
a = 5
b = 7

# and
print(a <= 10 and b >= 10)

# or
print(a <= 10 or b >= 10)

# not
print(not a <= 10)
print(not b >= 10)


# the truth tables
# let t be True and f be False

# AND table
# for an 'AND' table, the truth value becomes true on when both components are truth.
#  a    |    b    |    a and b
# ---------------------------------
#  t    |    t    |       t
#  t    |    f    |       f
#  f    |    t    |       f
#  f    |    f    |       f

print((a <= 10) and (b >= 10))

# OR table
# for an 'OR' table, the truth value becomes true on when either components are truth,
# or we can say, the truth value becomes false only when both components are false.
#  a    |    b    |    a or b
# ---------------------------------
#  t    |    t    |       t
#  t    |    f    |       t
#  f    |    t    |       t
#  f    |    f    |       f

print((a <= 10) or (b >= 10))

# NOT table
# for a 'NOT' table, the resulting truth value is negated.
# thus if the value is True, not True = False and when False, not False = True
#   b    |   not b
# -------------------
#   t    |     f
#   f    |     t

```

### Note
* Any value that is None (null), empty, zero, etc is valued to False otherwise True.
* So all empty structures are evaluated to False by python.
* `not` is uninary, thus `True or not True => True or False => True`
* order of precedence, `not, and, or`


## Practicals
* Find the Truth Value of the following:
    * `True and not False`
    * `not True and not False`
    * `True and False and True or False`
    * `True or False and True or False`
* Write a simple program that makes use of all the relational and logical operators.

## Summary
* Relational operators are used for comparison
* Locagical operators are use to combine simple relational expressions
* `not` is a uninary operator