# Exercise 20 a (OOP)
OOP stands for Object Oriented Programming. So, with this, style of doing things ( coding), instead of we using just variables or and functions, we bundle (use) the variables and functions together. Everything in python is an object. The integers, floats, strings, etc, is an object. Thus they may have some qualities ( properties/attributes) and functionalities ( methods). It is that OOP, is used to mimic real life objects.

## Class
A class is like a blue print of an object which defines the properties and functionalities of the object. For a real life example, lets think of a human being as an example. A human being, surely has a name, age, address, maybe married thus marital status and so on. You get the idea. These are the properties ( attributes) of the human being, they describe the 'object'. Again, a human is capable of doing certain things like talking, sleeping, drinking, jumping, etc. You get the clue right. An object does something.

## Structure of a class
Minimally, just like we define a function, we start with the `def` keyword followed by the `function_name` the a tuple of argument or just parenthesis. Classes have the `class` keyword.
> Remember, that indentation matters in python.

``` python
# a minimal class that does nothing
# with class_name, Human
# it is a conversion that one begins a class name with an 
# uppercase letter
class Human:
    pass
```

## Constructor
When a class is created, one may like to initialize some data thus passes them to the constructor. The constructor is actually a function that is called when an `instance` of the class is created. It has a special name, `__init__(some_args)` - ( it is a magic method) - Do not worry here. 
``` python
# a class with a constructor that does nothig
class Human:
    def __init__():
        pass
```

## Properties and Methods
A proerty is basically a variable, Yes, the variable that we discussed in `exercise 1`, just that here they belong to a class thus they are reffered to as properties.
A method is a function of the class. There is only a slight difference. Lets create a class with an attribute, name, an constructor and a method say_hello, that prints ( can return) `hello name` to the screen.
``` python
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
* `def __init__(self, name)` creates a Constructor and passes a data, name to it.
* In the constructor block, the data, `name`, was assigned to an attribute of the class `self.name`
* The `self` here refers to the `class` object it self - `Human`.
* `self.name` is the same as `Human.name`

<!-- 
what is a class? lame definition, example of things that can be modelled as class, structure
compare with something - a function

class is like an object in the real world
attributes - metrics, properties
methods - functionality
instances - object
access attributes
access methods
 -->
