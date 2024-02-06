class Employee:
    def __init__(self, name: str, position: str, salary: int):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        print(f'{self.position} {self.name} получает {self.salary}.')


class Manager(Employee):

    def __init__(self, name: str, position: str, salary: int):
        super().__init__(name, position, salary)
        self.subordinates = []

    def get_info(self):
        print(f'{self.position} {self.name} имеет зарплату {self.salary} и {len(self.subordinates)} подчиненных.')

    def add_subordinate(self, name: str):
        self.subordinates.append(name)

    def remove_subordinate(self, name: str):
        if name in self.subordinates:
            self.subordinates.remove(name)
        else:
            print(f'{name} отсутствует в списке подчиненных.')
