from typing import Union
from uuid import UUID


class AlreadyExistsException(Exception):
    def __init__(self, entity_name: str, name: str):
        self.message = f"{entity_name} {name} already exists within the database"
        super().__init__(self.message)


class DoesNotExistException(Exception):
    def __init__(self, entity_name: str, value: Union[str, UUID]):
        self.message = f"{entity_name} {value} doesn't exist within the database. Try creating the {entity_name} first"
        super().__init__(self.message)
