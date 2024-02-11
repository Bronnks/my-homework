from dataclasses import dataclass
import string
from typing import NamedTuple
from pydantic import BaseModel, Field, ValidationError, field_validator


@dataclass
class Student1:
    name: str
    lastname: str
    age: int
    course: int
    gpa: float

    def __post_init__(self) -> None:
        self.validate_name()
        self.validate_age()
        self.validate_course()
        self.validate_gpa()

    def validate_name(self) -> None:
        for i in (self.name, self.lastname):
            if i[0] not in string.ascii_uppercase:
                raise ValueError('Первая буква не заглавная')
            if not i.isalpha():
                raise ValueError('Имя|фамилия состоят не только из букв.')

    def validate_age(self) -> None:
        if self.age < 18 or self.age > 30:
            raise ValueError('Студент не проходит по возрасту.')

    def validate_course(self) -> None:
        if self.course < 1 or self.course > 6:
            raise ValueError('Курсов с такими значениями не существует.')

    def validate_gpa(self) -> None:
        if self.gpa < 1 or self.gpa > 100:
            raise ValueError('Такого среднего балла не может быть.')


class Student2(NamedTuple):
    name: str
    lastname: str
    age: int
    course: int
    gpa: float


def validate_student(student: Student2) -> None:
    for i in (student.name, student.lastname):
        if not i.isalpha():
            raise ValueError('Имя|фамилия состоят не только из букв.')
        if i[0] not in string.ascii_uppercase:
            raise ValueError('Первая буква не заглавная')
    if student.age < 18 or student.age > 30:
        raise ValueError('Студент не проходит по возрасту.')
    if student.course < 1 or student.course > 6:
        raise ValueError('Курсов с такими значениями не существует.')
    if student.gpa < 1 or student.gpa > 100:
        raise ValueError('Такого среднего балла не может быть.')


"""Реализация DTO с помощью TypedDict полностью аналогична с NamedTuple, различие, как я понял, лишь в том, что у
первого объект станет словарем, и можно будет уже работать с ним соответствующе."""


class Student3(BaseModel):
    name: str
    lastname: str
    age: int = Field(gt=17, lt=31)
    course: int = Field(gt=0, lt=7)
    gpa: float = Field(gt=0, lt=101)

    @field_validator('name', 'lastname')
    def validate_name(cls, v: str) -> str:
        if not v.isalpha():
            raise ValueError('Имя|фамилия состоят не только из букв.')
        if v[0] not in string.ascii_uppercase:
            raise ValueError('Первая буква не заглавная')
        return v


s = Student1('John', 'Smith', 21, 2, 45.3)
s2 = Student2('John', 'Smith', 21, 2, 45.3)
validate_student(s2)
try:
    s3 = Student3(**{'name': 'John', 'lastname': 'Doe', 'age': 20, 'course': 3, 'gpa': 14})
except ValidationError as e:
    print(e)
