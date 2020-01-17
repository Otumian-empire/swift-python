# Exercise 25 (Python SQLite)

In the previous exercise we discussed SQL and used it to write and read the database. In this exercise we shall make use of a built-in database know as `sqlite3` . Read more about [sqlite3][sqlite3-python-site].

## Create database and table with 

We do believe you installed the [SQLite Browser][sqlitebrowser-site]. Go ahead and create a database, `sample.db` and save it into a folder of your choice, we shall use, `Sample` as the folder name.

Create create table using this script.

``` SQL
CREATE TABLE `profile` (
	 `id` 	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	 `name` 	TEXT,
	 `job` 	TEXT,
	 `skill` 	TEXT,
	 `salary` 	INTEGER
);
```

## Connect to database

Before we use the `sqlite3` database, we must first import it, then connect to it.

``` Python
import sqlite3

DATABASE_NAME = 'sample.db'

# create connection
connection = sqlite3.connect(DATABASE_NAME)
```

## Cursor Object

After we create the a connection to the database, we then make use of its cursor object to read and write to the database.

``` Python
# cursor object
cursor = connection.cursor()
```

## Execute

We pass the SQL query and some parameters to the `execute` method after we have created the `cursor` object.

### SQL query

For the SQl query, it is recommended to use pkaceholders instead of passing the actual values directly.

``` Python
# consider some arbituary query

# don't do this
sql_query = "SELECT * some_tb WHERE `some_field` = 2"

# do this instead
sql_query = "SELECT * some_tb WHERE `some_field` = ?"

# the `?` is a placeholder
```

### Fectch

``` Python
# profile -> id:int, name:str, job:str, skill:str, salary:int
# `id` is a primary key and auto increments so we shall ignore it

name = "John Doe"
job = "Software Engineer"
skill = "Python Developer"
salary = 3000

# writing and updating has the same effect of 
# affectting some rows, else rowcount is -1
# reading rather returns an iterable (a row - tuple)
sql_query = "INSERT INTO `profile` ( `name` , `job` , `skill` , `salary` ) VALUES(?, ?, ?, ?)"

# the second argument is of the form, *parameters - remember `*arg` 
# there would be a change in the database thus get the number of affected rows
# with `rowcount` attribute
num_affected_row = cursor.execute(sql_query, name, job, skill, salary).rowcount

# do something if num_affected_row > 0

# consider select query
# for more than one row return, we can use fetchone() to get one row
# and fetchall to return all
sql_query = "SELECT * FROM `profile` "
row_profiles = cursor.execute(sql_query).fetchall()

# do something with row_profiles
```

## Commit

Sure commit here sound familiar, from `exercise 23 (Git)` . Commit mean save/write changes made to the database permanently. Thus after an `insert, update or delete` you have to commit.

``` Python
connetion.commit()
```

## Close cursor and connection

After every thing, we must close the cursor and close the database. This is done so that the database isn't blocked.

``` Python
cursor.close()
connection.close()
```

## Full code

``` Python
import sqlite3

DATABASE_NAME = 'sample.db'

# create connection
connection = sqlite3.connect(DATABASE_NAME)

# cursor object
cursor = connection.cursor()

# profile -> id:int, name:str, job:str, skill:str, salary:int
# `id` is a primary key and auto increments so we shall ignore it

name = "John Doe"
job = "Software Engineer"
skill = "Python Developer"
salary = 3000

# insert/write to database
sql_query = "INSERT INTO `profile` ( `name` , `job` , `skill` , `salary` ) VALUES(?, ?, ?, ?)"

# check if there is a change in the database
num_affected_row = cursor.execute(sql_query, name, job, skill, salary).rowcount

if num_affected_row:
    print("profile written to database successful")
else:
    print("profile writing to database unsuccessful")

# save the changes
connetion.commit()

# close cursor and connection
cursor.close()
connection.close()
```

## Reading

``` Python
import sqlite3

DATABASE_NAME = 'sample.db'

# create connection
connection = sqlite3.connect(DATABASE_NAME)

# cursor object
cursor = connection.cursor()

# read data
sql_query = "SELECT * FROM `profile` "

# check if there is a change in the database
rows = cursor.execute(sql_query).fetchall()

# every row is like a tuple - integer indexed
if rows > 0:
    for row in rows:
        id = row[0]
        name = row[1]
        job = row[3]
        skill = row[4]
        salary = row[5]

        print(f"ID: {id} - {name} is a(n) {job} specialized in {skill} and earns {salary}")
else:
    print("profile writing to database unsuccessful")

# there is no need to commit here as no changes are made to the database

# close cursor and connection
cursor.close()
connection.close()
```

## Practicals

> Use a class if possible

* Write a script that returns the number of characters in the entire file, and the number of characters on each line. Save these two into a database with the name of the file.
* Write a script that returns the document statistics of a give file. The document statistics are number of lines, number of words number of characters with space and witout space.

    ``` 
    file name
    ---------
    Lines      - 8
    Words      - 71
    Char (ws)  - 403
    Char (wos) - 337
    ```

    Write these into a database

* Write a scripts that backs the content of a file up. Save the back up in the database.

## Summary

The concept or steps behind the use of `sqlite3` is quite simple.

* `sqlite3` is a built-in light weight database
* `connect` to the database
* create a `cursor` object
* `execute` some queries
* `commit` the changes
* `close` cursor and connection

#
[sqlite3-python-site]:https://docs.python.org/3.7/library/sqlite3.html
[sqlitebrowser-site]:https://sqlitebrowser.org/dl/

