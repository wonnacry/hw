from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
	@abstractmethod
	def execute():
		pass

class AddTask(Command):
	def __init__(self, task, deadline):
		pass
	
	def execute():
		pass

class DeleteTask(Command):
	def __init__(self, n_id):
		pass
	
	def execute():
		pass

class ShowAllTasks(Command):
	def execute():
		pass

class Menu(object):
	def __init__(self):
		self.names = list()
		self.klasses = list()
		self.counter = 0
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.counter < len(self.names):
			a = self.names[self.counter], self.klasses[self.counter]
			self.counter +=1
			return a
		else:
			self.counter = 0
			raise StopIteration
	
	def add_command(self, name, klass):
		if not name:
			raise CommandException('Command must have a name!')
		if not issubclass(klass, Command):
			raise CommandException('Class {} is not Command!'.format(klass))
		self.names.append(name)
		self.klasses.append(klass)
	
	def execute(self, name, *args, **kwargs):
		if name not in self.names:
			raise CommandExcepion('Command with name {} is not found'.format(name))
		self.klasses[self.names.index(name)](*args, **kwargs)
	
class CommandException(Exception):
	pass














