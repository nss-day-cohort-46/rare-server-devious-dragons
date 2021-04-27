import sqlite3, json
from datetime import date
from models import Post

def get_all_posts():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            id,
            user_id,
            category_id,
            title,
            publication_date,
            image_url,
            content,
            approved
        FROM Posts
        """)

        dataset = db_cursor.fetchall()

        posts = []

        for row in dataset:
            post = Post(row['id'], 
                        row['user_id'],
                        row['category_id'],
                        row['title'],
                        row['publication_date'],
                        row['image_url'],
                        row['content'],
                        row['approved']) 
            posts.append(post.__dict__)

    return json.dumps(posts)

def get_single_post(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Posts p
        WHERE p.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        post = Post(data['id'], data['user_id'], data['category_id'],
                            data['title'], data['publication_date'],
                            data['image_url'], data['content'], data['approved'])
        
        return json.dumps(post.__dict__)

def create_post(new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO posts
            (
            user_id,
            title,
            content,
            publication_date,
            category_id,
            image_url,
            approved
            )
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?);
        """,
            (
            new_post['user_id'],
            new_post['title'],
            new_post['content'],
            date.today(),
            0,
            "",
            0,
            )
        )

        id = db_cursor.lastrowid
        new_post['id'] = id

    return json.dumps(new_post)

