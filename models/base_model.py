#!/usr/bin/env python3
'''class base model for every model to inherit from'''

from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''class for basemode'''

    def __init__(self) -> None:
        """ constructor for the instance"""
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"[{type(self)}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()


test = datetime.now()

print(test.isoformat())
