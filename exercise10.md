# Exercise 10 (Conditions)

In the previous exercise, `Exercise 9 (Logical and relational operators)` , we discussed relational and logical operators, and in this exercise we shall make use of Truth values.

This exercise is about decision making, conditions.

One would like to display certain output or take input or even terminate the program based on a certain condition. In Python we have the `if, elif and else` , statements which makes it easier to do some comparison.

## If statement

Basically, this is the structure of an `if` statement.

```Python
if <condition>:
    # some code
```

This starts with the `if` keyword, followed by a condition to evaluate then a colon, `:` . On a newline, we indent beyound the `if` keyword and add the code to execute when the condition is `True` .

### Example

```Python
# A simple program to check if a driver is driving above
# the speed limit

MAX_SPEED = 120  # this is a constant

# get the drivers speed
drivers_speed = float(input('Enter Vehicle speed: '))

if drivers_speed >= MAX_SPEED:
    print("Please slow down, spare your family the cost and grief.")
```

### Note

Nothing happends when the drivers speed is below speed limit

## Else statement

Perhaps We want to alert the user to do something when the condition fails or evaluates False, then one must add an `else` statement.

```Python
if <condition>:
    # some code
else:
    # do something else
```

### Example

```Python
# A simple program to check is a driver is driving 
# above the speed limit

MAX_SPEED = 120
drivers_speed = float(input('Enter Vehicle speed: '))

if drivers_speed >= MAX_SPEED:
    print("Please slow down, spare your family the cost and grief.")
else:
    print("waw, a very responsible being... You are one of a kind")
```

### Note

Python uses indentation for structuring or creating block codes. Consider the above example on `if else` statement, all the code in the indentation below the `if` statement is the body or block of the `if` . Those that are outside the `if`' s indentation forms another block of code. So make proper use of the indentations and use it correctly.

## Elif statement

So after the if statement failed, one may want to check for another condition, before the the `else` block, then we use the `elif` which is like, `else if` . Also there are certain instances where by a condition is neither `True` nor `False` but something closer. Consider when we take an integer input from a user, the input can be less than some constant, greater than that constant or even equal to that constant. Thus an `elif` statement becomes useful here.

### Example

```Python
# A program to check the speed limit on the high way
# lets assume that the minimum and maximum speed limit
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

We may have a nested `if else` statements as many as We please

### Example

```Python
# this code has something to do with the above
# but here we check if the driver has parked
# or is over speeding senselessly
# assume reverse for a negative value

PARKED_SPEED = 0
MIN_SPEED = 40
MAX_SPEED = 120
OVER_SPEED = 200

drivers_speed = float(input('Enter speed: '))

if drivers_speed < MIN_SPEED:

    # check if the vehicle is parked on the highway
    if drivers_speed == PARKED_SPEED:
        print("Please don't park on the high way.. It's deadly man.")
    else:
        print(f"Please drive at least {MIN_SPEED}km/h")

elif drivers_speed > MAX_SPEED:

    # check if the vehicle is really light speed
    if drivers_speed > OVER_SPEED:
        print("Please We are not on a racing track, We are over speeding")
    else:
        print(f"Please drive at most {MAX_SPEED}km/h")

else:

    # check if the vehicle is reversing
    if drivers_speed < PARKED_SPEED:
        print("what the heck man, no reversing on the highway")
    else:
        print("Rock on man")

# As We may see, we can have even more nested if and else and
# elifs as much as we can provided they don't make the code 
# hard to read
```

#### Note

White spaces, such as, spaces, newlines and indentation only makes our code pretty to read but has no effect on the code we write.

## Compound statements

Remeber relational and logical operators? We have made use of relational, what about logical?

### Example

```Python
# this code is the same as above but just serving some 
# different concept. we know it is bad to park or reverse 
# on the high way. kind of we can evaluate these two together,
# the maximum speed limit and the overspeeding limit are all 
# the same. we can either use a relational or a logical, either 
# would do. for the relational, over speeding limit is greater 
# than the maximum speed thus we may check for maximum speed

PARKED_SPEED = 0
MIN_SPEED  = 40
MAX_SPEED  = 120
OVER_SPEED = 200

drivers_speed = float(input('Enter speed: '))

# we use `<=` to compound reversing and parked
# we use `or` to compund the previous and minimum speed
if (drivers_speed <= PARKED_SPEED) or (drivers_speed < MIN_SPEED):
    print(f"Please drive at least {MIN_SPEED}km/h")
elif drivers_speed > MAX_SPEED:
    print(f"Please drive below {MAX_SPEED}km/h")
else:
    print("Rock on man")

```

### Note

```Python
# consider, when given
MAX_SPEED  = 120
OVER_SPEED = 200
drivers_speed = 210

# if We would like to catch OVER_SPEED, We check for OVER_SPEED 
# first else it won't be catched
if drivers_speed > OVER_SPEED:
    print("Over speed")
elif drivers_speed > MAX_SPEED:
    print("Max speed")
else:
    print("Rock on")

# unlike this example, OVER_SPEED would never be reached
# because OVER_SPEED is greater than MAX_SPEED
# even when drivers speed is 3000km/h
if drivers_speed > MAX_SPEED:
    print("Max speed")
elif drivers_speed > OVER_SPEED:
    print("Over speed")
else:
    print("Rock on")

```

## Practicals

- Write a program that checks if a given integer input is a multiple of 2, 3 or both 2 and 3.

  ```Python
  # the code should behave this way

  # input = 4
  # output = 4 is a multitple of 2

  # input = 6
  # output = 6 is a multitple of 2 and 3

  # input = 9
  # output = 9 is a multitple of 3

  # input = 18
  # output = 18 is a multitple of 2 and 3

  # input = 5
  # output = 5 is not a multiple of 2 or 3
  ```

## Summary

- `if else` and `elif` statement are used to create conditional statements.
- use `:` to create a block, followed by a consistent indentation
- the body of the `if` block is reached only if the condition evaluates to `True`
- We may have compound conditions in the `if` and `else` statement
