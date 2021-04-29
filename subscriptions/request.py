import sqlite3
import json
from datetime import date
from models import Subscription, post

def get_all_subscriptions():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT 
                id,
                follower_id,
                author_id,
                created_on,
                ended_on
            FROM Subscriptions
        """)

        dataset = db_cursor.fetchall()
        subscriptions = []

        for row in dataset:
            subscription = Subscription(row['id'],
                                        row['follower_id'],
                                        row['author_id'],
                                        row['created_on'],
                                        row['ended_on'])
            subscriptions.append(subscription.__dict__)
    return json.dumps(subscriptions)

def create_subscription(new_sub):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Subscriptions
            (
            follower_id,
            author_id,
            created_on
            )
        VALUES
            ( ?, ?, ?);
        """,
            (
            new_sub['followerId'],
            new_sub['authorId'],
            date.today()
            )
        )

        id = db_cursor.lastrowid
        new_sub['id'] = id

    return json.dumps(new_sub)

def delete_subscription(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Subscriptions
        WHERE id = ?
        """, (id, ))
    
            

