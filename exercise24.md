# Exercise 24 (SQL)
SQL = Structured Query Language.

This, we may say, is the language we shall use to talk to the database. Read more on about databases [here][wiki-what-is-a-bd-site].

All we are interested in is `CRUD` . We want to learn how to create ( insert), read ( select), update and delete data. To continue any further, Download the [SQLite Browser][sqlitebrowser-site]. It makes the work here easier.

## Create a sample table

Lets create a database, `sample.db` , and save it into a folder of any choice, but we recommend the folder in which we have done the practicals in.

Copy and paste this SQL code into windows ( text area) when we click on the `Execute SQL` tab.

``` sql
CREATE TABLE `test_tb` (
	 `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	 `name` TEXT
);
```

## The code above

* This code creates a table with the name, `test_tb` 
* There are two fields in the table, `id` and `name` 
* The `id` field has some properties
    - `INTEGER` - type of data to store
    - `NOT NULL` - the column value must not be empty or null
    - `PRIMARY KEY` - makes every row unique
    - `AUTOINCREMENT` - increase the `PRIMARY KEY` sequentially. Thus we ignore the values for the `id` field because it is `PRIMARY KEY` and `AUTOINCREMENT` 
* The `name` field has only one property, ie.the data type is a `TEXT` 

We shall use this table in this discussion.

## Insert

### Add a row
We may add data ( a row) to the table by inserting.

``` sql
INSERT INTO `test_tb` ( `name` ) VALUES('John Doe')
```

### Add multiple rows

``` SQL
INSERT INTO `test_tb` ( `name` ) VALUES ('Swift Python'), ('kirito'), ('kevin'), ('spit fire')
```

## Read

Reading is done by selecting.

    

### Read all rows and columns

This will read all the data and with all the field displaying.

``` SQL
SELECT * FROM `test_tb` 
```

### Read all rows and a particular column

This will read all the data but display only the `name` field.

``` SQL
SELECT `name` FROM `test_tb` 
```

And this will read all the data but display only the `id` field.

``` SQL
SELECT `id` FROM `test_tb` 
```

### Read rows WHERE some column's value is given (condition)

This will read all the data where the `name` field is equal to `John Doe` 

``` SQL
SELECT * FROM `test_tb` WHERE `name` = 'John Doe'
```

This will read a row whose column (id) value equals 3

``` SQL
SELECT * FROM `test_tb` WHERE `id` = 3
```

This will read a row whose column (id) value greater than 3

``` SQL
SELECT * FROM `test_tb` WHERE `id` > 3
```

## Update

Let us update a row, with `id` = 1 and change the `name` value to `Terry` 

``` sql
UPDATE `test_tb` SET `name` = 'Terry' WHERE `id` = 1
```

## Delete

Delete the row with `id` = 1

``` sql
DELETE FROM `test_tb` WHERE `id` = 1
```

Delete the row with `name` = 'kirito'

``` sql
DELETE FROM `test_tb` WHERE `name` = 'kirito'
```

### Delete all data

Be careful when we do this.

``` sql
DELETE FROM `test_tb
```

## Note

SQL is case insensitive

## Practical

use the DB Browser to create some tables and experiment with it

## Summary

* SQL is the language of the databases
* Inserting, reading, updating and deleting data is feasible

## Resources

* Download [SQLite Browser][sqlitebrowser-site]
* [Corey Schafer SQLite][corey-schafer-utube-site] - Youtube
* [wiki Databases][wiki-what-is-a-bd-site]
* [SQLite][sqlitebrowser-site]
* [w3schools SQL][w3schools-site]

#
[wiki-what-is-a-bd-site]:https://en.wikipedia.org/wiki/Database
[sqlitebrowser-site]:https://sqlitebrowser.org/dl/
[w3schools-site]:https://www.w3schools.com/sql/
[corey-schafer-utube-site]:https://www.youtube.com/watch?v=pd-0G0MigUA
[sqlite-database-tut-site]:https://www.youtube.com/watch?v=zLQ03DeH04c&list=PL-1QdJ8od_eyxntzYQhwCkcVZlqWVrmSf

