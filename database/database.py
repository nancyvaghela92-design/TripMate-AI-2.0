import sqlite3
from datetime import datetime

def connect_db():
    conn = sqlite3.connect("tripmate.db")
    return conn


def create_table():
    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS trips(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    destination TEXT,

    budget TEXT,

    travelers INTEGER,

    travel_type TEXT,

    itinerary TEXT,

    created_at TEXT
)
""")
    conn.commit()
    conn.close()


def create_favorite_table():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS favorite_hotels(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        hotel_name TEXT,

        destination TEXT,

        rating INTEGER,

        price INTEGER,

        hotel_type TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_trip(destination, budget, travelers, travel_type, itinerary):

    conn = connect_db()

    cursor = conn.cursor()

    created_at = datetime.now().strftime("%d %B %Y | %I:%M %p")

    cursor.execute("""
    INSERT INTO trips(
        destination,
        budget,
        travelers,
        travel_type,
        itinerary,
        created_at
    )

    VALUES(?,?,?,?,?,?)
    """, (
        destination,
        budget,
        travelers,
        travel_type,
        itinerary,
        created_at
    ))

    conn.commit()

    conn.close()

def get_all_trips():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trips ORDER BY id DESC")

    data = cursor.fetchall()

    conn.close()

    return data


def delete_trip(trip_id):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM trips WHERE id=?",
        (trip_id,)
    )

    conn.commit()
    conn.close()


def save_favorite(hotel_name, destination, rating, price, hotel_type):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO favorite_hotels(
        hotel_name,
        destination,
        rating,
        price,
        hotel_type
    )

    VALUES(?,?,?,?,?)
    """, (
        hotel_name,
        destination,
        rating,
        price,
        hotel_type
    ))

    conn.commit()
    conn.close()


def get_favorites():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM favorite_hotels ORDER BY id DESC")

    data = cursor.fetchall()

    conn.close()

    return data


def delete_favorite(favorite_id):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM favorite_hotels WHERE id=?",
        (favorite_id,)
    )

    conn.commit()
    conn.close()
def total_trips():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM trips")

    count = cursor.fetchone()[0]

    conn.close()

    return count


def total_favorites():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM favorite_hotels")

    count = cursor.fetchone()[0]

    conn.close()

    return count


def most_popular_destination():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT destination, COUNT(*)
        FROM trips
        GROUP BY destination
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)

    data = cursor.fetchone()

    conn.close()

    if data:
        return data[0]

    return "No Trips"


def average_travelers():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(travelers) FROM trips")

    avg = cursor.fetchone()[0]

    conn.close()

    if avg:
        return round(avg,1)

    return 0
