# Excercise 12 a (Functions)
A function is simply a block of code, with a unique name and maybe, takes some arguments ( data), that performs a specific task ( computing on the data). The use of functions prevents one from repeating a particular piece of routine/procedure over and over again. 

## Structure a function

``` Python
def function_name():
    # some code
```

## Example

``` Python
# Let say we want to ask five users their name and print it with some string.
some_str = "$"

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

The code above works well, we achieved our goal but we waisted a lot of time rewriting all these for five times. A simple solution would be to use a loop.

## Example

``` Python
# reading and outputting 5 users name using a loop
for i in range(5):
    person_name = input("Enter name: ")
    print(person_name  + some_str)
```

Well, this code also works well. The problem is that, what if we don't want it `n` times any more but we want it when we need it? 

Now another approach is the mudular ( functioanl) approach.

``` Python
# create a function to read and output 5 users name
# by calling the function 5 times

def get_and_print_name():
    person_name = input("Enter name: ")
    print(person_name  + some_str)

# to make this function work, we have to call it 
# just like we do to variables
# but here we add `()` to it.

get_and_print_name()
get_and_print_name()
get_and_print_name()
get_and_print_name()
get_and_print_name()

# well isn't there some repetition here? Yes there is.
# or we can use a loop

for i in range(5):
    get_and_print_name()
```

## Advantage of using a function

* Reduce code redundancy
* It is easier to catch and fix bug in our code
* It can be plugged into another code

## Example

``` Python
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

