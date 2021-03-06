#!/usr/bin/env python3
''' Module contains the class Filestorage '''
import os
import datetime
import json
import models
import models.base_model
import models.user
import models.state
import models.city
import models.amenity
import models.place
import models.review


class FileStorage:
    ''' This is the class file storage '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        json_dict = {}
        for keys in FileStorage.__objects.keys():
            json_dict[keys] = FileStorage.__objects[keys].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        ''' deserializes the JSON file to __objects (if file exists) '''
        json_dict = {}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.loads(f.read())
        except:
            return
        ''' Only created this objs to please pep8 '''
        ''' Other wise would have directly built the filstorage.objects '''
        objs = {}
        for keys in json_dict.keys():
            if json_dict[keys]['__class__'] == "BaseModel":
                objs[keys] = models.base_model.BaseModel(**json_dict[keys])
            elif json_dict[keys]['__class__'] == "User":
                objs[keys] = models.user.User(**json_dict[keys])
            elif json_dict[keys]['__class__'] == "State":
                objs[keys] = models.state.State(**json_dict[keys])
            elif json_dict[keys]['__class__'] == "City":
                objs[keys] = models.city.City(**json_dict[keys])
            elif json_dict[keys]['__class__'] == "Amenity":
                objs[keys] = models.amenity.Amenity(**json_dict[keys])
            elif json_dict[keys]['__class__'] == "Place":
                objs[keys] = models.place.Place(**json_dict[keys])
            else:
                objs[keys] = models.review.Review(**json_dict[keys])
        FileStorage.__objects = {}
        for keys in objs.keys():
            FileStorage.__objects[keys] = objs[keys]
