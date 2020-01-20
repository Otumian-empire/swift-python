# Exercise 7 (String operations and function)
A string is a sequence of at least zero characters enclosed within ( delimiter by) an opened and closed single ( `''` ) or double ( `""` ) quotation marks. This include any character, even a space or numbers. `Eg: 'swift Python', "Alan Turing"` 

## String operations

These are operations - manipulations, we can do on strings objects. These are `string concatenation` and `string repetition` . We use the addition, `+` , and multiplication, `*` , operators, repectively, to cancatenate (_join_) and repeat strings.

### Example

Concatenation, in this context is add one string to another string.

``` Python
# String concatetion
first_name = 'Daniel'
last_name  = "Doe"
full_name = first_name + " " + last_name  

# we added the first name, space and then last name to 
# produce a full name. The " " is an empty string but
# with space between the delimeters
# output => Daniel Doe
# Without the space, we'd have, DanielDoe as the output

# String repetition
# Lets say we want to repeat a particular string for n
# number of times, we basically do, string * n.
# Lets try to repeat "Hello" three time
h = "Hello"
print(h * 3)
# output=> HelloHelloHello
```

## String function

These function will help us format the string. There are a lot of this function. The Python [docs][doc-site] has more.

### Calling the function

A function as we would discuss later is a piece of code that **does** something - performs certain computation. This done this way. `my_string.function()` .

``` Python

########### String functions ###########

name = "John"

# change of a name to lower case
print(name.lower())

# change of a name to upper case
print(name.upper())

# capitalize of a name - the first character becomes upper
# and the rest lower
print(name.capitalize())

# return string as a title format
print(name.title())

# remove (strip) 'h' from the name
print(name.strip('h'))

# find the length or size (number of characters) in name
print(len(name))

# split a string by some char
str_split = "hello world"
str_list = str_split.split(' ')  # ['hello', 'world']
print(str_list)

# join
list_str = ['hello', 'world']
new_str = " ".join(list_str)
print(new_str)  # "hello world"

# There is a whole lot on the Python home page
```

## Practical

* Write a program to take input from the user, print the input, seperated by a short-dash, `-` , and the length of the string. `Eg: input='Doe', output=Doe - 3` 
* Write a program that reads data from the user and converts the data to lower case, upper case, title and capitalize.

## Summary

* String concatenation - add ( join) one string onto another. `Eg: name = 'Future' + ' ' + 'Dann'.` 
* String repetition - repeat a string for _n-times_. `Eg: print("Green tea" * 2).` 
* Do `my_string.function_name()` to call a string function.

#
[doc-site]:(https://Python.org)

