import json
import sqlite3
from person_class import Person

def load_data_from_json():
    with open("persons.json") as f:
        data_to_database_executemany = []
        persons = json.load(f)

        for person in persons['persons']:
            data_to_database_executemany.append(tuple(person.values()))

    return data_to_database_executemany

def list_all_persons(conn):
    select_all = "SELECT DISTINCT * FROM person"
    cursor = conn.cursor()
    cursor.execute(select_all)
    rows = cursor.fetchall()

    persons = []
    
    for row in rows:
        person = Person(row[0], row[1], row[2], row[3])
        persons.append(person)
    
    for person in persons:
        print(person.to_string())

    ''' Gamla
    select_all = '''
        #SELECT DISTINCT * FROM person
    '''

    cursor = conn.cursor()
    cursor.execute(select_all)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    '''

def delete_person(conn):
    firstname = input("Enter the first name of the person you want to delete: ")
    lastname = input("Enter the last name of the person you want to delete: ")
    address = input("Enter the address of the person you want to delete: ")

    delete_query = '''
        DELETE FROM person WHERE firstname = ? AND lastname = ? AND address = ?
    '''

    cursor = conn.cursor()
    cursor.execute(delete_query, (firstname, lastname, address))
    conn.commit()

    print(f"Person with first name {firstname}, last name {lastname}, and address {address} has been deleted.")

def update_person_address(conn):
    firstname = input("Enter the first name of the person you want to update: ")
    lastname = input("Enter the last name of the person you want to update: ")
    new_address = input("Enter the new address: ")

    update_query = '''
        UPDATE person SET address = ? WHERE firstname = ? AND lastname = ?
    '''

    cursor = conn.cursor()
    cursor.execute(update_query, (new_address, firstname, lastname))
    conn.commit()

    print(f"Address for person with first name {firstname} and last name {lastname} has been updated.")

def main():
    # Connect to database and create table if it doesn't exist
    with sqlite3.connect('persons.db') as conn:
        create_table_person = '''
            CREATE TABLE IF NOT EXISTS person(
            firstname TEXT,
            lastname TEXT,
            dateofbirth INTEGER,
            address TEXT
            )
            '''

        conn.execute(create_table_person)

        while True:
            print('''\nPlease choose an option:
            1. Load data from JSON file
            2. List all persons
            3. Delete a person
            4. Update a persons address
            5. Quit''')

            choice = input("Enter your choice: ")

            if choice == "1":
                data_to_database_executemany = load_data_from_json()

                # Insert data
                insert_data = '''
                    INSERT INTO person(
                        firstname,
                        lastname,
                        dateofbirth,
                        address
                    ) VALUES (?, ?, ?, ?)
                '''

                conn.executemany(insert_data, data_to_database_executemany)
                conn.commit()

                print("Data inserted successfully!")

            elif choice == "2":
                list_all_persons(conn)

                input("Press enter to go back to menu")

            elif choice == "3":
                delete_person(conn)

            elif choice == "4":
                update_person_address(conn)

            elif choice == "5":
                conn.execute("DROP TABLE IF EXISTS person")
                print("Goodbye!")
                conn.close()
                break

            else:
                print("Invalid choice. Please choose again.")

if __name__ == '__main__':
    main()
