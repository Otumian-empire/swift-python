# Exercise 8 (String formatting)

There are a couple of ways to format our output, making our output more readable. We would go with the `f"... {some_value}"` approach known as string interpolation (f-strings).
The `{}` provides the means to insert values into our string as we write it out. `some_value` is the value we pass into the string, whereby `f` means format. The string must begin with the `f` followed by string delimiters (double or single quote).

## Example

```Python
# Consider a simple program to take the users
# name and age and then print them to the screen

name = input("Enter name: ")
age = input("Enter age: ")

print(f"User name: {name}\nUser age: {age}")

# Another sample code
# A program to find the area of a triangle
# The area of a triangle is half the product of the base
# (length) and height of the triangle

height = float(input("Enter height of triangle: "))
base = float(input("Enter base of triangle: "))
area = 0.5 * base * height

print(f"The area of a triangle of height, {height} and base, {base} has an area of {area}")
```

When we have a float, such as, `3.14159` we could round it with the `round(number, digit)` function to `2-decimal` places then print it out.

```Python
pi = 3.14159
rounded_pi = round(pi, 2)
print(f"pi, {pi}, rounded to 2d.p is {rounded_pi}")
```

There is a simple way to do that using f-strings.

```Python
pi = 3.14159
print(f"pi, {pi}, rounded to 2d.p is {pi:.2f}")
```

## Practicals

Using the new concept in this exercise and the white space character, newline - `\n` and one `print` function. Write a program that takes users full name and their favourite number. Print to the screen the string, `<full name> thinks <num / 3> is special`.

Given `<full name>` as, `Daniel` and `<number>` as `23`, print, `Daniel thinks 7.667 is special`. Divide the `<number>` by `3` and round it to 3 decimal places.

## Summary

- One may use `f"... {}"` to format a string
- `f` - means format
- `{}` allows us to insert values directly into the string
