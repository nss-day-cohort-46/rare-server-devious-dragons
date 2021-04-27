import sqlite3
import json
from models import Comment

def get_all_comments():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            id,
            post_id,
            author_id,
            content
        FROM Comments
        """)

        dataset = db_cursor.fetchall()

        comments = []

        for row in dataset:
            comment = Comment(row['id'], 
                        row['post_id'],
                        row['author_id'],
                        row['content']) 
            comments.append(comment.__dict__)

    return json.dumps(comments)
def create_comment(new_comment):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( post_id, author_id, content )
        VALUES
            ( ?, ?, ?);
        """, (new_comment['postId'], new_comment['authorId'],
              new_comment['content'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id


    return json.dumps(new_comment)