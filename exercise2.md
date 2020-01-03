# Exercise 2 (Data types)
As the name clearly tells, a data type is basically what kind of value a variable can hold or store ( also you may think of them as the kind of data you use in your program). More technically, a data type dictates the size of memory to be allocated for a value.
There are basically two types of data which are written in different forms. We have Numbers and Text (broadly speaking). For the numbers we have `integer` also know as `int` and we have `float` which is also know as a float. Floats are basically decimal numbers.
For the Text we have `string` s also known as `str` .
A string is a collection of at least a character, enclosed in single or double quote.

## Examples

``` python
Eg of int: -3, -5, 2, 58, ...
Eg of float: 1.0, 2.5, -3.000232, ...
Eg of str: "John", 'Github', 'Python', "swift python", '3', '-3.464', '+32-1', ...
```

## Note

* '2' is not the same as 2. Why? this is because '2' is a `string` and 2 is an `integer` .'2' is a string because it is enclosed in a quote.
* A string is basically a text of any characters or just a sentence
* If you want an output say, this is mashude's car.the what you have to do is to use double quote. `Eg: "Mashude's car"` or you have to escape it. `Eg: 'Mashude\'s car'` . We encourage the former.

## When to use int or float

Use int when the value of ineterst is a number and a discrete data, such as age, number of people, number of babies, etc.

``` python 
# Examples
my_age = 45
number_of_babies = 3
``` 

Any value that can be counted, use int. Use float when the value of interest is a number but is a continues value ( a real or decimal value) such as the weight, heaight, time, speed, etc. Any value that can be measured, use flaot.

``` python
# Examples
my_weight = 125.5
pi = 3.14
```

## Practicals

1. look into exercise 1, and for the 10 varaibles you created earlier, state their data types

1. what will be the data type of the following values, 'University of github', 'swift-python', 100, 12.0, 12, 'B+', '1 + 1', 345.0, 360, 3.1432, "sipping ice cream from a linux cup"

1. Now create a variable with a suitable name (the name of the variable should be in a way that describes or gives an information about the value of interest) `Eg: user_ip = '123.123.100.134' and user_name = 'John Doe'` 

## Summary:

* Data type refers to the kind of values you make use of in your program
* The Basic data types we have are the integer (int), float (float) and string (str) but there are also boolean values.
* A string made up of zero or more charaters enclosed in a single and a double quote. `name = ''` is an empty string.
* Use int for counting values and float for measuring or continous values.

