# Exercise 12 a (A function and its  definition)

A function is a block (piece) of code, with a unique name and maybe, takes some data, that performs a specific task (computes on the data). The use of functions prevents one from repeating a particular piece of routine/procedure/process over and over again.

## Basic Use Of Functions

### Example 1

Let say we want to ask a user five names and print them out with some string.

```Python
some_str = "$"

first_name = input("Enter first name: ")
print(first_name + some_str)

second_name = input("Enter second name: ")
print(second_name + some_str)

third_name = input("Enter third name: ")
print(third_name + some_str)

fourth_name = input("Enter fourth name: ")
print(fourth_name + some_str)

fifth_name = input("Enter fifth name: ")
print(fifth_name + some_str)

```

The code above works well, we achieved our goal but we waisted a lot of time rewriting all these (input and output) for five times. One of the solutions would be to use a loop.

### Example 2

A snippet that asks a user for five names and prints them out with some string.

```Python
some_str = "$"

for i in range(5):
    name = input("Enter name: ")
    print(name + some_str)  # str concat

```

Well, this code also works well. The problem is that, what if we want it multiple times, perhaps at different parts of our code? What about in another file? Of course, one would say, copy and paste it. There is better.

Now another approach is the modular (functional) approach.

### Structure a function

Let's see how to create a function.

```Python
def function_name():
    # code

```

The `def` keyword is used to define a function, followed by a function name, `function_name`. The function takes at least zero arguments (data) in parenthesis, followed by a colon, `:` which indicates the function block. Know that a function name should not be a python [keyword], a builtin function or a class name.

### Example 3

Let's create a function to read and output 5 names by calling the function 5 times. In this situation, we have bundled the input and output as one.

```Python
def get_and_print_name():
    some_str = "foo"

    person_name = input("Enter name: ")
    print(person_name + some_str)

# to make this function work, we have to call it just
# as we do to variables but here we add `()` to it.
# Do you remember print() and input()? These are all
# function calls.


get_and_print_name()
get_and_print_name()
get_and_print_name()
get_and_print_name()
get_and_print_name()

# well isn't there some repetition here? Yes, there is.
# or we can use a loop

for i in range(5):
    get_and_print_name()

```

### Example 4

A program that calculates and prints the `area` of a triangle taking the `base` and `height` as inputs.

```Python
def calc_area():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    area = 0.5 * base * height

    print(
        f"The area of a triagle of base, {base} and height, {height} is {area}")


# function call
calc_area()

```

## Functions and data

An argument is a value (some times a reference of the value) we pass to a function so that the function compute upon it. Think of an argument as data that you feed into the function for some computation.

We can discuss this snippet:

```Python
def get_and_print_name():
    some_str = "foo"

    name = input("Enter name: ")
    print(name + some_str)

```

We can make it better by passing the name as an argument to the function instead of taking it as input from the user when the program is running.

### Function parameters

We need to modify `get_and_print_name` to take an argument.

#### structure

```python
def function_name(<param1>, <param2>, <...>):
    # code

```

Parameters dictate how we would pass data (argument) to the function when we call it. `<param1>, <param2>, <...>` are the parameters the function expects. It could be just one or none.

### Example 5

Modification of `get_and_print_name`. We shall pass a parameter of `name` instead, indicating the name, previously accepted as input.

```Python
def get_and_print_name(name):
    some_str = " foo"
    print(name  + some_str)


get_and_print_name('John Doe')
```

### Example 6

A better version of the `calc_area` code would be that we can pass argument (data) to it just as we did above. It will be better when we can dictate what the base or height can be. With this, we can modify the functionality of the function to return a particular area based on the arguments (data) passed.

```Python
# A program that calculates and prints the area of a
# triangle passing the base and height as arguments

def calc_area(base, height):
    area = 0.5 * base * height

    print(
        f"The area of a triagle of base, {base} and height, {height} is {area}m^2")


# take the base and height from the user
base = float(input("Enter base: "))
height = float(input("Enter height: "))

# call the function here
calc_area(base, height)

```

### Parameter and argument

When we create a function, the placeholders for the data that the function may need is what we call the parameter. If we look at the code above in `Example 6`, the parameters are `base` and `height` - meaning, the function would need two data to compute upon. Now, when we want to make use of the function, call the function, we pass the required data as argument.

```Python
def calc_area(base, height):
    # code


calc_area(3, 4)

```

#### Note

- `base` and `height` in `def calc_area(base, height)` are parameters
- `3` and `4` are arguments
- we can assign `3` and `4` to variables and pass these variables as arguments instead.

```Python
def calc_area(base, height):
    # code


base = 3
height = 4
calc_area(base, height)

```

## Advantage of using a function

- Reduce code redundancy
- It is easier to catch and fix a bug in our code
- It can be plugged into another code

#

[keyword]: https://docs.python.org/3/reference/lexical_analysis.html#keywords
