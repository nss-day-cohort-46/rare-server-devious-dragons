import sqlite3
import json
from models import PostTag


def get_all_post_tags():
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT 
                pt.id,
                pt.post_id,
                tag_id
            FROM PostTags pt
        """)

        post_tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            post_tag = Tag(row['id'], row['postId', row['tagId']])

            post_tags.append(post_tag.__dict__)

    return json.dumps(post_tags)

    
def create_post_tag(post_with_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostTags
            (post_id, tag_id)
        VALUES
            ( ?, ?);
        """, (post_with_tag['postId'], post_with_tag['tagId'], ))

        id = db_cursor.lastrowid

        post_with_tag['id'] = id


    return json.dumps(post_with_tag)