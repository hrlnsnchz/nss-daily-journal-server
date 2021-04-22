import sqlite3
import json
from models import Mood


def get_all_moods():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM Moods m
            """)

        # Initialize an empty list to hold all mood representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a Mood instance from the current row
            mood = Mood(
                row['id'], #Doesn't seem to run without its 3 positional arguments but this returns only 1 animal
                row['label']
                )

            moods.append(mood.__dict__)

            # Use `json` package to properly serialize list as JSON
        return json.dumps(moods)


