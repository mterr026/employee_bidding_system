from peewee import PostgresqlDatabase

#login informatin for postgres
DATABASE = PostgresqlDatabase(
    'postgres',  
    user='postgres',  
    password='123', 
    host='localhost', 
    port=5432
)

#Check if database is connected, if not create connection
def get_db():
    if DATABASE.is_closed():
        DATABASE.connect()
    try:
        yield
    finally:
        if not DATABASE.is_closed():
            DATABASE.close()