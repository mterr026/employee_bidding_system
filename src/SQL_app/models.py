from peewee import *
from SQL_app.config import DATABASE

#Models are used to represent tables in the database, using models reduces the amount of code
#needed for CRUD operations

#Basemodel sets the the standard for all models, reduces the amount of redundancy
class BaseModel(Model):
    #Defines table configurations (table name, connection, )
    class Meta:
        database = DATABASE

#all model classes will inherit BaseModel class
class Users(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()

class Test(BaseModel):
    id = AutoField(primary_key=True)
    option = CharField()
    