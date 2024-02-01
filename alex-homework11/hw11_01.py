class Task:
    task_list = []

    def __init__(self, name):
        self.name = name

    def add_task(self):
        try:
            if len(Task.task_list) > 19:
                raise Exception
            else:
                Task.task_list.append(self.name)
        except Exception:
            print('Список задач переполнен.')

    def remove_task(self):
        if not Task.task_list:
            print('Список пуст, добавьте задачу сначала.')
            return
        try:
            Task.task_list.remove(self.name)
        except ValueError:
            print(f'Задачи {self.name} нет в списке.')

    @staticmethod
    def check_empty_list():
        if not Task.task_list:
            print('Список пуст.')
        else:
            print('В списке задач есть хотя бы одна задача.')

    @staticmethod
    def clear_list():
        Task.task_list.clear()

    @staticmethod
    def len_list():
        print(f'Длина списка задач: {len(Task.task_list)}')
