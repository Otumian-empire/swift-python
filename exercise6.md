# Exercise 6 (Input and output)
In this exercise we discuss Input and outputs.

## Input

To take input from the user, we use the `input(prompt)` function. The `prompt` is a string - message, "prompting" the user of what is required of or it could be empty - nothing is passed in the parentheses.

### Note

The value from the `input()` is always a string, so you have to _cast_ it to the desired type.

> Refer to exercise 4 , where we discussed in brief, casting.

### Example

``` python
# prompt user for first name
first_name = input("Enter first name: ")

# first name as we require is already a string so no need to cast
print("First Name: ", first_name)
```

## Output

The `print()` funtion is used to output information on the screen or write into files. This is the print function in full, 
`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)` 

### Parts of the print function

* `*objects: ` these are comma seperated objects you want to display or output. The `*` indicates there is more than one object. `Eg: print('I am', 34, 'years old')` . So we display three objects.

* `sep=' ': ` By default, all the objects `'I am', 34 and  'years old'` are seperated by a single space. We could change it to `# exercise 6 (Input and output))` 

* `end='\n': ` By default, the output from the print function adds `\n` - newline - to the objects so the next print goes to the next line.

* `file=sys.stdout: ` You see, always, your output is displayed ( sent) to the screen, it because of `file=sys.stdout` . This is basically a file and as such could be any other file. So if you want to output data into another file, the you chnage the default value of the `file` to the name of the file object of interest.

* `flush=False: ` By default doesn't forcibly flush the buffer to the screen, and its *False*. Change to *True* to do otherwise.

> Read more on Python Flush [Here](https://stackoverflow.com/questions/15608229/what-does-prints-flush-do) and then [Here](https://www.tutorialspoint.com/How-to-flush-the-internal-buffer-in-Python) or [Google it](https://google.com)

> Make references [Programiz](https://www.programiz.com/python-programming/methods/built-in/print) and [The Pydoc](https://docs.python.org/3.8/tutorial/inputoutput.html?highlight=input)

## Example 1

``` python
# example 1
# all appear on the different lines because, by default, end='\n'
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

Lets write a simple program that takes the name, age and weight of the user then we display the values to the screen
``` python
# A simple program that takes the name, age and weight
# of the user then display the values to the screen

current_year = 2020
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))

# you can write the above line seperately as below
# age = input('Enter your age: ') # age is a string
# age = int(age) # we convert the age to an integer

weight = float(input('Enter your weight in kg: '))

print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age, " - year of Birth:", current_year - age)
# I am subtraction the age, int, from 
# current_year, an int, to get the year of birth
# If we didn't cast the age, then we'd get an error
# Try it and see
```

## Practicals

1. write a program that finds the sum then the average of five numbers, by asking the user to enter then as floats. Display all the inputs, the sum and then the average. [Use descriptive outputs]
1. Write a simple program to simulate an interview for python developers. Display the anwsers in an essay form, with heading, `Your responds` .

## Summary

* Use `input(prompt)` to take input from the *std.in*, `promt` is the message you pass across to the user, as a guide.
* Use `print(objects)` to display comma seperated objects to the screen.
* You have to cast the value of an input to the desire value since by default, it is a string.

