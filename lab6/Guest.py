from Distributions import NormalDistribution


class Guest:
    cur_id = 0
    work_time_distribution = NormalDistribution(10, 1)

    def __init__(self, guest_type):
        self.id = Guest.cur_id
        self.type = guest_type
        self.eating = False
        self.finished = False

        self.time_to_finish = 0
        Guest.cur_id += 1

        #print(self.id, 'gen', self.type)

    def upd_time(self, dt):
        if self.eating:
            self.time_to_finish -= dt
            if self.time_to_finish <= 1e-5:
                #print(self.id, 'fin eat')
                self.eating = False
                self.finished = True
                return 'fin'

    def eat(self):
        #print(self.id, 'eat')
        self.eating = True
        self.time_to_finish = Guest.work_time_distribution.generate()
