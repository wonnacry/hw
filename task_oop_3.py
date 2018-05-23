from abc import ABCMeta, abstractmethod

class Courses(metaclass=ABCMeta):
    def __init__(self):

        self.students = []

    def add_student(self, student):
       self.students.append(student)

    def remove_student(self, id):
       if self.students:
           if id in range(len(self.students)):
                self.students.pop(id)
           else:
               print('Id is out of range')
       else:
           print('List of students is empty')

    def show_students(self):
       for n, i in enumerate(self.students):
           print('{}. {}'.format(n, i))

    names_of_courses = []

    @classmethod
    def add_course(cls, course):

        if not issubclass(course, Courses):
            raise CoursesException('Course "{}" is not from Courses!'.format(course))

        cls.names_of_courses.append(course)

    @abstractmethod
    def name_of_course(cls):
        pass

class CourseExtepion(Exception):
    def __init__(self, text):
        print(text)


class Python(Courses):

    def name_of_course(cls):
        return "Name of teacher's course: {}".format(__class__.__name__)




###Tests###

Courses.add_course(Python)
Kirill = Python()
Kirill.add_student("Ilya Bogdan")
Kirill.add_student("Petya Ivanov")
Kirill.add_student("Sasha Zaharov")
Kirill.show_students()
Kirill.remove_student(1)
print()
Kirill.show_students()
print(Kirill.name_of_course())