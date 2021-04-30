import sqlite3
import json
from models import Reaction

def get_all_reactions():
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


        db_cursor.execute("""
            SELECT 
                r.id,
                r.label,
                r.image_url
            FROM Reactions r
        """)

        reactions = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            react = Reaction(row['id'], row['label'], row['image_url'])

            reactions.append(react.__dict__)

    return json.dumps(reactions)

# def get_single_reaction(id):
    # with sqlite3.connect("./rare.db") as conn:
    #     conn.row_factory = sqlite3.Row
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         t.id,
    #         t.label
    #     FROM Tags t
    #     WHERE t.id = ?
    #     """, ( id, ))
        
    #     data = db_cursor.fetchone()

    #     tag = Tag(data['id'], data['label'])

    #     return json.dumps(tag.__dict__)

def create_reaction(reaction_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Reactions
            (label, image_url)
        VALUES
            ( ?, ?);
        """, (reaction_post['label'], reaction_post['imageUrl'], ))

        id = db_cursor.lastrowid

        reaction_post['id'] = id


    return json.dumps(reaction_post)

# def delete_reaction(id):
    # with sqlite3.connect("./rare.db") as conn:
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     DELETE FROM Tags
    #     WHERE id = ?
    #     """, (id, ))

