from gun import Gun
from tank import Panzer, Commander, Gunner, Crew


c1 = Commander('Jack', 'Daniels', 'ст.лейтенант', 'замхозобеспечение')
c2 = Commander('Brad', 'Pitt', 'ст.лейтенант', 'политрук')
g1 = Gunner('John', 'Travolta', 'сержант', 'артиллерист')
g2 = Gunner('Mat', 'Daimon', 'прапорщик', 'повар')
crew1 = Crew(c1,g1)
crew2 = Crew(c2,g2)
player1 = Panzer('ИС-2', Gun(122, 40), 90, 600, crew1)
player2 = Panzer('Тигр', Gun(88, 55), 120, 650, crew2)

AMMO_TYPES = ['фугасный', 'кумулятивный', 'подкалиберный']
ARMOUR_TYPES = ['гомогенная', 'разнесенная', 'комбинированная']


while True:
    # ================================= ХОД ПЕРВОГО ИГРОКА =========================================
    player1.crew.condition_status()
    if player1.crew.comm_status_ok:
        print('========== Игрок 1 ============>')
        selected_ammo = -1
        while player1.loaded_ammo == None:
            while (selected_ammo < 0 or selected_ammo > 2):
                print('0 - фугасный')
                print('1 - кумулятивный')
                print('2 - бронебойный')

                selected_ammo = int(input('Выбрать снаряд:'))

            player1.load_gun(AMMO_TYPES[selected_ammo])

        selected_armour = -1
        while (selected_armour < 0 or selected_armour > 2):
            print('0 - гомогенная')
            print('1 - разнесенная')
            print('2 - комбинированная')

            selected_armour = int(input('Выбрать броню:'))

        player1.select_armour(ARMOUR_TYPES[selected_armour])
        print('\n')
        print(f'Игрок 1 - текущее состояние: {player1}')
        print('\n')
        print(f'Нажмите Enter для выстрела')
        command = input()

        fired_ammo = player1.shoot()
        if fired_ammo:
            player2.handle_hit(fired_ammo)

        if player2.get_health() <= 0:
            print('Танк игрока 2 уничтожен')
            break
    else:
        player1.crew.list[0].condition = 'в порядке'
        print('Командир контужен, первый игрок пропускает ход.')

    # ================================= ХОД ВТОРОГО ИГРОКА =========================================
    player2.crew.condition_status()
    if player2.crew.comm_status_ok:
        print("========== Игрок 2 ============>")
        selected_ammo = -1
        while player2.loaded_ammo == None:
            while (selected_ammo < 0 or selected_ammo > 2):
                print('0 - фугасный')
                print('1 - кумулятивный')
                print('2 - бронебойный')

                selected_ammo = int(input('Выбрать снаряд:'))

            player2.load_gun(AMMO_TYPES[selected_ammo])

        selected_armour = -1
        while selected_armour < 0 or selected_armour > 2:
            print('0 - гомогенная')
            print('1 - разнесенная')
            print('2 - комбинированная')

            selected_armour = int(input('Выбрать броню:'))

        player2.select_armour(ARMOUR_TYPES[selected_armour])

        print('\n')
        print(f'Игрок 2 - текущее состояние: {player2}')
        print('\n')
        print(f'Нажмите Enter для выстрела')
        command = input()

        fired_ammo = player2.shoot()
        if fired_ammo:
            player1.handle_hit(fired_ammo)

        if player1.get_health() <= 0:
            print('Танк игрока 1 уничтожен')
            break
    else:
        player2.crew.list[0].condition = 'в порядке'
        print('Командир контужен, второй игрок пропускает ход.')
