from typing import List

from fastapi import FastAPI, Depends, HTTPException

from pydantic import BaseModel, ValidationError, validator, Field
import databases 
import sqlalchemy 
from datetime import datetime

from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "sqlite:///./store.db"

metadata = sqlalchemy.MetaData()

database = databases.Database(DATABASE_URL)

register = sqlalchemy.Table(
    "job",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Company_name", sqlalchemy.String(500)),
   
    sqlalchemy.Column("Title", sqlalchemy.String(500)),
    sqlalchemy.Column("Job_nature", sqlalchemy.String(500)),
    sqlalchemy.Column("Salary", sqlalchemy.Integer),

    sqlalchemy.Column("No_of_post", sqlalchemy.Integer),

    
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)

app = FastAPI()


origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
async def connect():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

class RegisterIn(BaseModel):

   

    Company_name:str = Field(...)
    
    Title:str = Field(...)
    Job_nature:str = Field(...)
    Salary:int
    No_of_post:int


class Register(BaseModel):
    id:int

    Company_name:str 
    
    Title:str 
    Job_nature:str 
    Salary:int
    No_of_post:int

@app.post('/register/', response_model=Register)
async def create(r: RegisterIn = Depends()):
    query = register.insert().values(
        
        Company_name=r.Company_name,
        
        Title=r.Title,
        Job_nature=r.Job_nature,
        Salary=r.Salary,
        No_of_post=r.No_of_post,
       
    )
    record_id = await database.execute(query)
    query = register.select().where(register.c.id == record_id)
    row = await database.fetch_one(query)
    return {**row}

@app.get('/register/{id}', response_model=Register)
async def get_one(id: int):
    query = register.select().where(register.c.id == id)
    user = await database.fetch_one(query)
    return {**user}

@app.get('/register/', response_model=List[Register])
async def get_all():
    query = register.select()
    all_get = await database.fetch_all(query)
    return all_get


@app.delete("/register/{id}", response_model=Register)
async def delete(id: int):
    query = register.delete().where(register.c.id == id)
    return await database.execute(query)


