from abc import ABCMeta, abstractmethod
import os.path
import json
import pickle

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

    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not ParamHandler!'.format(klass)
            )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found!'.format(ext)
            )
        return klass(source, *args, **kwargs)


class TextParamHandler(ParamHandler):
    def read(self):
        with open('./params.txt') as f:
            return f.read()

    def write(self):
        with open('./params.txt', 'w') as f:
            f.writelines('{}'.format(self.params))


class JsonParamHandler(ParamHandler):
    def read(self):
        with open('./params.json') as f:
            return json.load(f)

    def write(self):
        with open('./params.json', 'w') as f:
            json.dump(self.params, f, indent=4)


class PickleParamHandler(ParamHandler):
    def read(self):
        with open('./params.pickle', 'rb') as f:
            return pickle.load(f)

    def write(self):
        with open('./params.pickle', 'wb') as f:
            pickle.dump(self.params, f)


class ParamHandlerException(Exception):
    def __init__(self, text):
        print(text)


#ParamHandler.add_type('txt', TextParamHandler)
#config = ParamHandler.get_instance('./params.txt')
#config.add_param('key1', 'value1')
#config.add_param('key2', 'value2')
#config.add_param('key3', 'value3')
#config.write()
#
#t_read = ParamHandler.get_instance('./params.txt')
#print(t_read.read())
#
#ParamHandler.add_type('json', JsonParamHandler)
#wt_json = ParamHandler.get_instance('./params.json')
#wt_json.add_param('key1', 'value1')
#wt_json.add_param('key2', 'value2')
#wt_json.add_param('key3', 'value3')
#wt_json.write()
#
#rt_json = ParamHandler.get_instance('./params.json')
#print(rt_json.read())
#
#ParamHandler.add_type('pickle', PickleParamHandler)
#wt_pickle = ParamHandler.get_instance('./params.pickle')
#wt_pickle.add_param('key1', 'value1')
#wt_pickle.add_param('key2', 'value2')
#wt_pickle.add_param('key3', 'value3')
#wt_pickle.write()
#
#rt_pickle = ParamHandler.get_instance('./params.pickle')
#print(rt_pickle.read())