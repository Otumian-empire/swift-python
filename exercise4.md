# exercise 4 (Arithmatic Operators)
Arithmetic operators are reserved symbols that are used for performing mathematical operations ( calculations).

## Examples
operators | symbols | use  | return type
----------------------------------------
Addition | + | 1 + 3 | int
Subtraction | - | 3 - 1 | int
Multiplication | * | 3 * 2 | int
Exponent | ** | 3 ** 2 | int
Float division | / | 3 / 2 | float
Integer division | // | 3 // 2 | int
Modulo | % | 3 % 2 | int

# Note
* If one of the operands is a float, then the resulting value is casted ( converted) into float. `Eg: 1.0 + 1 = 2.0 and 1 + 1 = 1`.
* `//`, returns the whole number ( quotient) of the division. So,  `given: 22.0 // 3 = 7.0 and 22 // 3 = 7` .
* `/`, returns the quotient and the remainder as a float, together. `Eg: 3 / 2 = 1.5 and 0.25 / 0.5 = 0.5` .

# Practicals
write a program to evalute and print the following given that `a = 2` and `b = 5`:

1. 
    * a * (2 * b) - 5
    * 2 * (b - a) + b
1. (-(a * b) ** 2 - (4 * a * b) ) / ((b // a) // 3 + (16 / a / b))
1. ((a ** 2) - (b ** 2)) // ((b - a) ** 2)
1. ((a + b) % 2) - ((b % a) + 1)

# Summary
* `+, -, *, **, /, //, %` are reserved for mathematical operations.
* Rule of precedence is `(), **, *, //, /, +, -`.
* Use parentheses to change the precedence.
