# exercise 7 (String operations and function)
A string is a sequence of at least zero characters enclosed winthin (delimiter by) an opened and closed single or double quotation marks. This include any character, even a space. `Eg: 'swift python', "Alan Turing"`

## String operations
Basically is about how you can manipulate strings. We would use the addition, `+`, and multiplication, `*`, operators, repectively, to cancatenate (_join_) and repeat a string.

### Example
Concatenation, in this context is add one to another.

```python
# String concatetion
first_name = 'Daniel'
last_name  = "Doe"
full_name = first_name + " " + last_name  
# we added the first name and the last name to 
# produce a full name. The " " is an empty string but
# with space between the delimeters
# output => Daniel Doe
# With the space, we'd have, DanielDoe

# String repetition
# Let say you want to repeat a particular string for n
# number of times, you basically do, string * n.
# Lets try to repeat "Hello" three time
print("Hello" * 3)
# output=> HelloHelloHello
```

## String function
These function will help you format the string. There are a lot of this function, walk through them in the [docs](https://python.org)

### Calling the function
a function as we'd discuss later is a piece of code that **does** something. This done this way. `my_string.function()`.

```python
########### String functions ##########
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

# There is a whole lot on the python home page
```

## Practical
* Write a program to take input from the user, print the input seperate by a short-dash, `-` and the length of the string.
* Write a program reads data from the user and converts the data to lower case, upper case, title and capitalize.

## Summary
* String concatenation - add (join) one string onto another. `Eg: name = 'Future' + ' ' + 'Dann'.`
* String repetition - repeat a string for _n-times_.`Eg: print("Green tea" * 2).`
* Do `my_string.function_name()` to call a string function.
