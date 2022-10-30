import psycopg2

# def delete_table(connection, cursor, table_name):
#     cur.execute(f"""
#         DROP TABLE {table_name}
#     """)
#     connection.commit()

def create_db(connection, cursor, table_name, **table_columns):
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
        {table_name}_id SERIAL PRIMARY KEY
        );
        """)
    connection.commit()
    for name_column, type_column in table_columns.items():
        cursor.execute(f"""
            ALTER TABLE {table_name} ADD COLUMN IF NOT EXISTS {name_column} {type_column} 
        """)
        connection.commit()
    print(f'Table {table_name} is created')

def add_client(connection, cursor, table_name, **values):
    cur.execute(f"""
        INSERT INTO {table_name}({", ".join(key for key in values.keys())})
        VALUES ({", ".join(item for item in values.values())}) 
    """)
    connection.commit()
    cursor.execute(f"""
            SELECT {table_name}_id FROM {table_name}
    """)
    print(f'adding successful: {table_name}_id is {cursor.fetchone()[0]}')

def add_phone(connection, cursor, table_name, client_id, phone):
    cur.execute(f"""
        INSERT INTO {table_name} (client_id, phone)
        VALUES({client_id}, '{phone}');
    """)
    connection.commit()
    cursor.execute(f"""
            SELECT first_name, last_name, phone 
            FROM {table_name}
                INNER JOIN client USING (client_id);
    """)
    print(cur.fetchall())

def change_client(connection, cursor, table_name, client_id, **values):
    for key, value in values.items():
        cursor.execute(f"""
            UPDATE {table_name}
            SET {key} = {value}
            WHERE client_id = {client_id};
        """)
    cursor.execute(f"""
           SELECT * FROM {table_name} 
    """)
    print(cur.fetchall())

def delete_phone(connection, cursor, table_name, client_id, phone):
    cursor.execute(f"""
        DELETE FROM {table_name}
        WHERE client_id = {client_id} AND phone = {phone};
    """)
    cursor.execute(f"""
               SELECT * FROM {table_name} 
        """)
    print(cur.fetchall())

def delete_client(connection, cursor, table_name, client_id):
    cursor.execute(f"""
        DELETE FROM {table_name}
        WHERE client_id = {client_id}
    """)
    cursor.execute(f"""
                   SELECT * FROM {table_name} 
            """)
    print(cur.fetchall())

def find_client(cursor, **values):
    for key, value in values.items():
        cursor.execute(f"""
                    SELECT client_id, first_name, last_name, email, phone
                    FROM client INNER JOIN phone USING (client_id)
                    WHERE {key} = '{value}'
                """)
        print(cursor.fetchall())


with psycopg2.connect(database='clients_db', user='postgres', password='postgres') as conn:
    with conn.cursor() as cur:
        # create_db(conn, cur, 'client', first_name='VARCHAR(30)', last_name='VARCHAR(30)', email='VARCHAR(60)')
        # create_db(conn, cur, 'phone', client_id='INTEGER REFERENCES client(client_id)', phone='VARCHAR(20)')
        # add_client(conn, cur, 'client', first_name="'Valeria'", last_name="'Sofina'", email="'netology@netology.com'")
        # add_phone(conn, cur, 'phone', 5, '89191234568')
        # change_client(conn, cur, 'client', 1, first_name="'Roman'", last_name="'Sofin'", email="'new_netology@netology.com'")
        # delete_phone(conn, cur, 'phone',  1, "'89191234567'")
        # delete_client(conn, cur, 'client', 4)
        # find_client(cur, phone='89191234567')
        # delete_table(conn, cur, 'phone')

conn.close()

                   
