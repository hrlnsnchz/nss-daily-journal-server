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
    return ENTRIES

# Function with a single parameter
def get_single_entry(id):
    # Variable to hold the found entry, if it exists
    requested_entry = None

    # Iterate the ENTRIES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for entry in ENTRIES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if entry["id"] == id:
            requested_entry = entry

    return requested_entry