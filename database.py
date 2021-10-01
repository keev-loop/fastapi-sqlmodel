from sqlmodel import SQLModel, create_engine


engine = create_engine("sqlite:///./banco.db", echo=True)