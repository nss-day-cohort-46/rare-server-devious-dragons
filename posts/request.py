import sqlite3, json
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