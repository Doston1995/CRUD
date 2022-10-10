from pydantic import BaseModel, Field


class UserList(BaseModel):
    id          :str
    username    :str
    password    :str
    first_name  :str
    last_name   :str
    gender      :str
    create_at   :str
    status      :str

class UserEntry(BaseModel):
    username    :str = Field(..., example = "Doston")
    password    :str = Field(..., examole = "123")
    first_name  :str = Field(..., example = "Doston")
    last_name   :str = Field(..., example = "Imomaliyev")
    gender      :str = Field(..., example = "M")


class UserUpdate(BaseModel):
    id          :str = Field(..., example = "Your id")  
    first_name  :str = Field(..., example = "Doston")
    last_name   :str = Field(..., example = "Imomaliyev")
    gender      :str = Field(..., example = "M")
    status      :str = Field(..., example = "1")
    
    
class UserDelete(BaseModel):
    id: str = Field(..., example = "Enter your id")