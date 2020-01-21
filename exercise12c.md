# Excercise 12 c (Functions)

> This is a continuation of `excercise 12 b (Functions)` 

## Function with many arguments

Some time we would like to pass plenty argument into a function and thus one is forced to give the function numerous parameters on creation but there is a very simple approach in Python.

### Example

``` Python
# A function the takes a number of strings as argument and returns their length

def many_args(s1, s2, s3, s4, s5):
    print(len(s1))
    print(len(s2))
    print(len(s3))
    print(len(s4))
    print(len(s5))

many_args('sandy', 'jude', 'mani', 'desmond', 'peter')

# what the heck, what if there were about 1000's of args?

# better version is to use the tuple argument, *arg_name - the takeaway is `*` 
# all the argument passed is seen as a tuple object thus iteration is feasible

def many_args(*s):
    for i in s:
        print(len(i))

many_args('sandy', 'jude', 'mani', 'desmond', 'peter', 'sandy', 'jude', 'mani', 'desmond', 'peter', 'sandy', 'jude', 'mani', 'desmond', 'peter')

```

### Note

* You can do `some_name = func_name` then do, `some_name()` .this will work just like `func_name()` 

## Practicals

* Given a list, whose elements are also list ( talking about nested list), write a function that sorts this list and it list elements if possible

## Summary

* A function is simply a block of code than can be called and arguments be passed to it
* function definition 

    ```Python
    def function_name(some_args):
        # some code
    ``` 

* we can call the function by doing `func_name(some_args)` 
* A function allows resue of code
* A function can be used in any part of our code
* paramter are passed into the function when creating the function
* argument is what we pass to the function when we are calling it
* `return` exits a function and returns a value from the function
* use the *arg - tuple argument to collect more arguments
* A function may be called as many times as possible

