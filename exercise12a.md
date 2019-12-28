# excercise 12 a (Functions)
A function is simply a block of code, with a unique name and maybe, has some arguments, that performs a specific task. The use of functions prevents one from repeating a particular piece of routine/procedure over and over again.
A function is of the structure:

```python
def function_name():
    # some code

# Assuming we have created this function, we call 
# ( reference this function by calling it by its name 
# followed by the open and close parenthese)
function_name()

```

## Example
Let say we want to ask five users their name and print it some string.

```python
# basically what we'd do is take the user name and print it

some_str = "$$$"

# first person
first_person = input("Enter name: ")
print(first_person + some_str)

# second person
second_person = input("Enter name: ")
print(second_person + some_str)

# third person
third_person = input("Enter name: ")
print(third_person + some_str)

# fourth person
fourth_person = input("Enter name: ")
print(fourth_person + some_str)

# fifth person
fifth_person = input("Enter name: ")
print(fifth_person + some_str)

```

The code above works well, we achieve our goal but we waisted a lot of time rewriting all these for five times. A simple solution would be to use a loop

## Example
```python
# reading and outputting 5 users name using a loop

for i in range(5):
    person_name = input("Enter name: ")
    print(person_name  + some_str)

```

Well this code also works well. Now another approach is the mudular ( functioanl approach).

```python
# create a function to reading and outputting 5 users name
# by calling the function 5 times

def get_and_print_name():
    person_name = input("Enter name: ")
    print(person_name  + some_str)


get_and_print_name()
get_and_print_name()
get_and_print_name()
get_and_print_name()
get_and_print_name()

# well isn't there some repetition here? Yes there is.
# or you can use a loop
for i in range(5):
    get_and_print_name()

```
## Advantage of using a function
* Reduce code redundancy
* It is easier to catch and fix bug in your code
* It can be plugged into another code

## Example
```python
# A program that calculates and prints the area of a triangle taking the 
# base and height as inputs

def calc_area():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    area = 0.5 * base * height

    print(f"The area of a triagle of base, {base} and height, {height} is {area}")

# call the function here
calc_area()

```
