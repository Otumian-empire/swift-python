# excercise 12 b (Functions)
> This is a continuation of `excercise 12 a (Functions)`

## A function with argument
An argument is basically a value ( some times a reference of the value) we pass to a function so that the function may make use to it to reach an end.

A better version of the above code would be that we are able to pass argument to it. It will be better when we can dictate what the base or height can be. With this we can modify the functionality of the function to return a particular area based on the arguments passed. 

### Example
# A program that calculates and prints the area of a triangle taking the base and height as arguments

```python
# A program that calculates and prints the area of a 
# triangle passing the base and height as arguments

def calc_area(base, height):
    area = 0.5 * base * height

    print(f"The area of a triagle of base, {base} and height, {height} is {area}")


# take the base and height from the user
base = float(input("Enter base: "))
height = float(input("Enter height: "))

# call the function here
calc_area(base, height)

```

### Note
There is what we call argument and also a parameter. They are almost the same basically. So an argument is a parameter. Use put the paramter into the function when creating the function and the argument is what we pass to the function when we are calling it.

```python
def calc_area(base, height):
    # code

calc_area(3, 4)

# base and height in def calc_area(base, height) are paramters
# 3 and 4 are arguments, also we can assign 3 and 4 to a variable and pass the variables as argument instead.
```

## Function that returns a value
Sometimes, one may want a value from a function to make use of it in one way or another. To achieve this we rather return the value rather printing it out in the function.

```python
# A function that returns a value
# this function returns the area of a triangle, taking the base and height as arguments

def calc_area(base, height):
    return 0.5 * base * height

# take the base and height from the user
user_base = float(input("Enter base: "))
user_height = float(input("Enter height: "))

# call the function here
area = calc_area(user_base, user_height)

print(f"The area of a triagle of base, {user_base} and height, {user_height} is {area}")

```

### Example a sorting function
```python
# this is a function that take list, an iterable as an argument and them sorts it
# how this sorting function works
# so give a list of size, n
# having 2 loops, nested actually,
# the first loop, loops through the function n times
# the second does, n - 1 time
# in the second loop we check if the the first value is greater than the second value
# if it is we swap the values and then we compare the second with the third and then
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
