# Exercise 9 (Logical and relational operators)
We advice skimming through or revisiting `Exercise 3 ( More on data types and comments)` .

How are boolean values generated? Simple, logical operators with the use of Relation Operators generate Boolean Values.

## Relational Operators

Relational Operators, a binary operators just like the Arithmatic Operators. These are used for comparison. `Eg: <, >, <=, >=, ==, !=` . Thus are sometimes referred to as Comparison Operators.

### Table of relational operators

| Operator |     Name    |   Use case   | Return value|
| :------: | :---------: | :----------: | :---:|
|     <    | less than  | `3 < 2` | `False` |
|     >    | greater than | `3 > 2` | `True` |
|     <=   | less than or equal to | `3 <= 2` | `False` |
|     >=   | greater than or equal to | `3 >= 2` | `True` |
|     ==   | equal to | `3 == 2` | `False` |
|     !=   | not equal to | `3 != 2` | `True` |

### Example

``` Python
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
# `!` , means `not` 
```

## Logical Operators

Logical operators, combine two or more expressions to generate a boolean value. `Eg: and, or, not` . This combines more relational expressions to generate a truth value.

### The truth tables

The truth table simplifies what truth values are gebreated when use any of the logical operator.

Assume `t` as `True` and `f` as `False` 

#### AND table

For an `AND` table, the truth value becomes true only when both components are true.

|   a   |   b   | a and b |
| :---: | :---: |:------: |
|   t   |   t   |   t     |
|   t   |   f   |   f     |
|   f   |   t   |   f     |
|   f   |   f   |   f     |

#### OR table

For an `OR` table, the truth value becomes true on when either components are truth, or we could say, the truth value becomes false only when both components are false.

|   a   |   b   | a or b  |
| :---: | :---: |:------: |
|   t   |   t   |   t     |
|   t   |   f   |   t     |
|   f   |   t   |   t     |
|   f   |   f   |   f     |

#### Not table

For a `NOT` table, when the value is true it becomes false and when it is false then it becomes true. `NOT` here is the same as negation in some context. It is true and when it is not true then it is false.

|   a   |  not a  |
| :---: | :-----: |
|   t   |    f    |
|   f   |    t    |

### Example

``` Python
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

# compound with logical operators
print((a <= 10) and (b >= 10))

print((a <= 10) or (b >= 10))

print((a <= 10) or (b >= 10))
```

### Note

* Any value that is None (null), empty, zero, etc is valued to False otherwise True.
* So all empty structures are evaluated to False by Python.
* `not` is uninary, thus `True or not True => True or False => True` 
* order of precedence, `not, and, or` 

## Practicals

* Find the Truth Value of the following:
    - `True and not False` 
    - `not True and not False` 
    - `True and False and True or False` 
    - `True or False and True or False` 
* Write a simple program that makes use of all the relational and logical operators.

## Summary

* Relational operators are used for comparison
* Locagical operators are use to combine simple relational expressions
* `not` is a uninary operator

