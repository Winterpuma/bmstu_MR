class Cashier:
    cur_id = 0

    def __init__(self, get_from, send_to, distribution):
        self.work_time_distribution = distribution
        self.busy = False
        self.get_from = get_from
        self.send_to = send_to
        self.current_req = None
        self.time_to_finish = 0

        self.id = Cashier.cur_id
        Cashier.cur_id += 1

    def upd_time(self, dt):
        if self.busy:
            self.time_to_finish -= dt
            if self.time_to_finish <= 1e-5:
                #print(self.current_req.id, 'cash', self.id, 'finished')
                self.send_to.append(self.current_req)
                self.busy = False
                self.current_req = None
        if not self.busy and len(self.get_from):
            self.busy = True
            self.current_req = self.get_from.pop(0)
            #print(self.current_req.id, 'cash', self.id, 'accepted')
            self.time_to_finish += self.work_time_distribution.generate()
