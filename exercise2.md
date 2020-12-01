# Exercise 2 ( Data Types)

A data type is basically, the kind of value ( data) a variable can hold or store. Think of data types as the kind of data we use in our program. More technically, a data type dictates the size of memory allocated for a value.

There are generally two types of data written in different forms. We have Numbers and Text (broadly speaking). Have a brief read on [C's data type][cdata-type-size-site] - by the way, Python was implemented in [C][c-site].

For numbers, we have `integer` also know as `int`. We have `float` which is also known as a `float`. Floats are real numbers. For text, we have `string` also known as `str`. A string is a collection of at least zero characters, enclosed ( delimited) in single or double quote.

## Examples

```Python
Eg of int: -3, -5, 2, 58, ...
Eg of float: 1.0, 2.5, -3.000232, ...
Eg of str: "", "John", 'Github', 'Python', "swift Python", '3', '-3.464', '+32-1', ...
```

## Note

- `""` or `''` denote an empty string.
- '2' is not the same as 2. Why? This is because `'2'` is a `string` but `2` is an `integer`. `'2'` is a string because it is enclosed in a quote.
- A string is a text of any characters or just a sentence.
- If we want an output such as, `this is John's car`, then what we have to do is to use double quote. `Eg: "This is John's car"` or we have to escape it. `Eg: 'This is John\'s car'`. We encourage the former.

## When to use `int` or `float`

Use `int` when the value of interest is an integer, a discrete data, such as age, number of people, number of babies, etc. For a value that can be counted, use `int`.

```Python
my_age = 45
number_of_babies = 3

```

Use `float` when the value of interest is a real, a continues value ( a real) such as the weight, height, time, speed, etc. For a value that can be measured, use `float`.

```Python
my_weight = 125.5
pi = 3.14
```

## Type hinting

Python has a way of hinting the type of data passed into a variable. This is done by annotating the variable. It follows this format, `var_name:type=value` . Note that this is not necessarily something we really should do - not compulsory. It will help catch some error though. We the developers ( the team) should decide whether we would like to use it or not. Hardly do I use it.

```Python
age:int = 34
name:str = "Veldora"
weight:float = 120.50
```

## Variable name rules

Consider these whenever we want to create a variable.

- The variable must begin with a letter, `[a - z, A - Z]` or an underscore `_`.
- Followed by any other character(s) such as a letter `[a - z, A - Z]`, numbers `[0 -9]` or an underscore `_`.
- These must exclude any other character since these characters may have special meanings in python.
- Variable names are case sensitive, therefore, `name` and `Name` or any generic of `name` are not the same.
- A variable name must not be a reserved [key words][keyword-list-site].
- [PEP-8][pep-8-site] has more namings.

## Practicals

1. Look into `Exercise 1 ( creating a variable)`, and for the 10 variables we created earlier, state their data types

1. What will be the data type of the following values, `'University of github', 'swift-Python', 100, 12.0, 12, 'B+', '1 + 1', 345.0, 360, 3.1432, "sipping ice cream from a linux cup"`

1. Now create a variable with a suitable name ( the name of the variable should be in a way that describes or gives information about what the value of interest is) `Eg: user_ip = '123.123.100.134' and full_name = 'John Doe'`

## Summary:

- Data type refers to the kind of values we make use of in our program
- The Basic data types we have are the integer (int), float (float) and string (str) but there are also boolean values.
- A string is made up of zero or more characters enclosed in a single and a double quote. `name = ''` is an empty string.
- Use int for counting values and float for measuring or continuous values.
- Once in a while go through [PEP-8][pep-8-site]

#

[cdata-type-size-site]: https://en.wikipedia.org/wiki/C_data_types
[c-site]: https://en.wikipedia.org/wiki/C_(programming_language)
[pep-8-site]: https://www.python.org/dev/peps/pep-0008/
[keyword-list-site]: https://github.com/python/cpython/blob/3.8/Lib/keyword.py

[md2pdf][https://www.markdowntopdf.com/]
