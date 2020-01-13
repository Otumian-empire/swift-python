# Exercise 21 (Modules)

A module is a file (script), containing definitions and statements. This can be any program that you write/wrote and wishes to use that same code without copying and pasting the code into the new script. All you have got to do is to import them.

## Example

Consider the code below, this is taken from `exercise 12 a (Functions)` .

``` python
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

Importing a module is very simple actually, all you need is the `import` keyword and the module name. The module name is the name of the file/script, without the suffix (extension), `.py` 

``` python
import modele_name
```

## Import `area.py` 

To import the `area.py` , and make use of `calc_area` we have to import it.

``` python
import area

# now you may think of this import area like a class
# with some properties and methods
# yes, what you are thinking is right
# the dot notation will work, actually, that's how it would work

area.calc_area()

# refer to this same code in `exercise 12 a (Functions)` 
# you realize that we call the function similar to how we've done here
# just without the module name and this is because the function is in the module
```

## Import objects from a module

Lets assume that there is at least a function in the module and you want to make use of a particular one or all, using the `from` module annotation. Add a function that calculates the perimeter of the triangle, `calc_peri` , to the `area.py` script and rename the module to `triangle.py` .

``` python
from module_name import object_name
```

### Import a particular object

Our goal here is to import `calc_area` from the `triangle` module.

``` python
from triangle import calc_area, calc_peri

# call the calculate area function
calc_area()

# call the calculate perimeter function
calc_peri()
```

### Import all objects

Our goal here is to import all the objects in the module. This can be achieved by using `*` to imply all. With these we have access to all the objects.

``` python
from triangle import *

# call the calculate area function
calc_area()

# call the calculate perimeter function
calc_peri()
```

#### Note

`from module import object` is almost similar to `import module` just that with the latter you have to do `module.object` to make use of the object.

> visit [python doc](www.python.org) to read on the built-in modules and packages

## EXample

``` python
# file name: employee.py
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

You can do, `from module import object as pseudoname` where the object is now pseudoname. This may allow the resolution of conflicting names

``` python
# import employee script
from Employee import Employee as App

print("Employee")

me = App("John Matthew Doe", "Python Developer", 1200.00)
print(f"My name is {me.name} and i am a {me.job}.")
print(f"My salary is {me.salary}.")
print(f"When i work overtime, My salary for the month is {me.return_gross_pay(400)}")
```

## Practicals

* As practice project, write a script, `mathsmodule.py` that performs mathemathical operations such as addition, subtracion, etc. Use a class and create a `test.py` script then import it there. Your `module` should pass these test. Assume that the method names will include, `add, subtr, mult, div, floor_div, pow, mod` . Add comments and then create a new file, `mathsmodule.md` - this can by a `.txt` file too. The documentation, should have information about the developer, what the module is about, how to use the module, how and what to improve, how the methods work and how to use the methods, some errors you expect to occur, some constants that were used, etc. We hope this is becoming clear.

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

* A module is a script that you can reuse in another code - look at the advantages of using a function in `Excercise 12 a (Functions)` 
* use the `import` keyword to bring in a module
* `from module import *` imports all the objects in the module
* `from module import some_objects` import these objects
* `from module import object as obj` imports object given a new name `obj` from module

