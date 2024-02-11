from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str, base_salary: int) -> None:
        self.name = name
        self.base_salary = base_salary

    @abstractmethod
    def calculate_salary(self) -> None:
        pass

    def sum_salary(self, bonus: float) -> float:
        return self.base_salary * bonus + self.base_salary


class Manager(Employee):
    def calculate_salary(self) -> float:
        return self.sum_salary(0.2)


class Developer(Employee):
    def calculate_salary(self) -> float:
        return self.sum_salary(0.1)


class Tester(Employee):
    def calculate_salary(self) -> float:
        return self.sum_salary(0.3)
