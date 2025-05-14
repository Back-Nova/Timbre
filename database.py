import psycopg2

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='Timbre',  # Cambia esto
        user='postgres',
        password='Aban12062007'       # Cambia esto también
    )
