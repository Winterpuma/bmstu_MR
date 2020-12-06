class Processor:
    def __init__(self, requests_queue, distribution):
        self.work_time_distribution = distribution
        self.busy = False
        self.requests_queue = requests_queue
        self.current_req = None
        self.time_to_finish = 0

    def upd_time(self, dt):
        self.time_to_finish -= dt

        # Еще занят, но время работы закончилось
        if self.busy and self.time_to_finish <= 1e-5:
            self.busy = False
            #print(self.current_req.id, 'proc')
            self.current_req = None
            return 'req fin'

        # Свободен, а в очереди есть заявки
        if not self.busy and len(self.requests_queue) != 0:
            self.current_req = self.requests_queue.pop(0)
            self.time_to_finish = self.work_time_distribution.generate()
            self.busy = True
            return 'req acc'

        return 'pass'
