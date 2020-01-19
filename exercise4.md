# Exercise 4 ( Arithmatic Operators)
Arithmetic operators are reserved symbols that are used for performing mathematical operations ( calculations).

## Examples

| operators | symbols | use  | return type |
| :------:  | :-----: | :-: | :---------: |
| Addition | + | 1 + 3 | int|
| Subtraction | - | 3 - 1 | int|
| Multiplication | * | 3 * 2 | int|
| Exponent | ** | 3 ** 2 | int|
| Float division | / | 3 / 2 | float|
| Integer division | // | 3 // 2 | int|
| Modulo | % | 3 % 2 | int|

### Note

* If one of the operands is a float, then the resulting value is casted ( converted) into float. `Eg: 1.0 + 1 = 2.0 and 1 + 1 = 1` .
* `//` , returns the whole number part ( quotient) of the division. So, `given: 22.0 // 3 = 7.0 and 22 // 3 = 7` .
* `/` , returns the quotient and the remainder as a float, together. `Eg: 22 /3 = 7.333333333333333 and 0.25 / 0.5 = 0.5` .

# Casting

Casting means, converting or changing from one type to another. To know the type of a value, use the `type(obj)` function. `Eg: type(2) and type('2') will return <class 'int'> and <class 'str'>` respectively. Meaning that, 2 is an integer and '2' is a string.

``` python
# casting
x = 2 # x is an int
y = float(x) # we cast x to a float and passed the value to y
z = str(y) # y is a float, changed to a string and the value assigned to z
```

## Note

The values of x and y doesn't change after the casting, except that we do, `y = float(y)` .

# Practicals

write a program to evalute and print the results of the following given that `a = 2` and `b = 5` :

1.  - a * (2 * b) - 5
    - 2 * (b - a) + b
1. (-(a * b) ** 2 - (4 * a * b) ) / ((b // a) // 3 + (16 / a / b))
1. ((a ** 2) - (b ** 2)) // ((b - a) ** 2)
1. ((a + b) % 2) - ((b % a) + 1)

# Summary

* `+, -, *, **, /, //, %` are reserved for mathematical operations.
* Rule of precedence is `(), **, *, //, /, +, -` .
* Use parentheses to change the precedence.

