import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

def create_db():
    # Name, price, seats total, seats first class, cruise (knots), range, fuel (us gal, usable), runway (ft)
    c.execute("""CREATE TABLE planes (
              manufacturer text,
              type text,
              price real,
              seats integer,
              fcseats integer,
              cruise integer,
              range integer,
              fuel integer,
              runway integer    
             )""")
create_db()


def insert_plane(plane):
    with conn:
        c.execute("INSERT INTO planes VALUES (:manufacturer, :type, :price, :seats, :fcseats, :cruise, :range, :fuel, :runway)",
                  {'manufacturer': plane.manufacturer, 'type': plane.type, 'price': plane.price, 'seats': plane.seats, 'fcseats': plane.fcseats, 'cruise': plane.cruise, 'range': plane.range, 'fuel': plane.fuel, 'runway': plane.runway})

def list_planes(q):
    c.execute("SELECT * FROM planes")
    

def close_connection():
    conn.close()