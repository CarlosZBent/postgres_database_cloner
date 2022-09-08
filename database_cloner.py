from sqlmodel import (
    Field, 
    SQLModel, 
    Session, 
    create_engine, 
    select,
    )
from typing import Optional


class Connection:
    def __init__(self, url) -> None:
        self.url = url
        self.session = Session
        self.engine = create_engine(url=url)

    def __str__(self) -> str:
        return 'Conecction with string {}'.format(self.url)

    def ping(self, model):
        with self.session(self.engine) as session:
            statement = select(model)
            results = session.exec(statement)
            if results:
                print('Connected')
                return True
            else:
                print('Not connected')
                return False

    def get_data(self, model):
        with self.session(self.engine) as session:
            statement = select(model)
            results = session.exec(statement)
            for result in results:
                print(result)

    
class Operations:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def compare(connection_one, connection_two):
        if connection_one == connection_two:
            print('Same')
        else:
            print('Not same')

          

# connect the script to the origin DB

# test the connection

# connect the script to the destination DB

# test the connection

# check that destination DB has compatible columns with origin DB

# fetch data from the origin DB

# save data on destination DB
