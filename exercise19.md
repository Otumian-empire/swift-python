# Exercise 19 (Files)
In this exercise we create, read and write into a file, which we have actually been doing with the `print` function in directly - recall `sys.stdout` .

## File modes

File mode is basically the privilege which you give to the file object when opening/accessing a file. This modes provides a read only, write only, append or read and wite privileges when handling files.
| Mode  | parameter | description |
| ----  | --------- | ----------- |
| Write | `w` , `w+` | `w` - write mode. Write into file but create file when file does not exist or overwrite the content when file already exist. `w+` allows for write and read privileges.|
| Read  | `r` , `r+` | `r` - read mode. Opens file for reading only. `r+` - allows reading and writing privileges.|
| Append| `a` , `a+` | `a` - append mode. Wite data to the end file. `a+` - create file if file does not exist.|

## Create file

Use the open function to create a file. `open(file_name, mode)` 

``` python
# creating a file with name helloworld.py
open('helloworld.py', 'w+')

# helloworld.py file will be created in the current working file directory
```

## Open file

After creating the file, a file object is returned.

``` python
# creating a file with name helloworld.py
file_obj = open('helloworld.py', 'w+')

# close the file after opening to release resources
file_obj.close()
```

## Alternative to open file

Use the `with ... as` clause to `open` and `close` the file. This is mostly peferred - but do as you please and do it right.

``` python
# creating a file with name helloworld.py
with open('helloworld.py', 'w+') as file_obj:
    print('file ceated successfully.')

# notice we didn't use file_obj.close()
```

## Read from file

Read the content of the file using the file object. Create a sample file, `sample.py` and add the line `# hello world python` to it. Save the file and close it. Use `read` , `readline` and `readlines` of the file object to read the content of the file.

| file method | function |
| ----------- | -------- |
| `read(size)` | reads entire file content or just some part by passing an `int` argument as size.|
| `readline()` | reads file content line by line. It moves the pointer to the next line after wards.|
| `readlines()` | reads the entire file content, line by line as a list.|

### `read(size)` 

``` python
# read file content of sample.py
# sample.py is the file created from above
# else, create a file with name, sample.py
# add the line, # hello world python

with open('sample.py', 'r') as file_obj:
    content = file_obj.read()
    print("File content")
    print("-------------")
    print(content)

# or go with the open and close
file_object = open('sample.py', 'r')
content = file_obj.read()
print("File content")
print("-------------")
print(content)
file_obj.close()
```

### `readline` 

``` python
# read file content of sample.py
# a line at a time

print("File content")
print("-------------")

with open('sample.py', 'r') as file_obj:
    line = file_obj.readline()
    print(line)

# this returns a file pointer object
# this pointer is now on the second line after we called readline()
# when you call readline() again, it returns the second line
# then moves the pointer to the next line - the 3rd line
# and so on.. add print(file_obj.readline()) and see for yourself
```

### `readlines` 

``` python
# read file content of sample.py
# line by line as a list object

# lets make this more fun
# prompt the user for the number of lines there is in the file
# prompt the user which line should be read
# then print the line

file_content = []

with open('sample.py', 'r') as file_object:
    file_content = file_object.readlines()

user_input = int(input("Enter line: "))

line = file_content[user_input - 1]

print(user_input, line)

# a very short version which we believe is hard to read
# thus as much as you can, try to make your code more readable
with open('sample.py', 'r') as file_object:
    print(file_object.readlines()[int(input("Enter line: ")) - 1])

# unhealthy man
print(open('sample.py', 'r').readlines()[int(input("Enter line: ")) - 1])
```

## Write to file

When we print, we write to the screen but in this example we shall write to a file.

### write method

Use the `write` method to write data into file.

``` python
# write into file with the write method
with open('samplewrite.txt', 'w+') as write_obj:
    write_obj.write("Hello world")

# add another line to the previous content
# using the append mode
with open('samplewrite.txt', 'a+') as write_obj:
    write_obj.write("I am a python developer")
```

### print function

Use the `print` function to write data into file.

``` python
# write into file with the print function
with open('samplewrite.txt', 'w+') as write_obj:
    content = "I remember foo and bar from my little years"
    print(content, file=write_obj)
```

## Example

A program that counts the number of characters on the first line of file with and without spaces.

``` python
# a program that counts the number of characters on the first line of file.
with open('testsample.py', 'r') as read_obj:
    first_line = read_obj.readline()
    no_ws = "".join(first_line.split(" "))

    print('ws:', len(first_line))
    print('no_ws:', len(no_ws))
```

## Practical

* Write a function that returns the number of characters in the entire file, and the number of characters on each line.
* Write a function that returns the document statistics of a give file. The document statistics are number of lines, number of words number of characters with space and witout space.

    ```sample output
    file name
    ---------
    Lines      - 8
    Words      - 71
    Char (ws)  - 403
    Char (wos) - 337
    ```

* Write a program that allows creating, reading and updating of the content of a file.

## Summary

* file made be opened with the `read` , `write` or `append` mode
* use `open(file_name, mode)` to open or create
* use read, readline or readlines to read the content of the file
* use `write` or `print(content, file=your_file_object)` to write into files

