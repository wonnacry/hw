from abc import ABCMeta, abstractmethod
import re


class Validator(metaclass=ABCMeta):
    types = {}

    def add_type(name, klass):
        if not name:
            raise ValidatorExteption('Validator must have a name!')
        if name in Validator.types:
            print('Klass {} is already in types'.format(name))
        else:
            if issubclass(klass, Validator):
                Validator.types[name] = klass
            else:
                raise ValidatorExteption("Klass {} is not Validator".format(name))

    def get_instance(name):
        klass = Validator.types.get(name)
        if klass is None:
            raise ValidatorException('Type "{}" not found!'.format(name))
        return klass

    @abstractmethod
    def validate(value):
        pass


class ValidatorException(Exception):
    """Expression here"""
    pass


class EmailValidator(Validator):

    def validate(email):
        if '@' in email:
            return True
        else:
            return False


class DateTimeValidator(Validator):

    def validate(datetime):
        template = re.compile('\d{1,4}[-./]\d{1,2}[-./]\d{1,4} ?\d?\d?:?\d?\d?:?\d?\d?')
        a = template.findall(datetime)
        a = str(a[0])
        if a == datetime:
            return True
        else:
            return False
