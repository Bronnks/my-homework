from faker import Faker
import json

fake = Faker()


def create_student():
    test = {'name': fake.first_name(),
            'lastname': fake.last_name(),
            'age': fake.random_int(min=18, max=45),
            'course': 1,
            'group': 1,
            'subjects': {'python': {'score': fake.random_int(min=1, max=10)},
                         'JS': {'score': fake.random_int(min=1, max=10)},
                         'pascal': {'score': fake.random_int(min=1, max=10)},
                         'java': {'score': fake.random_int(min=1, max=10)}
                         }
            }
    return test


def create_json():
    with open('students.json', 'w+', encoding="utf-8") as f:
        test = {}
        for i in range(5):
            test[i] = create_student()
        json.dump(test, f)


def calculate_scores(s):
    sum_scores = 0
    x = clas[str(s)]
    sum_scores += x['subjects']['python']['score']
    sum_scores += x['subjects']['JS']['score']
    sum_scores += x['subjects']['pascal']['score']
    sum_scores += x['subjects']['java']['score']
    return sum_scores / 4


create_json()
with open('students.json', encoding="utf-8") as f:
    clas = json.load(f)
    av_score = [calculate_scores(i) for i in range(5)]
    for i in range(1, 6):
        print(f'Средний бал {i} студента - {av_score[i - 1]}')
    print(f'Средний бал по группе - {sum(av_score) / 5}')

# С json раньше не работал, поэтому решение полная импровизация, но вроде работает
