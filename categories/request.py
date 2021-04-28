import sqlite3
import json
from models import Post


def get_all_categories():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            id,
            label
        FROM Categories
        """)

        dataset = db_cursor.fetchall()

        categories = []

        for row in dataset:
            cat = {
                "id": row['id'],
                "label": row['label']
            }
            categories.append(cat)

    return json.dumps(categories)


def create_category(new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            (label)
        VALUES
            ( ? );
        
        """, (new_category['label'], ))

        id = db_cursor.lastrowid
        new_category['id'] = id

    return json.dumps(new_category)


def update_category(id, new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Categories
            SET
                label = ?
            WHERE id = ?
        """, (new_category['label'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def delete_category(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM Categories
            WHERE id = ?
        """, (id,))
