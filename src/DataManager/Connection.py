import psycopg2
import os, time;

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        db_url = os.getenv('DATABASE_URL')

        conn = None
        attempts = 0

        while attempts < 5:
            try:
                self.connection = psycopg2.connect(db_url)
                print("Database connection established.")
                return
            except psycopg2.OperationalError as e:
                attempts += 1
                print(f"Database connection failed (attempt {attempts}/5): {e}")
                time.sleep(5)
        
        raise Exception("Failed to connect to the database after 5 attempts.")
       

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
