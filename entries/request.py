import sqlite3
import json
from models import Entry, Mood
ENTRIES = [
    { 
        "id": 1, 
        "concept": "sql queries", 
        "entry": "sql queries aren't so bad", 
        "date": 4182021, #DOESNT LIKE 0 in front of 4
        "mood_id": 5 
    },
    { 
        "id": 2, 
        "concept": "sql queries", 
        "entry": "sql queries aren't so bad", 
        "date": 4182021, #DOESNT LIKE 0 in front of 4
        "mood_id": 5 
    },
    { 
        "id": 3, 
        "concept": "sql queries", 
        "entry": "sql queries aren't so bad", 
        "date": 4182021, #DOESNT LIKE 0 in front of 4
        "mood_id": 5 
    }
]


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.label mood_label
        FROM Entries e
        JOIN Moods m
            ON m.id = e.mood_id
            """)

        # Initialize an empty list to hold all entry representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row
            entry = Entry(
                row['id'], 
                row['concept'], 
                row['entry'], 
                row['date'],
                row['mood_id']
                )

            # Create a Mood instance from the current row
            mood = Mood(
                row['mood_id'],
                row['mood_label']
                )

            # Add the dictionary representation of the mood to the animal
            entry.mood = mood.__dict__

            # Add the dictionary representation of the entry to the list
            entries.append(entry.__dict__)

            # Use `json` package to properly serialize list as JSON
        return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.label mood_label
        FROM Entries e
        JOIN Moods m
        WHERE e.id = ?
        AND e.mood_id = m.id
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        entry = Entry(
            data['id'], 
            data['concept'], 
            data['entry'],
            data['date'], 
            data['mood_id']
            )
            
        mood = Mood(
            data['mood_id'],
            data['mood_label']
        )

        entry.mood = mood.__dict__

        return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))
    
def search_entry(searchTerm):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.concept,
            e.mood_id
        FROM Entries e
        WHERE e.entry LIKE ?
        """, ("%" + searchTerm + "%", ))

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(
                row["id"],
                row["date"],
                row["entry"],
                row["concept"],
                row["mood_id"])
            entries.append(entry.__dict__)

    return json.dumps(entries)