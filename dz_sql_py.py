import psycopg2 as psy

 

def create_db(conn):    

    with conn.cursor() as cur:
         cur.execute ("""
         CREATE TABLE client(
            client_id SERIAL PRIMARY KEY,
            name VARCHAR(40) NOT NULL,
            lastname VARCHAR(40) NOT NULL,
            email VARCHAR(40) NOT NULL
         );
         """)

         cur.execute ("""
         CREATE TABLE phone(
            phone_id SERIAL PRIMARY KEY,
            number VARCHAR(40),
            client_id INT NOT NULL REFERENCES client(client_id)
         );
         """)
         
         
         
         return conn.commit()
       
def add_client(conn, name, lastname, email):
    with conn.cursor() as cur:
         cur.execute (f"""
         INSERT INTO client(name, lastname, email)
         VALUES('{name}','{lastname}','{email}');
         """)
         return conn.commit()
    
    
def add_phone(conn, number:int(), client_id):
    with conn.cursor() as cur:
         cur.execute (f"""
         INSERT INTO phone(number, client_id)
         VALUES('{number}','{client_id}');
         """)
         return conn.commit()
         
def change_client(conn, client_id, name=None, lastname=None, email=None):
    with conn.cursor() as cur:
         cur.execute (f"""
         UPDATE client
         SET name = '{name}',
         lastname = '{lastname}',
         email = '{email}'
         WHERE client_id = '{client_id}'
         """)
         return conn.commit()

def delete_phone(conn, client_id, number):
    with conn.cursor() as cur:
         cur.execute (f"""  
         DELETE FROM phone      
         WHERE client_id = '{client_id}' AND number = '{number}'
         """)

def delete_client(conn, client_id):
    with conn.cursor() as cur:
         cur.execute (f"""
         DELETE FROM client      
         WHERE client_id = '{client_id}'
         """)

def find_client(conn, name=None, lastname=None, email=None, number=None):
     with conn.cursor() as cur:
         cur.execute("""
                --begin-sql
                SELECT *
                  FROM client cl
                  JOIN phone ph ON cl.client_id = ph.client_id
                 WHERE (name = %(name)s OR %(name)s IS NULL)
                   AND (lastname = %(lastname)s OR %(lastname)s IS NULL)
                   AND (email = %(email)s OR %(email)s IS NULL)
                   AND (number = %(number)s OR %(number)s IS NULL);
            """, {"name": name, "lastname": lastname, "email": email, "number": number})

with psy.connect(database="clients_db", user="postgres", password="slavauka") as conn:
        
    # create_db(conn)
    # add_client(conn, 'Test','Test1','efkefk')
    # add_phone(conn,87772692121,2)
    # change_client(conn, '1', 'update_name', 'update_lastname', 'update_@')
    # delete_phone(conn, '1', '87772692121')
    # delete_client(conn, '1')
    # find_client(conn, '87772692121')
    conn.close

