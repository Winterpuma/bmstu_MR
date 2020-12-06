class Request:
    cur_id = 0

    def __init__(self):
        self.id = Request.cur_id
        Request.cur_id += 1