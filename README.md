# Group Exercise Lesson 11 - 12

## Instructions

This is probably your first slightly larger program, so you will tackle it as a group exercise. 

- Each team consists of 2-4 members.
- You must use one class `Person` in your code.
- You can use all the examples from previous lessons

### `Exercise 1` Load data from a file

1. Create a file in either csv or json format. It should contain data for at least 5 Persons, you can create it manually or with a script.
2. Each person should have a firstname, lastname, birthdate and address.
3. Read the file and insert it into to a SQLite database.

### `Exercise 2` List all persons stored in the database

*Hint* here is a good place to use the class `Person`. e.g you can create a Person object for each row, and print it with a custom `__str__` method.

1. Create a (SQL) query that gets all rows (select *) from the table
2. Print all rows

### `Exercise 3` Menu

1. Create a menu with options:
   1. Load data from file (Use your solution from Exercise 1)
   2. List all persons (select *) (Use your solution from Exercise 2)
      1. *EXTRA* query the database with firstname
      2. *EXTRA* query the database with lastname
      3. *EXTRA* query the database with birthdate
      4. *EXTRA* query the database with address
   3. Delete a person
   4. *EXTRA* update a persons address

### *EXTRA* *EXTRA* Add another table

Create another table, i.e Vehicles, Friends or Transactions.

1. Add it to your menu
2. Make it possible to add data to the second table
3. Query the database with a join
