import random


def step_model(generator, processor, total_tasks=0, repeat=0, step=0.001):
    processed_tasks = 0
    t_curr = step
    t_gen = generator.generate()
    t_gen_prev = t_proc = 0
    cur_queue_len = max_queue_len = 0
    free = True

    while processed_tasks < total_tasks:
        # Генератор
        if t_curr > t_gen:
            cur_queue_len += 1
            if cur_queue_len > max_queue_len:
                max_queue_len = cur_queue_len
            t_gen_prev = t_gen
            t_gen += generator.generate()

        # Обработчик
        if t_curr > t_proc:
            if cur_queue_len > 0:
                was_free = free
                if free:
                    free = False
                else:
                    processed_tasks += 1
                    if random.randint(1, 100) <= repeat:
                        cur_queue_len += 1
                cur_queue_len -= 1
                if was_free:
                    t_proc = t_gen_prev + processor.generate()
                else:
                    t_proc += processor.generate()
            else:
                free = True
        t_curr += step

    return max_queue_len
