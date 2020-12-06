from Request import Request


class Generator:
    def __init__(self, distribution):
        self.work_time_distribution = distribution
        self.time_to_finish = 0

    def upd_time(self, dt):
        self.time_to_finish -= dt

        if self.time_to_finish <= 1e-5:
            self.time_to_finish = self.work_time_distribution.generate()
            return Request()

        return None
