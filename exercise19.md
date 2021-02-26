# Exercise 19 (Files)

In this exercise, we shall create, read and write into a file. We have been doing this with the `print()` function indirectly - recall `sys.stdout`.

## File modes

A file mode is a privilege that we give to a file object when opening/accessing a file. These modes provide a read-only, write-only, append or read and write privilege when handling files.

| Mode   | Parameter  | Description                                                                                                                                                                                         |
| ------ | :--------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Write  | `w` , `w+` | `w` - write mode. Writes into a file but create the file when the file does not exist or overwrites the file content when the file already exists.<br> `w+` - allows for write and read privileges. |
| Read   | `r` , `r+` | `r` - read mode. Opens file for reading only.<br> `r+` - allows reading and writing privileges.                                                                                                     |
| Append | `a` , `a+` | `a` - append mode. Wite data to the end file.<br> `a+` - create file if file does not exist.                                                                                                        |

## Create a file

Use the open function to create a file. `open(file_name, mode)`

```Python
# creating a file with name helloworld.py
open('helloworld.py', 'w+')

# helloworld.py file will be created in the current working file directory
# if helloworld.py will be overwritten if it already exists
```

## Closing file

After opening, reading and writing to a file, we have to close it.

```Python
# close the file after opening to release resources
file_obj.close()
```

## Open file

After creating the file, a file object is returned.

```Python
# creating a file with name helloworld.py
file_obj = open('helloworld.py', 'w+')
```

### Alternative to open/create a file

Use the `with ... as` clause to `open` and `close` the file. This is mostly preferred.

```Python
# creating a file with name helloworld.py
with open('helloworld.py', 'w+') as file_obj:
    print('file ceated successfully.')
```

## Read from file

Read the content of the file using the file object. Create a sample file, `sample.py` and add the line `# hello world Python` to it. Save the file and close it. Use `read`, `readline` and `readlines` of the file object to read the content of the file.

| File method   | Function                                                                                                   |
| ------------- | ---------------------------------------------------------------------------------------------------------- |
| `read(size)`  | reads entire file content or just some part by passing an `int` argument as size.                          |
| `readline()`  | reads file content line by line and returns one at a go. It moves the pointer to the next line afterwards. |
| `readlines()` | reads the entire file content, line by line as a list.                                                     |

### `read(size)`

```Python
# read file content of sample.py
# sample.py is the file created from above
# else, create a file with name, sample.py
# add the line, # hello world Python

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

```Python
# read file content of sample.py
# a line at a time

print("File content")
print("-------------")

with open('sample.py', 'r') as file_obj:
    line = file_obj.readline()
    print(line)

# this returns a file pointer object
# this pointer is now on the second line after we called readline()
# when we call readline() again, it returns the second line
# then moves the pointer to the next line - the 3rd line
# and so on.. add print(file_obj.readline()) and see for yourself
```

### `readlines`

```Python
# read file content of sample.py
# line by line as a list object

# lets make this more fun
# prompt the user which line should be read
# then print that line

file_content = []

try:
    with open('s.html', 'r') as file_object:
        file_content = file_object.readlines()

    user_input = int(input("Enter line number: "))

    line = file_content[user_input - 1]

    print(user_input, line)
except Exception as e:
    print(f'{e}')
```

What will happen if the user enters a line number that does not exist?

## Write to file

When we print, we write to the screen but in this example, we shall write to a file.

### write method

Use the `write` method to write data into a file.

```Python
# write into file with the write method
with open('samplewrite.txt', 'w+') as write_obj:
    write_obj.write("Hello world")

# add another line to the previous content
# using the append mode
with open('samplewrite.txt', 'a+') as write_obj:
    write_obj.write("I am a Python developer")
```

### print function

Use the `print` function to write data into a file.

```Python
# write into file with the print function
with open('samplewrite.txt', 'w+') as write_obj:
    content = "I remember foo and bar from my little years"
    print(content, file=write_obj)
```

## Example

A program that counts the number of characters on the first line of a file.

```Python
# a program that counts the number of characters on the first line of file.
with open('testsample.py', 'r') as read_obj:
    first_line = read_obj.readline()
    number_chars = "".join(first_line.split(" "))

    print('ws:', len(first_line))
    print('number_chars:', len(number_chars))
```

## Practical

- Write a function that returns the number of lines and characters on each line in the entire file.
- Write a function that returns the document statistics of a given file. The document statistics are the number of lines, number of words, number of characters with space and without space. Lines are separated by newlines, words are separated by spaces.

  ```sample output
  file name
  ---------
  Lines      - 8
  Words      - 71
  Char (ws)  - 403
  Char (wos) - 337
  ```

- Write a program that allows creating, reading and updating of the content of a file.

## Summary

- open file in the `read` , `write` or `append` mode
- use `open(file_name, mode)` to open or create a file
- use `read` , `readline` or `readlines` to read the content of the file
- use `write` or `print(content, file=your_file_object)` to write into files
