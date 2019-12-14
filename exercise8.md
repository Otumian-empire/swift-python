# exercise 8 (String formatting)
There are a lot of ways to format your output which makes manipulation of your output more readable. We'd go with the `f"... {}"` approach.
The `{}` provides the means to insert values into your string as you write it out, and the `f` means format.

# Example

```python
# Consider a simple program to take the users
# name and age and then output them to the screen

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

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

# Practicals
Using the new concept in this exercise and the white white space character, `\n`, write a program that accepts from the user, inputs, name, age, sex and hobby. Output a descriptive essay of the values you have taken.
> You extend this and take as many inputs as possible.


# Summary
* One may use `f"... {}"` to format a string
* `f` - means format
* `{}` allows you to insert values directly into the string