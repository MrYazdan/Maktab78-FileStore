from core.models import DBModel


class User(DBModel):  # User model
    TABLE = 'users'
    PK = 'id'

    def __init__(self, first_name, last_name, phone, national_id, age, password, id=None) -> None:
        ...

        if id: self.id = id
