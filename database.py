import psycopg2

from config import (
    DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER, PARAMETRES
)

connection = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    port=DB_PORT
)

cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS cities
    (
        city_id INT PRIMARY KEY,
        name VARCHAR(32) NOT NULL
    );
    """
)
cursor.execute(
    f"""CREATE TABLE IF NOT EXISTS weather
    (
        id INT PRIMARY KEY,
        city_id INT,
        {PARAMETRES.replace(' ', ' INT, ') + ' INT,'}
        created_at TIMESTAMP,
        FOREIGN KEY (city_id) REFERENCES cities(city_id)
    );
    """
)
connection.commit()


cursor.close()
connection.close()
