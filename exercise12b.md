# Excercise 12 b (A function that returns a value)

> This is a continuation of `exercise 12 a (A function and its  definition)`

## Function that returns a value

So far, we have written functions that print values to the screen. We can also return a value from a function, assign that value to a variable and make use of it in the future.

### Example 1

Previously when we wrote the `calc_area` function, it prints out a string, detailing the input and the output. Say, we are only interested in the computed result, we can return the computed result using the `return` keyword followed by the computed value. The snippet below is only modified to return the computed by `calc_area`.

```Python
def calc_area(base, height):
    return 0.5 * base * height


# take the base and height from the user
base = float(input("Enter base: "))
height = float(input("Enter height: "))

# call the function here and pass base and height
# to it as the base and height are required
# the value is then assigned to a variable, `area`
area = calc_area(base, height)

# We then make use of the `area`
print(
    f"The area of a triagle of base, {base} and height, {height} is {area}")

```

`calc_area` is now not associated with printing a user-friendly text narrating what input and output were involved. This is left in the hands of the user to decide. This makes it easier to write unit tests for `calc_area` and also import it as a script in other programs.

### Example 2

This is a function that takes a list as an argument and them sorts it from the lowest to the highest. How does this sorting function work?

Say that we are given a list of size, `n` numbers, using two loops, nested actually. The first loop loops through the list `n - 1` times. The second does, `n - 2` times. In the second loop, we check if the first value is greater than the second value. If it is, we `swap` the values and then we compare the second with the third and then the third and fourth and so on until we reach the end of the list. The first loop moves (steps 1) then the process starts again.

```Python
def sort_func(nums):
    """
    This function takes a list as an argument and
    returns a sorted version of it
    """
    n = len(nums)

    for i in range(n):
        for j in range(1, n):
            if nums[j - 1] > nums[j]:
                # swap
                nums[j - 1], nums[j] = nums[j], nums[j - 1]

    return nums


print(sort_func([6, 3, 2, 4, 1]))
print(sort_func(['w', 't', 'a', 'i']))

```

On this line, `nums[j - 1], nums[j] = nums[j], nums[j - 1]`, we swap values here if `nums[j - 1] > nums[j]`. This is a "technique" used for swapping in python without introducing an helping variable.

We could have done,

```Python
temp = nums[j - 1]
nums[j - 1] = nums[j]
nums[j] = temp
```

## Function with many arguments

We have passed single values (data) or a list into our function as arguments so far. Now, say we would like to pass several arguments into a function (we can still use a list - sort of), we are forced to give the function numerous parameters on creation but there is a simple approach in Python.

### Example 3

A function that takes several strings as an argument and returns the number of characters in each argument.

```Python
def many_args(s1, s2, s3, s4, s5):
    print(len(s1))
    print(len(s2))
    print(len(s3))
    print(len(s4))
    print(len(s5))

many_args('sandy', 'jude', 'mani', 'desmond', 'peter')
```

We did it right? No. What if we want to pass a sixth argument? We have to update the `many_args` function. Any other program that has used `many_args` function has to update the number of arguments passed. We don't want that. We should never write such functions. This is an opinion and a style choice.

## `*args` and `**kwargs`

In the next `exercise` we shall discuss more on data structures in python such as list, dictionary, set and tuple into some details. These data structures help in organization and management of data. We came across the word iterable. The previously mentioned data structures also allow iteration.

### list, tuple, set and dictionary in brief

In this context, we are interested in data structures as arguments so these should be enough.

- A list is a comma-separated collection of data delimited by square brackets, `[data1, data2, ...]` where data can be of any data type or data structure. This implies we can have a list that has other lists as data.
- A tuple is just list but is delimited by brackets, `(data1, data2, ...)`
- A set is just like a list but without duplicates, delimited by curly brackets, `{data1, data2, ...}`.
- A dictionary is a key-name pair kind of data structure. So far, list, tuple and set are indexed (enumerated) from 0 to `n`. For a dictionary, we use a key to access a value. `{key1:value2, key2:value2, ...}`. We can loop through the keys, the values and the keys and values. A dictionary is more like a set, with uniqueness in the keys.

