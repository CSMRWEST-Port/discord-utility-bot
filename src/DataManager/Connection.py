import psycopg2
import os, time;

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        db_url = os.getenv('DATABASE_URL')

        while self.connection is None:
            try:
                self.connection = psycopg2.connect(db_url)
            except psycopg2.OperationalError as e:
                print(e)
                break;
       

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
