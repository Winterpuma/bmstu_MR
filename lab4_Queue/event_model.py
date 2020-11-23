from random import randint


def event_model(generator, processor, total_tasks=0, repeat=0):
    processed_tasks = 0
    cur_queue_len = max_queue_len = 0
    events = [[generator.generate(), 'g']]
    free, process_flag = True, False

    while processed_tasks < total_tasks:
        event = events.pop(0)
        # Генератор
        if event[1] == 'g':
            cur_queue_len += 1
            if cur_queue_len > max_queue_len:
                max_queue_len = cur_queue_len
            add_event(events, [event[0] + generator.generate(), 'g'])
            if free:
                process_flag = True
        # Обработчик
        elif event[1] == 'p':
            processed_tasks += 1
            if randint(1, 100) <= repeat:
                cur_queue_len += 1
            process_flag = True

        if process_flag:
            if cur_queue_len > 0:
                cur_queue_len -= 1
                add_event(events, [event[0] + processor.generate(), 'p'])
                free = False
            else:
                free = True
            process_flag = False

    return max_queue_len


def add_event(events, event: list):
    i = 0
    while i < len(events) and events[i][0] < event[0]:
        i += 1
    if 0 < i < len(events):
        events.insert(i - 1, event)
    else:
        events.insert(i, event)
