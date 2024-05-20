from sqlmodel import SQLModel ,Session, Field ,create_engine,select
import os


connection_string=os.getenv('DB_URI')
print(connection_string)
engine=create_engine(connection_string)

def create_tables():
    SQLModel.metadata.create_all(engine)
