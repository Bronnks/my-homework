class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.courses = []

    def show_courses(self):
        if len(self.courses) == 0:
            print('Этот студент еще не записался ни на один курс.')
        else:
            print(f'Студент {self.name} изучает {', '.join((i.title for i in self.courses))}.')


class Courses:
    def __init__(self, title: str, instructor: str):
        self.title = title
        self.instructor = instructor
        self.students = []

    def enroll(self, student: object):
        if student in self.students:
            print('Этот студент уже изучает данный курс.')
        else:
            self.students.append(student)
            student.courses.append(self)

    def show_list_of_students(self):
        if len(self.students) == 0:
            print('На данном курсе еще нету студентов.')
        else:
            print(f'Студентов изучающих {self.title} = {len(self.students)}. А именно:')
            for i in self.students:
                print(f'Студент - {i.name}.')

    def dismissed(self, student: object):
        if student in self.students:
            self.students.remove(student)
            print(f'Студент {student.name} отчислен с курса {self.title}.')
        else:
            print('Такой студент не учится на данном курсе.')
