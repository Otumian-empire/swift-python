# Exercise 11 (Loops)
The need to repeat a certain process for a particular number of time or for as long as a particular condition holds arise. Here we'd look into loops ( also know iterations). There are basically two types of loops in python, the `for` and `while` loop.

Already, you have seen a list, briefly. A list is an in built structure for holding data ( a collection of these data actually). A list can be looped upon.

## Example of a list

``` python
# a list is a comma seperature collection of objects 
# (numbers, strings, other structure, etc), delimited by 
# open and close square bracket
# which permits looping or iteration
num_list = [1, 2, 3, 4, 5]
str_list = ['John', 'Mathew', 'zack', 'Doe']
```

Basically those are sample lists and perhaps our interest maybe to read all the elements of the list and then maybe do something with it.

## For loop

Structure of a `for` loop

``` python
for element in some_structure:
    # do something
```

### Structure looping with for

The `element` is an arbituary word we have use to refer to the current object ( element) in the `some_structure` . `some_structure` is an object with can be iterated upon.

#### Example

``` python
# looping through a list of numbers and adding 2 to each element 
# and displaying it
num_list = [1, 2, 3, 4, 5]
for number in num_list:
    print(number, '+', 2, "=", number + 2)
    # print(f"{number} + 2 = {number + 2})  # generates the same output as above
    
# looping through a list of strings and using the inbuillt function, len
# to find the length of the string element
str_list = ['John', 'Mathew', 'zack', 'Doe']
for str_element in str_list:
    print(f"{str_element} has a length of {len(str_element)}")
```

### Range looping

Now `some_structure` can be an in built function known as `range` . `range` is an iterating object, thus permits looping. The `range` funtion is of the form , `range(start, end, step)` . By default, it starts at `0` and steps at `1` . You may just pass `end` into the `range` function and it will work fine from `0` to `end` exclusive, `step` 1.

#### Note 

A list is an indexed object, thus one may access the element in the list using the index of the element in the list. The index always starts from `0` .

``` python
# str_list = ['John', 'Mathew', 'zack', 'Doe']
# their index:   0      1         2       3
# thus the last element in the list would have length of list minus one index.
```

#### Example

``` python
# looping through a list of numbers and adding 2 to each element 
# and displaying it, using the range function ( their index)
num_list = [1, 2, 3, 4, 5]

# get the length of num_list
len_num_list = len(num_list)

for index in range(len_num_list):
    print(num_list[index], '+', 2, "=", num_list[index] + 2)
    # print(f"{num_list[index]} + 2 = {num_list[index] + 2})

# looping through a list of strings and using the inbuillt function, len
# to find the length of the string element, using the range function
str_list = ['John', 'Mathew', 'zack', 'Doe']
len_str_list = len(str_list)

for str_index in range(len_str_list):
    print(f"{str_list[str_index]} has a length of {len(str_list[str_index])}")

# looping in range of 0 to 10 (by default 10 would not be 
# display but the looping occurs 10 times)
# because the loop is exclusive `end` 
# for i in range(0, 10):
for i in range(10):
    print(i)

# looping in range of 1 to 10
for i in range(1, 10):
    print(i)

# looping in range of 1 to 10, stepping 2
for i in range(1, 10, 2):
    print(i)
# output [1, 3, 5, 7, 9]

# print even numbers less than 20
for i in range(0, 20, 2):
    print(i)

# print odd numbers less than 20
for i in range(1, 20, 2):
    print(i)

# print elements in the reverse order
str_list = ['John', 'Mathew', 'zack', 'Doe']
len_str_list = len(str_list)

# last element, length of list minus one, thus start = len_str_list - 1
# end = -1
# step = -1

for index in range(len_str_list - 1, -1, -1):
    print(f"{str_list[index]}")

# assuming end = 0, implies that we only displace size minus one elements
```

## While loop

This loop does something ( executes its body until a condition is met or as far as a condition is still valid)

Structure of a `while` loop

``` python
while condition:
    # do something
```

Recall the exercise on conditions here.

### Structure looping with while

Usually we find the length of the structure and we'd use it as we did with the range. Consider the example below.

#### Example

``` python
# looping through a list of numbers and adding 2 to each element 
# and displaying it

num_list = [1, 2, 3, 4, 5]
length_of_list = len(num_list)

base = 0
# base is some arbituary variable
# we use base, as in base case
# our interest is to access the elements in the list using their index
# the first element is 0, second is 1 and so on.
# sure the last item will have an index of (length_of_list - 1)
# the index of the last element is less than the length of the list

while base < length_of_list:
    print(f"{num_list[base]} + 2 = {num_list[base] + 2}")
    base = base + 1  # base += 1 works fine too
    
# looping through a list of strings and using the inbuillt function, len
# to find the length of the string element

str_list = ['John', 'Mathew', 'zack', 'Doe']
for str_element in str_list:
    print(f"{str_element} has a length of {len(str_element)}")
```

#### Note

* In the above code, without `base = base + 1` , the loop becomes an infinite loop. A loop that would nerver terminate.
* Also assume we just say, `while True:` , will also not terminate.

### The lift off program

``` python
# A simple program the simulates a lift off

# version 1
lift_off_time = 5  # 5sec
while lift_off_time >= 0:
    print(lift_off_time)
    lift_off_time -= 1

print("Lift off")

# version 2
lift_off_time = 5  # 5sec
while lift_off_time >= 0:
    if lift_off_time == 0:
        print("Lift off")
    else:
        print(lift_off_time)

    lift_off_time -= 1

# version 3
lift_off_time = 5  # 5sec
while lift_off_time >= 0:
    if not lift_off_time == 0:
        print(lift_off_time)
    else:
        print("Lift off")

    lift_off_time -= 1

# version 4
lift_off_time = 5  # 5sec
cur_time = 0
while cur_time <= lift_off_time:
    print(lift_off_time)
    lift_off_time -= 1

print("Lift off")
```

## Practicals

* write a lift off program using a for loop
* Give a list of alphabets from `a - z` , use a loop to print out the vowels (create a list of vowels)
* Write the roll dice simulation program. A fair dice has 6 sides numbered from 1 to 6. Take an integer input from the user as the number of times the dice must be rolled and this value must be greater than 50. Using a loop (any loop) and an if, elif and else statement ( if necessary) and then print the number of times a particular number was obtained when the dice was rolled.

> Use all that you have learnt up to this exercise

## Summary

* A loop is used for repetition, for a particular number of time or based on some condition
* The two types of loops, `for` and `while` loop
* `for` loop is best used when we know the range
* `while` loop is best when the repetition is based on a condition
* One can loop ( iterate) through a structure such as a list or any object with an iterator in built

