import pyodbc
import math
import os


DB_PATH = "C:\\Users\\anastasiya_shyshliuk\\PycharmProjects\\python_course\\Final_Task\\cities.db"
CONN_STR = f"DRIVER={{Devart ODBC Driver for SQLite}};DATABASE={DB_PATH};"


def create_db():
    if not os.path.exists(DB_PATH):
        open(DB_PATH, 'w').close()

    conn = pyodbc.connect(CONN_STR)
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS cities (
            name TEXT PRIMARY KEY,
            latitude REAL,
            longitude REAL
        )
    """)
    conn.commit()
    conn.close()


def get_city_coordinates(city):
    conn = pyodbc.connect(CONN_STR)
    cur = conn.cursor()
    cur.execute(f"SELECT latitude, longitude FROM cities WHERE name = '{city}'")
    row = cur.fetchone()
    conn.close()
    return row if row else None


def save_city_coordinates(city, lat, lon):
    conn = pyodbc.connect(CONN_STR)
    cur = conn.cursor()
    cur.execute(f"INSERT INTO cities (name, latitude, longitude) VALUES ('{city}', {lat}, {lon})")
    conn.commit()
    conn.close()


def distance_between_cities(lat1, lon1, lat2, lon2):
    R = 6371
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


def main():
    create_db()

    city1 = input("Enter the first city: ").strip().title()
    city2 = input("Enter the second city: ").strip().title()

    coord1 = get_city_coordinates(city1)
    if not coord1:
        lat1 = float(input(f"Enter latitude for {city1}: "))
        lon1 = float(input(f"Enter longitude for {city1}: "))
        save_city_coordinates(city1, lat1, lon1)
        coord1 = (lat1, lon1)

    coord2 = get_city_coordinates(city2)
    if not coord2:
        lat2 = float(input(f"Enter latitude for {city2}: "))
        lon2 = float(input(f"Enter longitude for {city2}: "))
        save_city_coordinates(city2, lat2, lon2)
        coord2 = (lat2, lon2)

    distance = distance_between_cities(coord1[0], coord1[1], coord2[0], coord2[1])
    print(f"Distance between {city1} and {city2}: {distance:.2f} km")


if __name__ == "__main__":
    main()