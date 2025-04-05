from sqlmodel import SQLModel, create_engine

engine = create_engine("sqlite:///./database.db", echo=True)

print("CREATING . . . . ")

SQLModel.metadata.create_all(engine)