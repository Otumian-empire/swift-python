# Excercise 12 b (Functions)

> This is a continuation of `excercise 12 a (Functions)` 

In `Excercise 12 a (Functions)` , we created the function

``` Python
def get_and_print_name():
    person_name = input("Enter name: ")
    print(person_name  + some_str)
```

We can make it better by passing some values to the function.

## A function with argument

An argument is basically a value ( some times a reference of the value) we pass to a function so that the function may make use it to reach an end. Think of an argument as data that you feed into the function for some computation.

``` Python
def get_and_print_name(name, some_str):
    print(f"{name} {some_str}")

get_and_print_name('John Doe', "$_$")
```

A better version of the `calc_area` code from `Excercise 12 a (Functions)` would be that we are able to pass argument ( data) to it just as we did above. It will be better when we can dictate what the base or height can be. With this we can modify the functionality of the function to return a particular area based on the arguments ( data) passed.

#### Example

``` Python
# A program that calculates and prints the area of a 
# triangle passing the base and height as arguments

def calc_area(base, height):
    area = 0.5 * base * height

    print(f"The area of a triagle of base, {base} and height, {height} is {area}m^2")

# take the base and height from the user
base   = float(input("Enter base: "))
height = float(input("Enter height: "))

# call the function here
calc_area(base, height)
```

#### Note

There is what we call argument and also a parameter. They are almost the same basically. So an argument is a parameter. Use put the paramter into the function when creating the function and the argument is what we pass to the function when we are calling it.

``` Python
def calc_area(base, height):
    # code

calc_area(3, 4)

# base and height in def calc_area(base, height) are paramters
# 3 and 4 are arguments, also we can assign 3 and 4 to a variable and pass the variables as argument instead.
```
## Parameter and argument

When we create a function, the placeholders for the data that the function may need is what we call the parameter. If we look at the code above, the parameters are `base` and `height` - meaning, the function would needs two data to compute upon. Now, when we want to make use of the function, call the function, we pass the required data as argument.

## Function that returns a value

Sometimes, one may want a value from a function to make use of it in one way or another. To achieve this we return the value rather than printing it out in the function.

``` Python
# this function returns the area of a triangle, taking the base and height as arguments

def calc_area(base, height):
    return 0.5 * base * height

# take the base and height from the user
user_base   = float(input("Enter base: "))
user_height = float(input("Enter height: "))

# call the function here, and pass user_base and user_height to it
# as the base and height needed
area = calc_area(user_base, user_height)

print(f"The area of a triagle of base, {user_base} and height, {user_height} is {area}")
```

### Example - a sorting function

``` Python
# this is a function that take list, an iterable as an argument and them sorts it
# how this sorting function works
# given a list of size, `n` 
# having 2 loops, nested actually,
# the first loop, loops through the function `n` times
# the second does, `n - 1` time
# in the second loop we check if the the first value is greater than the second value
# if it is we `swap` the values and then we compare the second with the third and then
# the third and fourth and so on until we reacch the end of the list
# then the first loop moves ( steps 1) then the sequence begins again

def sort_func(my_ite):
    """ This function takes a list as an argument and returns a sorted version of it """
    length_of_ite = len(my_ite)

    for i in range(length_of_ite):
        for j in range(1, length_of_ite):
            if my_ite[j - 1] > my_ite[j]:
                my_ite[j - 1], my_ite[j] = my_ite[j], my_ite[j - 1]

    return my_ite

print(sort_func([6, 3, 2, 4, 1]))
print(sort_func(['w', 't', 'a', 'i']))
```

