#!/usr/bin/python3
"""
Base class module
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """Initilize instance of BaseModel Class
    This is the Base Model that care of initialization, serialization and deseriealization
    of the future instansces.
    """
    if kwargs:
        for key, value in kwargs.items():
            if key == 'created_at' or key == "updated_at":
                setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
            elif key == '__class__':
                continue
            else:
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Prints a BaseModel Instance"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
        
    def save(self):
        """Updates the public instance attribute updated_at with the current 
        datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys / values __dict__ 
        of the instance."""
        retval = (self.__dict__).copy()
        retval["created_at"] = retval['created_at'].isoformat()
        retval["updated_at"] = retval['updated_at'].isoformat()
        retval['__clas__'] = self.__class__.__name__
        return retval

    def __repr__(self):
        """Prints a BaseModel Instance"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )