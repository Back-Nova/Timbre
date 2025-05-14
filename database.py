import psycopg2

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='Timbre',  # Cambia esto
        user='postgres',
        password='Password'  # Cambia esto también
    )
