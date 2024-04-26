from pydantic import BaseModel, Field, EmailStr

class userSchema(BaseModel):
    user_id: int 
    name: str 
    email: EmailStr 
    password: str 
    role: str 

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "name": "Joe Doe",
                "email": "joe@xyz.com",
                "password": "any",
                "role": "jobseekar"
            }
        }
class Employe(BaseModel):
    emp_id: int 
    name: str 
    email: EmailStr 
    password: str 
    role: str 

    class Config:
        schema_extra = {
            "example": {
                "emp_id": 1,
                "name": "Joe Doe",
                "email": "joe@xyz.com",
                "password": "any",
                "role": "jobseekar"
            }
        }


class jobpost(BaseModel):
    job_id: int = Field(default=None)
    title: str = Field(default=None)
    company: str = Field(default=None)
    discription: str = Field(default=None)
    skill: str = Field(default=None)
    emp_id:int = Field(default=None)

class application(BaseModel):
    app_id: int = Field(default=None) 
    user_id: int = Field(default=None)
    job_id: int = Field(default=None)
    status: str = Field(default=None)
    resume_link: str = Field(default=None)
    
class UserLogin(BaseModel):
    email : EmailStr
    password : str 
    role: str

class EmpLogin(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    role: str


class userupdate(BaseModel):
    name: str 
    email: EmailStr 
    password: str 

class jobupdate(BaseModel):
    title: str = Field(default=None)
    company: str = Field(default=None)
    discription: str = Field(default=None)
    skill: str = Field(default=None)

class statusupdate(BaseModel):
    status: str = Field(default=None)