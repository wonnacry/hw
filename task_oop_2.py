from abc import ABCMeta, abstractmethod
import os.path
import json
import pickle
from collections import namedtuple, OrderedDict


class ParamHandler(metaclass=ABCMeta):

    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = types.get(ext)
        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found!'.format(ext)
            )
        return klass(source, *args, **kwargs)

types = {}

def params(klass):
	def decorator(func):
		types[klass] = func
		return func
	return decorator

@params('txt')
class TextParamHandler(ParamHandler):
    def read(self):
        with open(self.source) as f:
            self.params = f.read()

    def write(self):
        with open(self.source, 'w') as f:
            f.writelines('{}'.format(self.params))

@params('json')
class JsonParamHandler(ParamHandler):
    def read(self):
        with open(self.source) as f:
            self.params = json.load(f)

    def write(self):
        with open(self.source, 'w') as f:
            json.dump(self.params, f, indent=4)

@params('pickle')
class PickleParamHandler(ParamHandler):
    def read(self):
        with open(self.source, 'rb') as f:
            self.params = pickle.load(f)

    def write(self):
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)


class ParamHandlerException(Exception):
    def __init__(self, text):
        print(text)
