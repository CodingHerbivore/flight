import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

def create_db():
    # Name, price, seats total, seats first class, cruise (knots), range, fuel (us gal, usable),
    c.execute("""CREATE TABLE planes (
              manufacturer text,
              name text,
              price real,
              seats integer,
              fcseats integer,
              cruise integer,
              range integer,
              fuel integer    
             )""")
create_db()


def insert_plane(plane):
    with conn:
        c.execute("INSERT INTO planes VALUES (:manufacturer, :name, :price, :seats, :fcseats, :cruise, :range, :fuel)",
                  {'manufacturer': plane.manufacturer, 'name': plane.name, 'price': plane.price, 'seats': plane.seats, 'fcseats': plane.fcseats, 'cruise': plane.cruise, 'range': plane.range, 'fuel': plane.fuel})

def list_planes(manufacturer):
    c.execute("SELECT * FROM planes WHERE manufacturer = :manufacturer", {'manufacturer': manufacturer})
    return c.fetchall()

def close_connection():
    conn.close()