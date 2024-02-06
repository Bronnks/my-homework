from typing import Self, Any
class Task:

    def __init__(self) -> None:
        self.task_list = []

    def add_task(self, value: str) -> None:
        try:
            if len(self.task_list) > 19:
                raise Exception
            else:
                self.task_list.append(value)
        except Exception:
            print('Список задач переполнен.')

    def remove_task(self, value: str) -> None:
        if not self.task_list:
            print('Список пуст, добавьте задачу сначала.')
            return
        try:
            self.task_list.remove(value)
        except ValueError:
            print(f'Задачи {value} нет в списке.')

    def check_empty_list(self):
        if not self.task_list:
            print('Список пуст.')
        else:
            print('В списке задач есть хотя бы одна задача.')

    def clear_list(self):
        self.task_list.clear()

    def len_list(self):
        print(f'Длина списка задач: {len(self.task_list)}')
