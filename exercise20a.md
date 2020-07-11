# Exercise 20 a (OOP)
OOP stands for Object Oriented Programming. So, with this, style of doing things ( coding), instead of using just variables or and functions, we use them both, bundled together.

Everything in Python is an object. The integers, floats, strings, etc, are all object. Thus they may have some qualities ( properties/attributes) and some functionalities ( methods/behaviours). It is that OOP, is used to mimic real life objects.

## Class

A class is like a blue-print of an object which defines the properties and functionalities of the object. For a real life example, lets think of a human being as an example of a class. A human being, surely has a name, age, address, maybe married thus marital status, color of eyes and hair, complexity and so on. These are the properties ( attributes) of the human being. They describe the human being - 'object'.

Again, a human is capable of doing certain things like talking, sleeping, drinking, jumping, thinking, etc. Humans have functionalities. As an object does something.

> It is a conversion that, our _file name_ for the class, matches the _class name_ for our class object.

## Structure of a class

Minimally, just like we define a function, we start with the `def` keyword followed by the `function_name` then a tuple of arguments or just empty parenthesis. Python has the `class` keyword for defining a class.

> Remember, that indentation matters in Python.

``` Python
# a minimal class that does nothing
# with class_name, Human
# it is a conversion that one begins a class name with an 
# uppercase letter
class Human:
    pass
```

> `pass` is a keyword, we use it when maybe we are not ready to implement a function or class yet

## Constructor

When a class is created, one may like to initialize some data thus pass them to the constructor. The constructor is actually a function that is called when an `instance` of the class is created. It has a special name, `__init__(some_args)` .

``` Python
# a class with a constructor that does nothig
class Human:
    def __init__():
        pass
```

## Properties

A proerty is basically a variable. Yes, the variable that we have discussed in `Exercise 1 ( Creating a variable)` , just that here they belong to a class thus they are referred to as properties of that class.

## Methods

A method is a function of the class. There is only a slight difference. Lets create a class with an attribute, `name` , a `constructor` and a method `say_hello` , that prints `hello {name}` to the screen.

``` Python
# a class with one attribute, name
# a method, say_hello, that prints hello
class Human:

    def __init__(self, name):
        self.name = name

    def say_hello():
        print(f"hello, {self.name}")
```

### Code breakdown

* `class Human:` creates a class with name `Human` 
* `def __init__(self, name)` creates a Constructor and passes a data, which is `name` to it.
* In the constructor block, the data, `name` , was assigned to an attribute of the class `self.name` 
* The `self` here refers to the `class` object itself - `Human` .
* So `self.name` is the same as `Human.name` 
* `self` must always be used as it is a conversion in Python, which means we could use another keyword in place of `self` 

### Note

``` Python
def say_hello(name):
        print(f"hello, {name}")
```

In `say_hello` , we could just pass the name data to it and then print `hello {name}` but we passed the name to the constructor instead. This will make the name attribute accessible everywhere in the class thus we reference it with the `self` keyword, `self.name` .

## Creating an instance of a class

An instance of a class is an object of the class with all the attributes and methods of that class. So the `class Human` may have an instance of say, `John` . If we have a class of `Car` , `Ferrari` is an instance of the class `Car` .

``` Python
# We created a class earlier
# we shall create an instance of that class
# class name is Human, with an attribute, name,
# passed to it's constructor
# and a method, say_hello() that prints hello with the data passed as name.

john = Human('John Doe')
# we passed name into the contructor

# access/call the method
# class_object.method_name() or class_instance.method_name()
john.say_hello()
# output-> hello John Doe

# access the attribute
john.name = "Sandra Doe"
john.say_hello()
# output-> hello Sandra Doe
```

### Note

* Use the dot, `.` operator to access methods and attributes of the class
* Python is case sensitve, thus `human` and `Human` are completely different things
* When a method returns a value, just like a normal function does, we may get the returned value and print it.

## Rectangle class

> create a file, with name `rectangle.py` 

``` Python
# this is a simple is class to model a rectangle
# a rectangle has length and breadth, so we pass
#  the length and breadth to the constructor
# it has a 2 methods that would return the area and perimeter.

class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        """ returns the area as, length * breadth """
        return self.length * self.breadth

    def perimeter(self):
        """ returns the perimeter as, 2 * (length + breadth) """
        return 2 * (self.length + self.breadth)

# instance of the rectangle class
rect_inst = Rectangle(2, 3)  # l = 2, b = 3

# get the area
area = rect_inst.area()

# get the perimeter
perrmeter = rect_inst.perimeter()

print(f"The area and perimeter of the rectangle are, {area} and {perrmeter} respectively")
```

> `""" this is a doc string """` , it is just like a comment.

## Practicals

* Re-write the `Rectangle` class, and check for execptions.
* Write a class for basic mathematical operations, such as addition, subtraction, multiplication, division, floordivision ( aka integer division), modulo ( aka remainder), power, etc
* Write a class for a document statistics. Refer to the `exercise 19` to read about document statistics.
* Write a program that allows creating, reading and updating of the content of a file using OOP.

## Summary

* OOP = Object Oriented Programming
* `class` is the blue print of an object
* classes have `attributes` and `methods` 
* `attribute` is a data/variable
* `method` is a function
* constructor, `__init__(some_args)` , is used to initialize some attributes
* constructors to do not return any value
* say we have class, Human, `jojn = Human()` is an instance of the class
* `class_name().attribute_name` or `class_instance.attribute_name` to access a class attribute
* `class_name().method_name` or `class_instance.method_name` to access a class method

