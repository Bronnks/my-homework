class Product:
    def __init__(self, name: str, price: int, description: str):
        self.name = name
        self.price = price
        self.description = description


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item: object):
        self.items.append(item)

    def remove_item(self, item: object):
        if item in self.items:
            self.items.remove(item)
        else:
            print('Такого товара нет в корзине.')

    def show_items(self):
        if len(self.items) == 0:
            print('Корзина пока что пустая.')
        else:
            print('В корзине находятся:')
            for i in self.items:
                print(f'\t\t\t\t\t{i.name}')

    def get_total(self):
        count = sum(i.price for i in self.items)
        print(f'Общая стоимость товаров в корзине: {count}.')
