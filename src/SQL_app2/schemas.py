from pydantic import BaseModel

class UsersBase(BaseModel):
 
    name: str

    class Config:
        from_attributes = True

class Test(BaseModel):

    name: str

    class Config:
        from_attributes = True



class UserCreate(BaseModel):
    EIN: int
    password: str

    class Config:
        from_attributes = True

