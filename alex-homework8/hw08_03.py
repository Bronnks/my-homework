from faker import Faker
locale_list = ['en_US', 'it_IT', 'de_DE', 'es-ES', 'fr_FR']
with open('fake.txt', 'w+', encoding="utf-8") as f:
    for i in locale_list:
        f.write(Faker(i).text())
        f.write('\n----------\n')
