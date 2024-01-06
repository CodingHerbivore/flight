import pandas as pd
from classes.plane import Plane
from database import insert_plane

def load_planes():
    df = pd.read_csv('planes.csv')
    
    for i, row in df.iterrows():
        plane = Plane(row.manufacturer,
                      row.type,
                      row.price,
                      row.seats,
                      row.fcseats,
                      row.cruise,
                      row.range,
                      row.fuel,
                      row.runway)
        
        insert_plane(plane)
    print("Planes loaded.")


    