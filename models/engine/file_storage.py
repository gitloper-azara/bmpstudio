#!/usr/bin/python3
'''Serialising instances to a JSON file and
Deserialising JSON file to instances
'''
import json
from models.base_model import BaseModel
from models.categories import Category
from models.images import Image
from models.photographers import Photographer


class FileStorage:
    '''A storage engine that serialises instances to a JSON file
    and deserialises a JSON file to instances
    '''
    __file_path = 'file.json'
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'Category': Category,
        'Image': Image,
        'Photographer': Photographer,
    }

    def all(self):
        '''A public instance method to the storage class

        Returns:
            The dictionary '__objects' when called upon
        '''
        return self.__objects

    def new(self, obj):
        '''A public instance method to the storage class that sets
        inside of '__objects', the 'obj' with the key <obj class name>.id
        '''
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        '''A public instance method to the storage class that serialises
        '__objects' to the JSON file
        '''
        serialised_objs = {}
        for key, value in self.__objects.items():
            serialised_objs[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(serialised_objs, json_file)

    def reload(self):
        '''A publc instance method to the storage class that deserialises
        the JSON file to '__objects' if the JSON file exists
        '''
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                self.__objects = json.load(file)
                for key, value in self.__objects.items():
                    cls = value['__class__']
                    self.all()[key] = self.__classes[cls](**value)
        except FileNotFoundError:
            pass
