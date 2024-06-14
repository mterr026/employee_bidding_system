from peewee import PostgresqlDatabase

DATABASE = PostgresqlDatabase(
    'postgres',  
    user='postgres',  
    password='123', 
    host='localhost', 
    port=5432
)