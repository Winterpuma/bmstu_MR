from random import random
from Guest import Guest


class Generator:
    def __init__(self, queues, saloon, distribution, max_outside_len, max_inside_len, saloon_capacity):
        self.work_time_distribution = distribution
        self.time_to_finish = 0
        self.queues = queues
        self.saloon = saloon
        self.max_outside_len = max_outside_len
        self.max_inside_len = max_inside_len
        self.saloon_capacity = saloon_capacity

    def upd_time(self, dt):
        self.time_to_finish -= dt

        if self.time_to_finish <= 1e-5:
            self.time_to_finish += self.work_time_distribution.generate()
            if random() < 0.3:
                # еда с собой
                if len(self.queues['outside']) <= self.max_outside_len:
                    self.queues['outside'].append(Guest('outside'))
                else:
                    return 'lost out'
            else:
                if len(self.queues['inside']) <= self.max_inside_len and len(self.saloon) < self.saloon_capacity:
                    new_guest = Guest('inside')
                    self.queues['inside'].append(new_guest)
                    self.saloon.append(new_guest)
                else:
                    if len(self.saloon) >= self.saloon_capacity:
                        return 'lost saloon'
                    return 'lost in'
            return 'gen'

        return None
