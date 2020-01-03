# Exercise 10 (Conditions)
In the previous  exercise we discussed relational and logical operators, and in this exercise we shall make use of Truth values.

This exercise is about decision making. One would like to display certain output or take input or even terminate the program based on a certain condition. In python we have the `if, elif and else` , statements which makes it easier to do some comparison.

## If statement

Basically, this is the structure of an if statement.

``` python
if condition:
    # some code
```

This starts with the `if` keyword, followed by a condition to evaluate then a `:` . On a newline, you indent beyound the `if` keyword and add the code to execute when the condition is `True` .

### Example

``` python
# A simple program to check is a driver is driving above the speed limit

MAX_SPEED = 120  # this is a constant
drivers_speed = float(input('Enter Vehicle speed: '))

if drivers_speed >= MAX_SPEED:
    print("Please slow down, think about your life and family first.")
```

### Note

Nothing happends when the drive is below speed limit

## Else statement

Perhaps you want to alert the user to do something when the condition fails ( becomes False), then one must add the else part.

``` python
if condition:
    # some code
else:
    # do something else
```

### Example

``` python
# A simple program to check is a driver is driving abpve the speed limit

MAX_SPEED = 120
drivers_speed = float(input('Enter Vehicle speed: '))

if drivers_speed >= MAX_SPEED:
    print("Please slow down, think about your life and family first.")
else:
    print("waw, very responsible being.. You are one of a kind")
```

### Note

Python uses indentation for structuring. Consider the above example on `if else` statement, all the code in the indentation below the `if` statement is the body of the `if` . Those that are outside the ifs indentation forms another block of code. So make proper use of the indentations and use it correctly.

## Elif statement

So after the if statement failed, you want to check for another condition, before the the `else` block, then you use the `elif` which is like, `else if` .

### Example

``` python
# A program to check the speed limit on the high way
# lets assume that the minimum and maximum speed limit is
# is between 40 and 120 km/h.. something like this.

MIN_SPEED = 40
MAX_SPEED = 120

drivers_speed = float(input('Enter speed: '))

# method 1
if drivers_speed < MIN_SPEED:
    print(f"Please drive at least {MIN_SPEED}km/h")
else:
    if drivers_speed > MAX_SPEED:
        print(f"Please drive at most {MAX_SPEED}km/h")
    else:
        print("Rock on man")

# method 2, we use an inbuilt approach with combines `else if` 
if drivers_speed < MIN_SPEED:
    print(f"Please drive at least {MIN_SPEED}km/h")
elif drivers_speed > MAX_SPEED:
    print(f"Please drive at most {MAX_SPEED}km/h")
else:
    print("Rock on man")
```

## Nested Conditions

You may have a nested `if else` statements as many as you please

### Example

``` python
# this code has something to do with the above
# but here we check if the driver has parked
# or is over speeding senselessly
# assume reverse for a negative value

PARK_SPEED = 0
MIN_SPEED  = 40
MAX_SPEED  = 120
OVER_SPEED = 200

drivers_speed = float(input('Enter speed: '))

if drivers_speed < MIN_SPEED:
    # check if the vehicle is parked on the highway
    if drivers_speed == PARK_SPEED:
        print("Please don't park on the high way.. It's deadly man.")
    else:
        print(f"Please drive at least {MIN_SPEED}km/h")
elif drivers_speed > MAX_SPEED:
    # check if the vehicle is really light speed
    if drivers_speed > OVER_SPEED:
        print("Please you are not on a racing track, you are over speeding")
    else:
        print(f"Please drive at most {MAX_SPEED}km/h")
else:
    # check if the vehicle is reversing
    if drivers_speed < PARK_SPEED:
        print("what the heck man, no reversing on the highway")
    else:
        print("Rock on man")

# As you may see, we can have even more nested if and else and
# elifs as much as we can provided they don't make the code hard to read

```

## Compound statements

Remeber relational and logical operators? We have made use of relational, what about logical?

### Example

``` python
# this code is the same as above but just serving some different concept
# we know it is bad to park or reverse on the high way,
# kind of we can evaluate these two together
# the maximum speed limit and the overspeeding limit are all the same
# we can either use a relational or a logical, either would do
# for the relational, over speeding limit is greater than the maximum speed
# thus we may check for maximum speed

PARK_SPEED = 0
MIN_SPEED  = 40
MAX_SPEED  = 120
OVER_SPEED = 200

drivers_speed = float(input('Enter speed: '))

# we use `<=` to compound reversing and parked
# we use `or` to compund the previous and minimum speed
if (drivers_speed <= PARK_SPEED) or (drivers_speed < MIN_SPEED):
    print(f"Please drive at least {MIN_SPEED}km/h")
elif drivers_speed > MAX_SPEED:
    print(f"Please drive at most {MAX_SPEED}km/h")
else:
    print("Rock on man")

```

### Note

``` python
# consider, when given
MAX_SPEED  = 120
OVER_SPEED = 200
drivers_speed = 210

# if you would like to catch OVER_SPEED, you check for OVER_SPEED first else it won't be catched
if drivers_speed > OVER_SPEED:
    print("Over speed")
elif drivers_speed > MAX_SPEED:
    print("Max speed")
else:
    print("Rock on")

# unlike this example, OVER_SPEED would never be reached
if drivers_speed > MAX_SPEED:
    print("Over speed")
elif drivers_speed > OVER_SPEED:
    print("Max speed")
else:
    print("Rock on")

```

## Practicals

* Write a program that checks if a given integer input is a multiple of 2, 3 or both 2 and 3 and then print what multiple it is with the input.

``` python
# your code should pass these inputs
# input = 6
# output = 6 is a multitple of 2 and 3

# input = 9
# output = 9 is a multitple of 3

# input = 18
# output = 18 is a multitple of 2 and 3
```

## Summary

* `if else` and `elif` statement are used to create conditional statements.
* use `:` to create a block, followed by a consistent indentation
* the body of the `if` block is reached only if the condition holds
* you may have compound conditions for the `if` and `elif` statement

