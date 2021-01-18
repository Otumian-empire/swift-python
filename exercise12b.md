# Excercise 12 b (Functions)

> This is a continuation of `excercise 12 a (Functions)`

## Function that returns a value

Sometimes, we may want a value from a function to make use of it in one way or another. To achieve this we return the value rather than printing it out in the function.

### Example 1

Previously when we wrote the `calc_area` function, it prints out a string, detailing the input and the output. We are only interested in the return value (the computed result). The snippet below is only modofied to return the computed.

```Python
def calc_area(base, height):
    return 0.5 * base * height


# take the base and height from the user
base = float(input("Enter base: "))
height = float(input("Enter height: "))

# call the function here, and pass base and height
# to it as the base and height needed
area = calc_area(base, height)

print(
    f"The area of a triagle of base, {base} and height, {height} is {area}")

```

`calc_area` is now not associated with printing a user friendly text narrating what input and output was involved. This is left in the hands of the user to. This makes it easier to write unittests for `calc_area` and also import it as a script in other programs.

### Example 2

This is a function that takes a list as an argument and them sorts it from the lowest to the highest. How does this sorting function works? Say that we are given a list of size, `n` numbers, using two loops, nested actually. The first loop, loops through the list `n - 1` times. The second does, `n - 2` times. In the second loop we check if the the first value is greater than the second value. If it is, we `swap` the values and then we compare the second with the third and then the third and fourth and so on until we reacch the end of the list. Then the first loop moves (steps 1) then the sequence begins again.

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

On this line, `nums[j - 1], nums[j] = nums[j], nums[j - 1]`, we swap values here. This is a "technique" used for swapping in python without introducing an helping variable.

We could have done,

```Python
temp = nums[j - 1]
nums[j - 1] = nums[j]
nums[j] = temp
```

## Function with many arguments

Say we would like to pass several arguments into a function, we are forced to give the function numerous parameters on creation but there is a simple approach in Python.

### Example 3

A function the takes a number of strings as argument and returns the number characters in each argument.

```Python
def many_args(s1, s2, s3, s4, s5):
    print(len(s1))
    print(len(s2))
    print(len(s3))
    print(len(s4))
    print(len(s5))

many_args('sandy', 'jude', 'mani', 'desmond', 'peter')
```

We did it right? No. What if we want to pass a sixth argument? We have to update the `many_args` function. Any other program that has used `many_args` function has to update the number of arguments passed. We don't want that. In fact, we should never write such functions. This is an opinion and a style choice.

## \*params

```Python
# what the heck, what if there were about 1000's of args?

# better version is to use the tuple argument, *arg_name - the takeaway is `*`
# all the argument passed is seen as a tuple object thus iteration is feasible


def many_args(*s):
    for i in s:
        print(i, "=", len(i))


many_args(
    'sandy', 'jude', 'mani', 'desmond', 'peter',
    'sandy', 'jude', 'mani', 'desmond', 'peter',
    'sandy', 'jude', 'mani', 'desmond', 'peter')

```

In the above code, we used `*s` to denote a tuple (collection) of arguments.

### Note

- You can do `some_name = func_name` then do, `some_name()` .this will work just like `func_name()`
