from time import time
from EvenDistribution import EvenDistribution
from Generator import Generator
from Operator import Operator
from Processor import Processor

unit_of_time = 0.01  # еденица системного времени - 0.01 минуты


# Возвращает индекс первого свободного оператора или -1
def pick_operator(operators):
    for i in range(len(operators)):
        if not operators[i].busy:
            return i
    return -1


# Один тик времени
def one_step(generator, operators, processors, request_info, generate_new=True):
    # Обновление генератора
    if generate_new:
        request = generator.upd_time(unit_of_time)
        if request:
            #print(request.id, 'gen')
            request_info['generated'] += 1
            i_operator = pick_operator(operators)
            if i_operator == -1: # все операторы заняты
                #print(request.id, 'lost')
                request_info['lost'] += 1
            else:
                operators[i_operator].accept_request(request)

    # Обновление операторов
    for cur_operator in operators:
        cur_operator.upd_time(unit_of_time)

    # Обновление компьютеров
    for cur_processor in processors:
        res = cur_processor.upd_time(unit_of_time)
        if res == 'req fin':  # заявка была обработана
            request_info['processed'] += 1


def modeling(generator, operators, processors, total_incoming_requests):
    request_info = {'generated': 0, 'lost': 0, 'processed': 0}

    # Пока не сгенерируется нужное число заявок
    while request_info['generated'] < total_incoming_requests:
        one_step(generator, operators, processors, request_info)

    # Пока все сгенерированные заявки не пройдут систему
    while request_info['lost'] + request_info['processed'] < total_incoming_requests:
        one_step(generator, operators, processors, request_info, False)

    return request_info


def main():
    client_generator = Generator(EvenDistribution(8, 12))

    first_queue = []
    second_queue = []

    operators = [
        Operator(first_queue, EvenDistribution(15, 25)),    # самый производительный
        Operator(first_queue, EvenDistribution(30, 50)),
        Operator(second_queue, EvenDistribution(20, 60))    # наименее производительный
    ]

    processors = [
        Processor(first_queue, EvenDistribution(15, 15)),   # ровно 15 минут
        Processor(second_queue, EvenDistribution(30, 30))   # ровно 30 минут
    ]

    total_requests = 300

    t_start = time()
    res = modeling(client_generator, operators, processors, total_requests)

    print('time seconds', time() - t_start)
    for key in res.keys():
        print(key, res[key])

    print('lost', res['lost'] / total_requests)


if __name__ == '__main__':
    main()
