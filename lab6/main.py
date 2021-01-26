from time import time
from Distributions import EvenDistribution, NormalDistribution
from Generator import Generator
from Cashier import Cashier
from Cook import Cook

unit_of_time = 0.1  # еденица системного времени - 0.1 минуты


# Один тик времени
def one_step(saloon, generator, cashiers, cooks, request_info, generate_new=True):
    # Обновление генератора
    if generate_new:
        res = generator.upd_time(unit_of_time)
        if res == 'gen':
            #print(len(saloon))
            request_info['generated'] += 1
        elif res == 'lost out':
            request_info['generated'] += 1
            request_info['lost outside'] += 1
        elif res == 'lost in':
            request_info['generated'] += 1
            request_info['lost inside'] += 1
        elif res == 'lost saloon':
            request_info['generated'] += 1
            request_info['lost saloon is full'] += 1

    # Обновление касс
    for cur_cashier in cashiers:
        cur_cashier.upd_time(unit_of_time)

    # Обновление поваров
    for cur_cook in cooks:
        res = cur_cook.upd_time(unit_of_time)
        if res == 'outside':  # заявка была обработана
            request_info['processed_out'] += 1

    # Обновление посетителей в заведении
    for guest in saloon:
        res = guest.upd_time(unit_of_time)
        if res == 'fin':
            request_info['processed_in'] += 1

    # Поевшие посетители уходят
    for i in range(len(saloon) -1, -1, -1):
        if saloon[i].finished:
            del saloon[i]


def modeling(saloon, generator, cashiers, cooks, total_incoming_requests):
    request_info = {'generated': 0, 'lost outside': 0, 'lost inside': 0, 'lost saloon is full': 0,
                    'processed_in': 0, 'processed_out': 0}

    prevent_inf_loop = 0
    max_loop = 10000000

    # Пока не сгенерируется нужное число заявок
    while request_info['generated'] < total_incoming_requests and prevent_inf_loop < max_loop:
        one_step(saloon, generator, cashiers, cooks, request_info)
        prevent_inf_loop += 1

    # Пока все сгенерированные заявки не пройдут систему
    while (request_info['lost inside'] + request_info['lost outside'] + request_info['lost saloon is full'] +
           request_info['processed_in'] + request_info['processed_out']) < total_incoming_requests \
            and prevent_inf_loop < max_loop:
        one_step(saloon, generator, cashiers, cooks, request_info, False)
        prevent_inf_loop += 1

    return request_info


def main():
    queue_inside = []
    queue_outside = []
    main_queue = {'inside': queue_inside, 'outside': queue_outside}
    saloon = []

    client_generator = Generator(main_queue, saloon, EvenDistribution(1, 3),
                                 max_inside_len=15, max_outside_len=4, saloon_capacity=50)

    queue_cook = []

    cashiers = [
        Cashier(queue_inside, queue_cook, EvenDistribution(2, 6)),
        Cashier(queue_outside, queue_cook, EvenDistribution(2, 6))
    ]

    cooks = [
        Cook(queue_cook, NormalDistribution(7, 1)),
        Cook(queue_cook, NormalDistribution(7, 1))
    ]

    total_requests = 10000

    t_start = time()
    res = modeling(saloon, client_generator, cashiers, cooks, total_requests)

    print('time seconds', time() - t_start)
    for key in res.keys():
        print(key, res[key])

    print('lost', (res['lost inside'] + res['lost outside'] + res['lost saloon is full']) / total_requests)


if __name__ == '__main__':
    main()
