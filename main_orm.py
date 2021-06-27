from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String


engine = create_engine(
    "mysql+mysqlconnector://root:secret@127.0.0.1:3306/mydatabase",
    echo=True,
)
Session = sessionmaker(bind=engine)
SESSION = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))


Base.metadata.create_all(engine)


def add_user(first_name, last_name):
    new_user = User(first_name=first_name, last_name=last_name)
    SESSION.add(new_user)
    SESSION.commit()
    return {
        "id": new_user.id,
        "first_name": new_user.first_name,
        "last_name": new_user.last_name
    }


def get_users():
    users = []
    users_in_db = SESSION.query(User).all()
    for user in users_in_db:
        new_user = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
        users.append(new_user)
    return users


def get_user_by_id(id):
    user = SESSION.query(User).filter_by(id=id).first()
    if user:
        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name
        }


def delete_user(id):
    user = SESSION.query(User).filter_by(id=id).first()
    if user:
        print(f"Found user with ID: {id}")
        SESSION.delete(user)
        SESSION.commit()
    else:
        print(f"User with ID: {id} not found.")


def update_user(id, first_name=None, last_name=None):
    user = SESSION.query(User).filter_by(id=id).first()
    if user:
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        SESSION.commit()
        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name
        }
