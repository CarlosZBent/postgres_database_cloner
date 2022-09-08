from sqlmodel import (
    Field, 
    SQLModel, 
    Session, 
    create_engine, 
    select,
    )
from typing import Optional
from database_cloner import Connection, Operations

class Users(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	username: Optional[str] = None
	user_id: int
	full_name: str
	phone_no: int
	email: str


conn1 = Connection('postgresql+psycopg2://postgres:CeZb2332@localhost:5432/postgres')
conn2 = Connection('postgresql+psycopg2://postgres:CeZb2332@localhost:5432/postgres')
# conn1.ping(Users)
# conn1.get_data(Users)

Operations.compare(conn1, conn2)

