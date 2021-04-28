import sqlite3
import json
from models import User
from datetime import date

def get_all_users():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            id,
            bio,
            profile_image_url,
            created_on,
            active,
            first_name,
            last_name,
            username,
            email,
            username,
            password
        FROM Users
        """)

        users = []   
        dataset = db_cursor.fetchall()   
        for row in dataset:

            user = User(row['id'],
            row['first_name'],
            row['last_name'],
            row['username'],
            row['email'],
            row['password'],
            row['created_on'],
            row['bio'],
            row['profile_image_url'])
            users.append(user.__dict__)

    return json.dumps(users)

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

def get_auth_user(post_login):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        print(post_login["username"])
        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            u.id
        FROM Users u
        WHERE u.email= ? and u.password = ?
        """, (post_login["username"], post_login["password"]))
        
        dataset = db_cursor.fetchone()
        
        validate = {}

        if dataset["id"]:
            validate = {
                "valid": True,
                "token": dataset["id"]
            }

        return json.dumps(validate)


#####################################################
#######################todo##########################
#####################################################

def get_single_user(id):
    pass

def delete_user(id):
    pass

def update_user(id, new_customer):
    pass

def get_user_by_email(email):
    pass
