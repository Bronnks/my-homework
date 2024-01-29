import requests
import sys
import time


def retry(attempts: int, delayed: bool):
    def dec(func):
        def wrapper():
            count_req = 0
            while count_req < attempts:
                try:
                    x = func()
                    count_req += 1
                    print(f'Попытка номер {count_req}')
                    print(f'Статус ответа:{x.status_code}')
                except:
                    count_req += 1
                    print(f'Попытка номер {count_req}')
                    print(f'Ошибка - {sys.exc_info()[0]}')
                else:
                    print('Ошибки в этом запросе не было')
                finally:
                    if delayed:
                        sleep = count_req * 2 + 3
                        time.sleep(sleep)
            print(f'Попытки закончились')

        return wrapper

    return dec

# пришлось увеличить timeout, т.к. при значении 0.05 постоянно выбивало ошибку по timeout, а с этим значением
# хоть есть положительные отклики
@retry(attempts=3, delayed=True)
def get_python() -> requests.Response:
    return requests.get('https://python.org', timeout=0.1)


@retry(attempts=3, delayed=False)
def get_python2() -> requests.Response:
    return requests.get('https://python.org', timeout=0.1)


get_python()
get_python2()
