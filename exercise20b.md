# Exercise 20 b (OOP - Concepts)

There are certain important concepts when it comes to OOP that makes software engineering better and simpler.

> Read the code - relax, that is all there is to it - coding

## OOP Concepts

Some concepts run through OOP in all OO languages:

- Class
- Inheritance
- Polymorphism
- Abstraction
- Encapsulation

> We shall only consider the creation of classes, inheritance and polymorphism.

### Note

These OOP concepts cut across all Object Oriented Programming languages but the implementation is quite different.

## Inheritance

Inheritance allows us to replicate/extend/inherit/modify/use another class' (object's) attributes and methods without having to re-write the whole properties and methods again for the second class. Think about any item/product that has been produced and used over some time now. You realize that there are different versions of the original. So, say there is version 1, 2, 3, and so on. How did version 2, 3, and the others come about? The company developed the v1 and later started v2? or they rather improved on v1 to get v2 then on v2 to get v3? Well, these two are feasible actually, the latter approach is the solution. The latter approach which is improving upon v1 to get v2 and so on works best and save resources.

So v1 grows into v2, and that's an inheritance or something like that is.

### Structure of Inheritance

You should understand that we have two classes and one of these two classes would like to use the attributes and methods of the other class. Let's create an `Animal class` and a `Cat class`, where `Cat` inherits the `Animal`.

```Python
class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age


class Cat:
    pass

```

For one class (the child class) to inherit from another class (the parent class), we pass the name of the parent class, just as we would pass an argument to a function, into a parenthesis before the colon, `:` of the child class.

```Python
class Parent:
    pass


class Child(Parent):
    pass

```

> It is a very good practice to have the classes in separate files. This means that we can have the classes in the same file. When should we separate our classes into separate files?

Let's have a look at the code below,

```Python
# sharing of common functionality using classes

# Super (Parent) class
class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age


# Sub (Child) class of Animal
class Cat(Animal):
    def purr(self):
        print("Purr..!!")


# Another sub (Child) class of Animal
class Dog(Animal):
    def bark(self):
        print("Woof..!!")


# instances of the child classes
will = Cat("Willington", "red", 5)
will.purr()

granny = Dog("Granny B", "green", 3)
granny.bark()

```

> Remember to pass in `self` and reference methods and attributes with `self`

### Example with multiple inheritances

```Python
# there are three class Human, Robot and Hybrid
# Hybrid inherits from Human and Robot

class Human:

    def __init__(self):
        print("I am a Human")

    def normal_wtt(self):
        print("I can behave like a human being")


class Robot:

    def __init__(self):
        print("I am a Robot")

    def super_wtt(self):
        print("I can behave like a machine")


class Hybrid(Human, Robot):

    def __init__(self):
        print("I am a Hybrid")


h = Hybrid()

h.normal_wtt()
h.super_wtt()


# output
# I am a Hybrid
# I can behave like a human being
# I can behave like a machine

```

The `Hybrid` class now has access to the `Human` and `Robot` class.

### `super()` function

Use the `super()` to access the original methods in the base class.

```Python
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

## Polymorphism

The idea of polymorphism is to have many forms. Let's consider an example.

```Python
# parent class
class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}"

```

So say a class extends the `Human` class, there are a lot of ways to say hello, and thus one would like to have a different implementation for different humans.

```Python
# child class - which extends Human
class Engineer(Human):

    # say hello the engineers' way, so we override the say_hello method
    def say_hello(self):
        return f"Hello, {self.name}, I am an Engineer!!"

```

> continuation in exercise 20 c