### `*args`

We discussed passing multiple data into a function as arguments and we saw some of the limitations.

`*args` means a collection of data, like the list, tuple or set. `*args` is a conversion, whereby the variable name, `args`, is preceded by an asterisk, `*`. It is the `*` that makes the variable a collection of data or an iterable. The number of data in the variable is unspecified. This solves the issue of we had to update the function when we want to pass another data to the function. So `*args`, can be `*some_var_name`. One of the key concepts here is, limiting the number of parameters a function takes. At most four and these four should be named arguments if something like that happens.

#### Example 4

We shall we implement `example 3` but this time using the `*args` concept.

```Python
def many_args(*s):
    for i in s:
        print(i, "=", len(i))


many_args(
    'sandy', 'jude', 'mani', 'desmond', 'peter',
    'sandy', 'jude', 'mani', 'desmond', 'peter',
    'sandy', 'jude', 'mani', 'desmond', 'peter')

```

We were able to pass several arguments to `many_args` but our function just has `*s` as a parameter.

#### Passing a list into a function that takes `*args`

We can also pass a list into `many_args`

```Python
largs = ['candy', 'foo', 'bar', 'swift', 'python',
         'ryder', 'horse', 'rubber-duck', 'pizza']


many_args(largs)
```

But what was the output? Try it out and see. What do you think happened (Look at example 4)? How do we fix this?

#### making a list argument as \*list_arg

This `'candy', 'foo', 'bar', 'swift', 'python', 'ryder', 'horse', 'rubber-duck', 'pizza'] = 9`, was the output from Example 5. What this means is that we passed one argument to `many_args` and this argument is a list of nine strings. We did not pass nine strings as an argument to `many_args`.

To pass a list or tuple as `*args`, we only have to precede the variable name by an asterisk. Try it out and see for yourself.

```Python
many_args(*largs)


# output of *largs
# candy = 5
# foo = 3
# bar = 3
# swift = 5
# python = 6
# ryder = 5
# horse = 5
# rubber-duck = 11
# pizza = 5

```

### \*\*kwarg

`**kwarg` stands for keyword arguments. `**kwarg` is basically `*args`, but we pass keys alongside the values. So the values are accessed by the keys. This is like a dictionary.

#### Example 5

```Python
def many_args(**s):

    for key, value in s.items():
        print(f"{key}: {value}, has {len(value)} chars")


many_args(title="Swift python", author="Otu Michael",
          hobby="Staring at the screen")

```

Now we can access the values passed, with their keys.

#### passing the data as a dictionary

We said lamely, that a dictionary is a key-name pair data structure. Consider the snippet below, where we create a dictionary.

```Python
dict_data = {
    'title': "Swift python",
    'author': "Otu Michael",
    'hobby': "Staring at the screen"
}
```

Let's pass `**dict_data` into many_args

```Python
many_args(**dict_data)

# output
# title: Swift python, has 12 chars
# author: Otu Michael, has 11 chars
# hobby: Staring at the screen, has 21 chars
```

What will happen when `**` is omitted? Try it out. Does add ing a key, solve the issue? What did you notice?

### Default arguments

So what do you think would happen when we don't pass an argument to the function that takes an argument?

Of course an error. We want our functions to function with default data so that the function will assume (use) this value when none is passed.

#### Example 6

Let's make use of the `calc_area` function. We would assign a default value to the parameters.

```Python
def calc_area(base=1, height=1):
    return 0.5 * base * height


# passed no args
print(calc_area())  # 0.5

# passed base but not height
print(calc_area(base=12))  # 0.6

# passed height but not base
print(calc_area(height=14))  # 0.7

```

Here the default parameters are 1.

### Note

- You can do `some_name = func_name` then call, `some_name()` .this will work just like `func_name()`
