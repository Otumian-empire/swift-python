# Exercise 8 (String formatting)
There are a lot of ways to format our output which makes manipulation of our output more readable. We'd go with the `f"... {some_value}"` approach.
The `{}` provides the means to insert values into our string as we write it out, `some_value` is the value you pass into the string and the `f` means format. The string must, begin with the `f` .

## Example

``` Python
# Consider a simple program to take the users
# name and age and then output them to the screen

user_name = input("Enter name: ")
user_age = input("Enter age: ")

output = f"User name: {user_name}\nUser age: {user_age}"

print(output)

# Another sample code
# A program to find the area of a triangle
# We'd skip, Analysis and Design

height = float(input("Enter height of triangle: "))
base = float(input("Enter base of triangle: "))
area = 0.5 * base * height

print(f"The area of a triangle of height, {height} and base, {base} has an area of {area}")
```

## Practicals

Using the new concept in this exercise and the white space character, newline - `\n` , write a program that accepts from the user, inputs, name, age, sex and hobby. Output a descriptive essay of the values taken.

> Be curious and creative, take as many inputs as possible.

## Summary

* One may use `f"... {}"` to format a string
* `f` - means format
* `{}` allows us to insert values directly into the string

