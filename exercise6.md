# Exercise 6 (Input and output)

We shall discuss in this exercise, Inputs and outputs.

## Input

To take input from the user, we use the `input(prompt)` function. The `prompt` is a string, a message we to the user, as instructions.

### Note

The value from the `input()` is always a string, so we have to _cast_ it to the desired type.

> Refer to `Exercise 4 ( Arithmetic Operators) - Casting`, where we discussed in brief, casting.

### Example

```Python
# prompt user for the user's first name
first_name = input("Enter first name: ")

# first name as we require is already a string so no need to cast
print("First Name:", first_name)
# print(f"First Name: {first_name}")
```

## Output

The `print()` funtion is used to output information on the screen or write into files. This is the print function in full,
`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

### Parts of the print function

- `*objects: ` these are comma-separated objects we want to display or output. The `*` indicates there is more than one object. `Eg: print('I am', 34, 'years old')` . So we display three objects.

- `sep=' ': ` By default, all the objects `'I am', 34 and 'years old'` are separated by a single space. We could change it to any character we desire, passing `sep=desired_character`. `Eg: print('I am', 34, 'years old', sep=":)")` and the output, `I am:)34:)years old`. **Try it yourself and see**.

- `end='\n': ` By default, `print` adds a newline after the output. `Eg: print('I am', 34, 'years old', end=";")`. This ends every `print` statement with a `;`.

- `file=sys.stdout: ` We see, always that, our output is displayed (sent) to the screen, which is the standard output. `file` is set to `sys.stdout` by default. `sys.stdout` is a file and as such we pass could any other file. So if we want to output data into another file, then we change the default value of `file` to the name of the file object of interest.

- `flush=False: ` By default doesn't forcibly flush the buffer to the screen, and its _False_. Change to _True_ to do otherwise.

> Read more on Python Flush [Here][flush-resource-site-1] and then [Here][flush-resource-site-2] or [Google it][google-site]

> Make references at [Programiz][programiz-site] and [The Pydoc][pydoc-site]

## Example 1

```Python
# example 1
# all of these strings appear on the different lines because, by default, end='\n'
print("hello")
print("world")

# we make end='' - an empty string
print('John', end='')

# the next object after this print would be on the same line as this
print(' Doe')

# so when we set, `end=' - GVR\n'` , then the object will end with
# the string, ` - GVR` then add a newline.
print('Hello world', end=' - GVR\n')

# print() - without any object would print a newline instead
```

## Example 2

Let us write a simple program that takes the name, age and weight of the user then we display the values to the screen.

```Python
# A simple program that takes the name, age and weight
# of the user then display the values to the screen

current_year = 2020
first_name = input('Enter our first name: ')
last_name = input('Enter our last name: ')
age = int(input('Enter our age: '))

# we can write the above line seperately as below
# age = input('Enter our age: ') # age is a string
# age = int(age) # we convert the age to an integer

weight = float(input('Enter our weight in kg: '))

print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age, " - year of Birth:", current_year - age)
# I am subtractingand the age, int, from
# current_year, an int, to get the year of birth
# If we didn't cast the age, then we'd get an error
# Try it and see
```

## Practicals

1. write a program that finds the Sum and the average of five numbers, by asking the user to enter then as floats. Display all the inputs, the Sum and the average. [Use descriptive outputs]

## Summary

- Use `input(prompt)` to take input from the _std.in_, `prompt` is the message we pass across to the user, as a guide.
- Use `print(objects)` to display comma-separated objects to the screen.
- We have to cast the value of an input to the desired value since, by default, it is a string.

#

[flush-resource-site-1](https://stackoverflow.com/questions/15608229/what-does-prints-flush-do)
[flush-resource-site-2](https://www.tutorialspoint.com/How-to-flush-the-internal-buffer-in-Python)
[google-site](https://google.com)
[Programiz-site](https://www.programiz.com/Python-programming/methods/built-in/print)
[pydoc-site](https://docs.Python.org/3.8/tutorial/inputoutput.html?highlight=input)
