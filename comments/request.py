import sqlite3
import json
from models import Comment, User

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

def get_single_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            u.username
        FROM Comments c
        JOIN Users u
            ON c.author_id = u.id
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        comment = Comment(data['id'], data['post_id'], data['author_id'], data['content'])
        comment.username = data['username']
        
        # comment.append(comment.__dict__)
    return json.dumps(comment.__dict__)


def get_comments_by_post_id(post_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            u.username
        from Comments c
        JOIN Users u
            ON c.author_id = u.id
        WHERE c.post_id = ?
        """, ( post_id, ))
        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
          comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])
          comment.username = row['username']
          comments.append(comment.__dict__)
    return json.dumps(comments)

def update_comment(id, new_comment):
  with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comments
            SET
                post_id = ?,
                author_id = ?,
                content = ?
        WHERE id = ?
        """, (new_comment['postId'], new_comment['authorId'],
              new_comment['content'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

  if rows_affected == 0:
        # Forces 404 response by main module
      return False
  else:
        # Forces 204 response by main module
      return True

def delete_comment(id):
  with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))
