import sqlite3, json
from datetime import date
from models import Post
from models import Tag
from models import PostTag

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
            

            db_cursor.execute("""
                SELECT 
                    t.id,
                    t.label 
                FROM Tags t
                JOIN PostTags pt
                    ON t.id = pt.tag_id
                WHERE pt.post_id = ?
                """, (row['id'],))
                    
            post_tags= db_cursor.fetchall()

            tags = []

            for row in post_tags:
                tag = Tag(row['id'], row['label'])

                tags.append(tag.__dict__)

            post.tags =tags
            
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
        
        
        db_cursor.execute("""
                SELECT 
                    pt.id,
                    pt.tag_id,
                    pt.post_id,
                    t.id tagId,
                    t.label
                FROM PostTags pt
                JOIN Tags t
                    ON t.id = pt.tag_id
                WHERE pt.post_id = ?
                """, (id,))
                    
        post_tags= db_cursor.fetchall()

        postTags = []

        for row in post_tags:
            post_tag = PostTag(row['id'], row['tag_id'], row['post_id'])
            
            tag = Tag(row['tag_id'], row['label'])

            post_tag.tag = tag.__dict__
            
            postTags.append(post_tag.__dict__)
        
        post.postTags =postTags
    
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
            new_post['publication_date'],
            new_post['category_id'],
            new_post['image_url'],
            0,
            )
        )

        id = db_cursor.lastrowid
        new_post['id'] = id

    return json.dumps(new_post)

def update_post(id, post_obj):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE posts
            SET
                title = ?,
                content = ?,
                category_id = ?,
                image_url= ?
        WHERE id = ?
        """, (
            post_obj['title'],
            post_obj['content'],
            post_obj['category_id'],
            post_obj['image_url'], id
            , ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def delete_post(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
        """, (id, ))
