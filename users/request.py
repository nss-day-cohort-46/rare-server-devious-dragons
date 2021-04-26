import sqlite3
import json
from models import User
from datetime import date

def get_all_users():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email
        FROM customer c
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            customer = Customer(row['id'], row['name'], row['address'],
                            row['email'])

            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


def get_single_user(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'])

        return json.dumps(customer.__dict__)

def register_user(user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO users
            ( first_name, last_name, email, password, created_on, active, is_staff )
        VALUES
            ( ?, ?, ?, ?);
        """, (user['first_name'], user['last_name'],
            user['email'], user['password'], date.today(),1,1 ))

        id = db_cursor.lastrowid

        user['id'] = id
        user['valid']=True
        user['token']=id


    return json.dumps(user)


def delete_user(id):
    pass

def update_user(id, new_customer):
    pass

def get_user_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)