class Operator:
    def __init__(self, send_to, distribution):
        self.work_time_distribution = distribution
        self.busy = False
        self.send_to = send_to
        self.current_req = None
        self.time_to_finish = 0

    def accept_request(self, request):
        self.busy = True
        self.current_req = request
        self.time_to_finish = self.work_time_distribution.generate()

    def finish_cur_request(self):
        self.send_to.append(self.current_req)
        self.busy = False
        self.current_req = None

    def upd_time(self, dt):
        self.time_to_finish -= dt
        if self.busy and self.time_to_finish <= 1e-5:
            self.finish_cur_request()
            return 'req fin'
        return 'pass'
