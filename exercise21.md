# Exercise 21 (Modules)
A module is a file (script), containing definitions and statements. This can be any program that we write/wrote and hope to use that same code without copying and pasting the code into the new script. All we have to do is to `import` them.

## Example

Consider the code below, this is taken from `exercise 12 a (Functions)` .

``` Python
# file name: area.py
# description:
#   A program that calculates and prints the area of a triangle 
#   taking the base and height as inputs

def calc_area():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))

    area = 0.5 * base * height

    print(f"The area of a triagle of base, {base} and height, {height} is {area}")
```

## Import a module

Importing a module is very simple actually, all we need is the `import` keyword and the module name. The module name is the name of the file/script, without the suffix (extension), `.py` 

``` Python
import modele_name
```

## Import `area.py` 

To import the `area.py` , and make use of `calc_area` we have to import it.

``` Python
import area

# think of this `import area` like a class
# with some properties and methods
# the dot notation will work, actually, that's how it would work

area.calc_area()

# refer to this same code in `exercise 12 a (Functions)` 
# we called the function similar to how we've done here
# just without the module name and this is because the function is in the module
```

## Import objects from a module

Lets assume that there is at least a function in the module and we want to make use of a particular one or all, using the `from module` annotation.

Add a function that calculates the perimeter of the triangle, `calc_peri` , to the `area.py` script and rename the module to `triangle.py` .

``` Python
from module_name import object_name
```

### Import a particular object

Our goal here is to import `calc_area` and `calc_peri` from the `triangle` module.

``` Python
from triangle import calc_area, calc_peri

# call the calculate area function
calc_area()

# call the calculate perimeter function
calc_peri()
```

### Import all objects

Our goal here is to import all the objects in the module. This can be achieved by using `*` to imply all. With these we have access to all the objects.

``` Python
from triangle import *

# call the calculate area function
calc_area()

# call the calculate perimeter function
calc_peri()
```

#### Note

`from module import object` is almost similar to `import module` just that with the latter we have to do `module.object` to make use of the object.

> visit [Python doc][python-site] to read on the built-in modules and packages

## Math module

The math module contains some  mathetical functions algebra, logarithm, trignometry, some constants and others.

Lets make use of pi, e, gcd, exp, factorial, pow, sqrt, cos, sin.

> pi and e are constants and the rest are functions.

We are going to import a lot of things from the math module thus to keep it structured we shall group them as tuples  though it will work fine anyways.

``` Python
# import objects from the math lib
# making use of some constants such as `pi` and `e` ,
# some trig function like the cosine and sine
# and other functions

from math import (
    pi, e,
    cos, sin, tan,
    sqrt, pow, exp,
    gcd, factorial
)

# pi and e

# area of a circle = pi times radius square
radius = 7  # cm
# area = pi * radius ** 2
# area = pi * radius * radius
area = pi * pow(radius, 2)

print(f"The area of the circle of radius, {radius} is {round(area,2)}cm^2")

print(end='\n\n')

# e(n) for some integer `n` , is the same as e ** n, pow(e, n) and e * e * ...n
# lets check if they are actually
if e * e == pow(e, 2) == e ** 2:
    print("Cool, e ** n, pow(e, n) and e * e * ...n are all the same")
else:
    print("Sorry, they are not the same")

print(end='\n\n')

# cos, sin and tan
# given that theta is 60 degree
theta = 60  # degree
print(f"Trig table for degree, {theta}")
print("-------------------------")
print(f"cos({theta}) {cos(theta)}")
print(f"sin({theta}) {sin(theta)}")
print(f"tan({theta}) {tan(theta)}")

print(end='\n\n')

# gcd and factorial
# we shall roughly make use of type hinting

# gcd of 81 and 72
first_int: int = 81
second_int: int = 72
gcd_int: int = gcd(first_int, second_int)

print(f"the gcd  of {first_int} and {second_int} is {gcd_int}")

# the factorial of gcd_int
fact_int: int = factorial(gcd_int)
print(f"The factorial, {gcd_int}!, is {fact_int}")

```

