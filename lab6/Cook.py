class Cook:
    cur_id = 0

    def __init__(self, requests_queue, distribution):
        self.work_time_distribution = distribution
        self.busy = False
        self.requests_queue = requests_queue
        self.current_req = None
        self.time_to_finish = 0

        self.id = Cook.cur_id
        Cook.cur_id += 1

    def upd_time(self, dt):
        res = ''

        if self.busy:
            self.time_to_finish -= dt

            # Еще занят, но время работы закончилось
            if self.time_to_finish <= 1e-5:
                #print(self.current_req.id, 'cook', self.id, 'fin')
                res = self.current_req.type
                if res == 'inside':
                    self.current_req.eat()
                self.busy = False
                self.current_req = None

        # Свободен, а в очереди есть заявки
        if not self.busy and len(self.requests_queue):
            self.current_req = self.requests_queue.pop(0)
            #print(self.current_req.id, 'cook', self.id, 'accepted')
            self.time_to_finish += self.work_time_distribution.generate()
            self.busy = True

        return res
