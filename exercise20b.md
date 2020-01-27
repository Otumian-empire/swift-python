# Exercise 20 b (OOP - Concepts)
There are certain important concepts when it comes to OOP that makes software engineering better and simpler.

> Read the code - relax, that is all there is to it - coding

## OOP Concepts

There are some concepts that runs through OOP in all OO languages:

* Class
* Inheritance
* Polymorphism
* Abstraction  
* Encapsulation

> OOP in Python is basically creation of classes and inheritance.

### Note

These OOP concepts cuts across all Object Oriented Programming languages but the implementation is quite different.

## Inheritance

Inheritance allows us to replicate/extend/inherit/modify/use another class' (object's) attributes and methods without having to re-write the whole properties and methods again for the second class. So think about any item/product that has been produced and used over some time now. You realize that there are actually different versions of the original. So, say there is version 1, 2, 3, and so on. How do we think version 2, 3, and the others came about? The company developed the v1 and later started v2? or they rather improved on v1 to get v2 then on v2 to get v3? Well, these two are feasible actually, the latter approach is the solution. The latter approach which is improving upon v1 to get v2 and so on works best.

So v1 grows into v2, and thats inheritance or something like that is.

### Structure of Inheritance

Just understand that we basically have two classes and one of these two classes would like to use the attributes and methods of the other class. Lets create an `Animal class` and a `Cat class` , where `Cat` inherits the `Animal` .

``` Python
class Animal:
	def __init__(self, name, color, age):
		self.name = name
		self.color = color
		self.age = age

class Cat:
	pass
```

For one class (the child class)  to inherit from another class (the parent class), we pass the name of the parent class, just as we would pass an argument to a function, into a parenthesis before the colon, `:` .

``` Python
class Parent:
	pass

class Child(Parent):
	pass
```

> It is a very good practice to have the classes in seperate files

Lets have a look at the code below, 

``` Python
# sharing of common functionanlity using classes

# Super (Parent) class
class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

# Sub (Child) classes

class Cat(Animal):
    def purr(self):
        print("Purr..!!")

class Dog(Animal):
    def bark(self):
        print("Woof..!!")

# instances of the child classes
skull = Cat("Skull Crusher", "red", 5)
skull.purr()

granny = Dog("Granny Hairy", "green", 3)
granny.bark()
```

> Remember to pass in `self` and reference methods and attributes with `self` 

## Example with multiple inheritance

``` Python
# there are three class
# Human, Robot and Hybrid
# Hybrid inherits froms

class Human:

    def__init__(self):
        print("I am a Human")
        
class Robot:

    def __init__(self):
        print("I am a Robot")

class Hybrid(Human, Robot):

    def __init__(self):
        print("I am a Hybrid")
```

## `super()` function

Use the `super()` to access the original methods in the base class.

``` Python
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def number_of_legs(self):
        return self.legs

    def color_of_obj(self):
        return self.color

    def run(self):
        print(f"I have {self.number_of_legs()} legs")
        print(f"I am {self.color_of_obj()} in complexion")

class Tiger (Cat):
    def __init__(self, color, legs, is_big):
        # to have the same functionality as the base class
        # pass the color and legs data to the constructor of
        # the super class. In this way we can modify the 
        # constructor method of the child class to match 
        # the parent class
        super().__init__(color, legs)
        # this saves us from doing
        # self.color = color
        # self.legs = legs
        self.is_big = is_big

    def run(self):
        # call the original run methods of the base class
        super().run()
        print("I have enormous claws for sprinting")

felix = Cat("yellow", 6)
felix.run()

tiger = Tiger("green", 5, True)
tiger.run()
```

> continuation in exercise 20 c

