# Exercise 20 a (OOP)

OOP stands for Object-Oriented Programming. In this style of doing things (coding), instead of using just variables or and functions, we use them both, bundled together.

Everything in Python is an object. The integers, floats, strings, etc, are all objects. Thus they may have some qualities (properties/attributes) and some functionalities (methods/behaviours). It is that OOP is used to mimic real-life objects. We can create a human object, who happens to have a name, a job, maybe or even, if this human can disassemble and reassemble a system unit. This human can program, sing in the shower, this human can eat and drink. This human has some qualities and can do certain things.

## Class

The "bit" of OOP is a class. A class is the architecture or blueprint of an object. It defines the properties and functionalities of the object. Let's think of a human being as an example of a class. A human being, surely has a name, age, address, maybe this human is married thus marital status, the colour of eyes and hair, complexity and so on. These are the properties (attributes) of the human being. They describe the human being - the 'object'.

Again, a human is capable of doing certain things. Actions such as talking, sleeping, drinking, jumping, thinking, coding, etc. Humans have capabilities. As such an object does something or acts.

> It is a conversion that our _file name_ for the class, matches the _class name_ for our class object.

## Structure of a class

Minimally, just as we defined a function, we started with the `def` keyword, followed by the `function_name` then a tuple of arguments or just empty parenthesis. Did you get the gist of `a tuple of arguments`? Python has the `class` keyword for defining a class.

> Remember, that indentation matters in Python. It is that which defines the block.

```Python
# human.py
# a class that does nothing with class_name, Human
# it is a conversion that one begins a class name with an
# uppercase letter
class Human:
    pass

```

> `human.py` is preferred over `Human.py` as a file name.
> `pass` is a keyword, we use it when maybe we are not ready to implement a function or class yet.

## Constructor

When a class is created, we can initialize some attributes. We pass the data via the constructor. The constructor is a function that is called when an `instance` of the class is created. It has a special name, `__init__(self)`.

```Python
# a class with a constructor
class Human:
    def __init__(self):
        pass

```

## Properties

A property is a variable. Yes, the variable concept that we have discussed in `Exercise 1 (Creating a variable)`, just that here the variable belongs to a class and it is referred to as a property of the class.

Let's initialize a property, `name`, in the constructor and give it a value, `'default name'`. `'default name'` will be shared by all instances of the class.

```Python
# a class with a constructor that does no data passed as a parameter
class Human:
    def __init__(self):
        self.name = "default name"

```

If we want the users to pass their name instead of the default name we have, we will let the user pass a data, as the user's name. We then take then name, passed by the user and assign it to the name attribute of the class.

```Python
# a class with a constructor that does no data passed as a parameter
class Human:
    def __init__(self, name):
        self.name = name

```

We can pass several parameters which means that we can have several attributes. Know when you are overdoing it.

## Methods

A method is a function of a class. We discussed functions in `exercise 12 (Functions) a, b and c`. Refresh and clear some cache if you have to. There is only a slight difference between a method and a function. A method takes `self` as a first parameter.

Let's create a class with an attribute, `name`, a `constructor` and a method `say_hello`, that prints `'hello {name}'` to the screen. We shall pass the `name` data as a parameter to the constructor.

```Python
# a class with one attribute, name
# a method, say_hello, that prints hello name
class Human:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"hello, {self.name}")

```

### Code breakdown

- `class Human:` creates a class with the name `Human`.
- `def __init__(self, name)` creates a Constructor and passes a data, which is `name` to it through the constructor.
- In the constructor block, the data, `name`, was assigned to an attribute of the class `self.name`
- The `self` here refers to the `class` object itself - `Human`.
- So `self.name` is the same as `Human.name`.
- `self` must always be used as the first parameter in a method. It is a conversion in Python. This means that we could use another keyword in place of `self`. Don't do it if you want others to read and understand your code and probably contribute to it.

### Note

In `say_hello`, we could just pass the `name` data to it and then print `hello {name}` but we passed the name to the constructor instead. This will make the name attribute accessible everywhere in the class thus we reference it with the `self` keyword, `self.name`. If we pass the `name` data to the `say_hello` method, we will not have to use `self` to access it.

```Python
class Human:

    def say_hello(self, name):
            print(f"hello, {name}")

```

## Empty or No constructor

Would we have to create a constructor when we won't pass any data to the constructor? Would we create a constructor if we do not want to initialize an attribute?

The answer is quite simple, do not create the constructor at all. The constructor you may be talking about is:

```Python
class Human:
     def __init__(self):
        pass

```

No attribute was initialized nor was data passed via the constructor. The constructor function does nothing. If the constructor does nothing, then do not create it.

## Creating an instance of a class

An instance of a class is an object of the class with all the attributes and methods of that class. So the class `Human` may have an instance, `John`. If we have a class of `Car`, `Ferrari` is an instance of the class `Car`. We created a `Human` class earlier. We shall create an instance of that class.

Class name, `Human`, with an attribute, `name` passed to its constructor and has a method, `say_hello()` that prints hello with the data passed as `name`.

```Python
john = Human('John Doe')
# we passed the name into the constructor

# access/call the method
# class_object.method_name() or class_instance.method_name()
john.say_hello()
# output-> hello John Doe

# access the attribute
john.name = "Sandra Doe"
john.say_hello()
# output-> hello Sandra Doe

```

Where did we pass the argument to the constructor? We passed the argument(s) in the parenthesis when we were creating an instance of the class.

### Note

- Use the dot, `.` operator to access methods and attributes of the class.
- Python is case sensitive, thus `human` and `Human` are completely different.
- When a method returns a value, just like a normal function does, we may get the returned value and print it.

## Rectangle class

> create a file, with the name `rectangle.py`

This is a sample class to model a rectangle. A rectangle, we know has a length and a breadth. We shall pass the length and breadth as data into the constructor. In our case, we are interested in the area and the perimeter of the said rectangle thus we shall create two methods, `area` and `perimeter` to return the area and perimeter of the rectangle.

```Python
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
perimeter = rect_inst.perimeter()

print(
    f"The area and perimeter of the rectangle are, {area} and {perimeter} respectively")

```

> `""" this is a docstring """`, triple quoted string, it is just like a comment.

## Practicals

- Re-write the `Rectangle` class, and check for exceptions. Hint: `int` and `float` values required.
- Write a class for basic mathematical operations, such as addition, subtraction, multiplication, division, floor division ( aka integer division), modulo ( aka remainder) and exponent (power), without using built-in functions.
- Write a class for document statistics. Refer to `exercise 19` to read about document statistics.
- Using a class write a program that allows creating, reading and updating of the content of a file.

## Summary

- OOP = Object Oriented Programming
- `class` is the blue print of an object
- classes have `attributes` and `methods`
- `attribute` is a data/variable
- `method` is a function
- constructor, `__init__(self, some_args)` , is used to initialize some attributes
- constructors to do not return any value
- say we have class, Human, `john = Human()` is an instance of the class
- `class_name().attribute_name` or `class_instance.attribute_name` to access a class attribute
- `class_name().method_name` or `class_instance.method_name` to access a class method
