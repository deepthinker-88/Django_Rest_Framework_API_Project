import psycopg2

def create_database_connection():
    try:
        #    conn = psycopg2.connect(database="test", user="postgres", password="secret")
        conn = psycopg2.connect(
            datbase = 'football',
            user = 'postgres',
            
        )
        print("Connected to the Postgres Database succesfully")
    except Exception as e:
        print(f"Could not connect to the Postgres Database due to {e}")
    
    
create_database_connection('football','postgres','postgres','127.0.0.1','5432')

