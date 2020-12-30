# Exercise 9 (Logical and relational operators)

We advice skimming through or revisiting `Exercise 3 ( More on data types and comments)`.

How are boolean values generated? Logical operators with the use of Relation operators generate Boolean Values. We are saying that when we compare values, boolean values (`True` or `False`) are returned as a result.

## Relational Operators

Relational operators are binary operators just like the Arithmetic operators. `Eg: <, >, <=, >=, ==, !=` . Hence are sometimes referred to as Comparison operators. They are used for comparing values.

### Table of relational operators

| Operator |           Name           | Use case | Return value |
| :------: | :----------------------: | :------: | :----------: |
|    <     |        less than         | `3 < 2`  |   `False`    |
|    >     |       greater than       | `3 > 2`  |    `True`    |
|    <=    |  less than or equal to   | `3 <= 2` |   `False`    |
|    >=    | greater than or equal to | `3 >= 2` |    `True`    |
|    ==    |         equal to         | `3 == 2` |   `False`    |
|    !=    |       not equal to       | `3 != 2` |    `True`    |

### Example

```Python
# let a and b be two non-zero integers of value 5 and 7 respectively
a = 5
b = 7

# Pay much attention to the Truth values generated

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
# Not the double equal to. Unlike the assignment operator,
# which is just a character.

# not equal to
print(a != b)
# `!` , means `not`
```

## Logical Operators

Logical operators, combine two or more expressions to generate a boolean value. `Eg: and, or, not`. This combines more relational expressions to generate a truth value.

### The truth tables

The truth table simplifies what truth values are generated when using any of the logical operators.

Assume `t` as `True` and `f` as `False`

#### AND table

For an `AND` table, the truth value becomes `True` only when both components are `True`.

|  a  |  b  | a and b |
| :-: | :-: | :-----: |
|  t  |  t  |    t    |
|  t  |  f  |    f    |
|  f  |  t  |    f    |
|  f  |  f  |    f    |

#### OR table

For an `OR` table, the truth value becomes `False` only when both components are `False`.

|  a  |  b  | a or b |
| :-: | :-: | :----: |
|  t  |  t  |   t    |
|  t  |  f  |   t    |
|  f  |  t  |   t    |
|  f  |  f  |   f    |

#### Not table

For a `NOT` table, when the value is `True` it becomes `False` and when it is `False` then it becomes `True`. `NOT` here is the same as negation in some context. If an expression evaluates to `True` its negation will be `False`.

|  a  | not a |
| :-: | :---: |
|  t  |   f   |
|  f  |   t   |

### Example

```Python
# let a and b be two non-zero integers of value 5 and 7 respectively
a = 5
b = 7

# and
print(a <= 10 and b >= 10)

# or
print(a <= 10 or b >= 10)

# not
print(not a <= 10)
print(not b >= 10)

# compound with logical operators
print((a <= 10) and (b >= 10))

print((a <= 10) or (b >= 10))

print((a <= 10) or (b >= 10))
```

### Note

- Any value that is `None` (null - has no value), empty, zero, ... is evaluated to `False` otherwise `True`.
- So all empty structures are evaluated to False by Python.
- `not` is unary, then `True or not True => True or False => True`
- order of precedence, `not, and, or`

## Practicals

Find the Truth Value of the following:

- `True and not False`
- `not True and not False`
- `True and False and True or False`
- `True or False and True or False`

## Summary

- Relational operators are used for comparison
- Logical operators compound simple relational expressions
- `not` is a unary operator
