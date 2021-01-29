# Excercise 12 c (Recursive and lambda functions)

> This is a continuation of `exercise 12 b (A function that returns a value)`

## Recursive functions

We have discussed how to create a function, how pass an argument to the function and then how to call a function. We have done a lot, it will pay us well if we take breaks frequently.

In this exercise, we would discuss more on function. A recursive function calls itself. It does so until the base case becomes false.

Let's implement a factorial function. Our function will take in an integer input. If the input is less than 1, the function returns 1, else we proceed.

Let the integer input be, `n`. `n` factorial is, `n!` = `n * (n - 1) * (n - 2) * (n - 3) * ... * 1`. Our base case is 1. When we get to one we break.

### Example 1

```Python
factorial = 1
n = int(input("Enter n: "))

if n < 1:
    print(1)
else:
    for i in range(1, n+1):
        factorial *= i

    print(factorial)

# input  output
#    3     6
#    5     720
#    15    1307674368000
```

### Example 2

Now we shall implement the above using a recursive function.

```Python
def factorial(n):
    if n < 1:
        return 1

    else:
        return n * factorial(n-1)
```

- `def factorial(n)`: we define a function called factorial that take an integer argument, `n`.
- `if n < 1: return 1`: we check the base case and return 1. The function returns 1 and the execution stops.
- `else: return n * factorial(n-1)`: if `n > 1`, we return `n` multiplied by `factorial(n-1)`.
- If `n=5`, we would have that:
  - `factorial(5) = 5 * factorial(4)`
  - `factorial(5) = 5 * 4 * factorial(3)`
  - `factorial(5) = 5 * 4 * 3 * factorial(2)`
  - `factorial(5) = 5 * 4 * 3 * 2 * factorial(1)`
  - `factorial(5) = 5 * 4 * 3 * 2 * 1`
  - `factorial(5) = 720`

### Example 3

Implementation of Euclid GCD algorithm. We are interested in the greatest common divisor of two numbers, `gcd(a, b)`.

Algorithm:

- let a, b be the two numbers
- let r be the remainder of a and b, `a % b`
- check if r is 0, b divides a, if so, return b
- else assign b to a and r to b and repeat the second step

```Python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

while True:
    r = a % b

    if r == 0:
        print(b)
        break

    else:
        a = b
        b = r

# a = 72
# b = 96
# gcd(a, b) = 24
```

### Example 4

Using recursion.

```Python
def gcd(a, b):
    r = a % b

    if r == 0:
        return b

    else:
        return gcd(b, r)

print(gcd(72, 96))  # 24
```

Let us shorten this code

```Python
def gcd(a, b):
    if a % b == 0:
        return b

    return gcd(b, a % b)
```

## Lambda functions

Lambda function is also known as anonymous functions - functions without a name. We can say they are a one-time-function. We create a lambda function using the `lambda` keyword.

### Structure

Let's consider a function that increments a given integer by one and returns the value.

```Python
def inc(n):
    return n + 1


print(inc(2))  # 3

```

The snippet above uses the `def` keyword to create the function. Now let's see how we would use the `lambda` keyword to create the same function.

#### Example 5

```Python
print((lambda x: x+1)(2))  # 3
```

So the structure of a lambda function is similar to that of normal function. We use the `lambda` keyword instead of `def`, the function has no name. Any parameters are space comma-separated from the lambda keyword. The function body is separated by a colon, `:`.

#### Example 6

We can pass multiple arguments into a lambda function. Note that we can not use `return` lambda function. Let's use a lambda function to compare two numbers and return the lesser number.

```Python
print((lambda a, b: a if a < b else b)(2, 4))  # 2

```

Normally we would have written,

```Python
def min_val(a, b): return a if a < b else b


print(min_val(2, 4))  # 2
```

This is the same as :

```Python
def min_val(a, b):
    if a < b:
        return a
    else:  #  we can comment out the else:
        return b
```

### Assigning name to lambda functions

Consider `example 5` where we increment a given number by one, we can pass the lambda function to a variable and call the function later.

```Python
inc = (lambda n: n + 1)

print(inc(2))  # 3
```

CAn you tell the difference between these two,

```python
# first func
inc = (lambda x: x + 1)
print(inc(4))

# second func
inc = (lambda x: x + 1)(4)
print(inc)
```

## Practicals

- Write a function to sort this list, `[[47, 3, 1, 34], [0. - 3, 4], [7, 21, 13, 37, 8]]`
- Write a function that returns the temperature from degree Fahrenheit to degree Celcius
- Write a function that returns the sum of numbers between a given range inclusive. If the range is `1 to 5`, return `15`.
- Write a function the prints the squares between a given range inclusive
- Write a function that sums up the individual digits in a given integer. Given, `12345`, return `15`
- Write a function that verifies if a given year is a leap year. For a given input to be a leap year, it must be divisible by 4 but(and) not divisible by 100, or the input is divisible by 400.

## Summary

- A function is a block of code that performs a specific task
- A function can take at least zero arguments
- function definition

  ```Python
  def function_name(some_args):
      # some code
  ```

- we can call the function by doing `func_name(some_args)`
- A function allows reuse of code
- A function can be used in any part of our code
- parameters are passed into the function when creating the function
- argument is what we pass to the function when we are calling it
- `return` exits a function and returns a value from the function
- use the \*arg - tuple argument to collect more arguments
- A function may be called as many times as possible
- A recursive function calls itself
- A lambda function is a nameless function, usually required on the fly
