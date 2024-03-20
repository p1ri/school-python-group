import json
import sqlite3
from person_class import Person

with open("persons.json") as f:
    data_to_database_executemany = []
    persons = json.load(f)

    for person in persons['persons']:
        data_to_database_executemany.append(tuple(person.values()))


# vi tog bort id och timestamp
create_table_person = '''
        CREATE TABLE IF NOT EXISTS person(
        firstname TEXT,
        lastname TEXT,
        dateofbirth INTEGER,
        address TEXT
        )
        '''



insert_data = '''
            INSERT INTO person(
                firstname,
                lastname,
                dateofbirth,
                address

            )
            VALUES (?, ?, ?, ?)
            '''


with sqlite3.connect('persons.db', isolation_level=None) as conn:
    conn.execute(create_table_person)

    #conn.executemany(insert_data, data_to_database_executemany)

    cursor = conn.execute('SELECT * FROM person')
    
    for row in cursor:
        print(row)

    current = cursor.fetchone()
    
    person = Person(*row)
    print(person)


conn.commit()
conn.close()

