import sqlite3
import json
from models import PostReaction

def get_all_postReactions():
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


        db_cursor.execute("""
            SELECT 
                pr.id,
                pr.user_id,
                pr.reaction_id,
                pr.post_id
            FROM PostReactions pr
        """)

        post_reactions = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            reaction = PostReaction(row['id'], row['user_id'], row['post_id'], row['reaction_id'])

            post_reactions.append(reaction.__dict__)

    return json.dumps(post_reactions)

def create_postReaction(react_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostReactions
            (user_id, reaction_id, post_id)
        VALUES
            ( ?, ?, ?);
        """, (react_post['userId'], react_post['reactionId'], react_post['postId'] ))

        id = db_cursor.lastrowid

        react_post['id'] = id


    return json.dumps(react_post)

def get_postReactions_by_reaction(reactionId):
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT 
                pr.id,
                pr.user_id,
                pr.reaction_id,
                pr.post_id
            FROM PostReactions pr
            WHERE pr.reaction_id = ?
        """, (reactionId, ))

        post_reactions = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            reaction = PostReaction(row['id'], row['user_id'], row['reaction_id'], row['post_id'])

            post_reactions.append(reaction.__dict__)

    return json.dumps(post_reactions)