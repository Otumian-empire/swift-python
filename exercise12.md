# excercise 12 (Functions)
A function is simply a block of code, with a unique name and maybe, has some arguments, that performs a specific task. The use of functions prevents one from repeating a particular piece of routine/procedure over and over again.
A function is of the structure:

```python
def function_name():
    # some code

# Assuming we have created this function, we call 
# ( reference this function by calling it by its name 
# followed by the open and close parenthese)
function_name()

```

## Example
Let say we want to ask five users their name and print it some string.

```python
# basically what we'd do is take the user name and print it

some_str = "$$$"

# first person
first_person = input("Enter name: ")
print(first_person + some_str)

# second person
second_person = input("Enter name: ")
print(second_person + some_str)

# third person
third_person = input("Enter name: ")
print(third_person + some_str)

# fourth person
fourth_person = input("Enter name: ")
print(fourth_person + some_str)

# fifth person
fifth_person = input("Enter name: ")
print(fifth_person + some_str)

```

The code above works well, we achieve our goal but we waisted a lot of time rewriting all these for five times. A simple solution would be to use a loop

## Example
```python
# reading and outputting 5 users name using a loop

for i in range(5):
    person_name = input("Enter name: ")
    print(person_name  + some_str)

```

Well this code also works well. Now another approach is the mudular ( functioanl approach).

```python
# create a function to reading and outputting 5 users name
# by calling the function 5 times

def get_and_print_name():
    person_name = input("Enter name: ")
    print(person_name  + some_str)


get_and_print_name()
get_and_print_name()
get_and_print_name()
get_and_print_name()
get_and_print_name()

# well isn't there some repetition here? Yes there is.
# or you can use a loop
for i in range(5):
    get_and_print_name()

```
## Advantage of using a function
* Reduce code redundancy
* It is easier to catch and fix bug in your code
* It can be plugged into another code

## Example
```python
# A program that calculates and prints the area of a triangle taking the 
# base and height as inputs

def calc_area():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    area = 0.5 * base * height

    print(f"The area of a triagle of base, {base} and height, {height} is {area}")

# call the function here
calc_area()

```

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

## Function with many arguments
Some time one'd like to pass plenty argument into a function and thus one is forced to give the function numerous parameters on creation but there is a very simple approach in python.

### Example
```python
# A function the takes a number of strings as argument and returns their length

def many_args(s1, s2, s3, s4, s5):
    print(len(s1))
    print(len(s2))
    print(len(s3))
    print(len(s4))
    print(len(s5))

many_args('sandy', 'jude', 'mani', 'desmond', 'peter')

# what the heck, what if there were about 1000's of args?

# better version is to use the tuple argument, *arg_name
# so every thing you pass is seen as a tuple does we can iterate easily

def many_args(*s):
    for i in s:
        print(len(i))

many_args('sandy', 'jude', 'mani', 'desmond', 'peter', 'sandy', 'jude', 'mani', 'desmond', 'peter', 'sandy', 'jude', 'mani', 'desmond', 'peter')

```

## Note
* You can do some do `some_name = func_name` then do, `some_name()`. this will work just like `func_name()`

## Practicals
* Given a list, whose elements are also list ( talking about nested list), write a function that sorts this list and it list elements if possible

## Summary
* A function is simply a block of code than can be called and arguments be passed to it
* function definition 
```python
    def function_name(some_args):
        # some code
``` 

* you can call the function by doing `func_name(some_args)`
* A function allows resue of code
* A function can be used in any part of our code
* paramter are passed into the function when creating the function
* argument is what we pass to the function when we are calling it
* `return` exits a function and returns a value from the function
* use the *arg - tuple argument to collect more arguments
* A function may be called as many times as possible