## More example

``` Python
# file name: employee.py
# calculating the gross pay

class Employee:

    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

        # some constants
        self.WORKING_DAYS_IN_A_MONTH = 30
        self.WORKING_HOURS_IN_A_DAY = 12
        self.PAY_RATE = 0.25

        # the total number of hours the employee should have done in a whole month
        self.WORKED_HOURS = self.WORKING_HOURS_IN_A_DAY * self.WORKING_DAYS_IN_A_MONTH

    # calculate the gross pay based on the time employee did for the whole month
    # the hours here is the total hours that the employee has overworked
    def return_gross_pay(self, hours):
        gross_pay = 0

        if hours > self.WORKED_HOURS:
            over_time = hours - self.WORKED_HOURS
            over_time_pay = over_time + (self.salary * self.PAY_RATE)

            gross_pay = self.salary + over_time_pay
        else:
            gross_pay = self.salary

        return gross_pay
```

### Note

We can do, `from module import object as pseudoname` where the object is now pseudoname. This may allow the resolution of conflicting names

``` Python
# import employee script
from Employee import Employee as App

print("Employee")

me = App("John Matthew Doe", "Python Developer", 1200.00)
print(f"My name is {me.name} and i am a {me.job}.")
print(f"My salary is {me.salary}.")
print(f"When i work overtime, My salary for the month is {me.return_gross_pay(400)}")
```

Or

``` Python
from triangle import calc_area as area, calc_peri as perimeter

# call area
area()

# call perimeter
perimeter()
```

## Practicals

* As practice project, write a script, `mathsmodule.py` that performs mathemathical operations such as addition, subtracion, etc. Use a class and create a `test.py` script then import it there. Our `module` should pass these test.<br>Assume that the method names will include, `add, subtr, mult, div, floor_div, pow, mod` . Add comments and then create a new file, `mathsmodule.md` - this can by a `.txt` file too. The documentation, should have information about the developer, what the module is about, how to use the module, how and what to improve, how the methods work and how to use the methods, some errors we expect to occur, some constants that were used, etc. We hope this is becoming clear.

    - test add
        - add(1,2) = 10
        - add(1,-2) = -1
        - add(1,2,3,4) = 10

    - test subtr
        - subtr(1,2) = -1
        - subtr(1,-2) = 3

    - test mult
        - add(1,2) = 2
        - add(1,-2) = -2
        - add(1,2,4) = 8

    - test div
        - div(1,2) = 0.5
        - div(1,-2) = -0.5
        - div(5, 0) = None

    - test floor_div
        - floor_div(1,2) = 10
        - floor_div(1,-2) = -1
        - floor_div(1,2,3,4) = 10

    - test pow
        - pow(1,2) = 1
        - pow(2,3) = 8
        - pow(2,-2) = 0.25

    - test mod
        - mod(1,2) = 1
        - mod(22,7) = 1

* For a second version of this program, let a method take 3 args, operator, first_operand, second_operand. Instead of calling any of the methods such as add, just call, `evaluate` with arguments such as `evaluate('+', 2, 5)` to return 7. This should work even if the second and third arguments are in a form of strings such as `evaluate('+', '2', '5')` .

* For a third version, instead of the symbols, such as using, `+` , use `add` instead. Thus `evaluate(+, 2, 5)` , `evaluate('+', '2', '5')` and `evaluate('add', 2, 5)` or `evaluate('add', '2', '5')` works the same.

## Summary

* A module is a script that we can reuse in another code - look at the advantages of using a function in `Excercise 12 a (Functions)` 
* use the `import` keyword to bring in a module
* `from module import *` imports all the objects in the module
* `from module import some_objects` import these objects
* `from module import object as obj` imports object given a new name `obj` from module

#
[python-site]:https://www.Python.org

