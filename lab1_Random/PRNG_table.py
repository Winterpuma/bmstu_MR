from time import time


class Table:

    _randomDigits = ""
    _len = 0
    _cur_index = 0
    
    def __init__(self, filename):
        f = open(filename)
        for line in f.read().split('\n'):
            self._randomDigits += line
        f.close()

        self._len = len(self._randomDigits)

    # [lower; upper)
    def next(self, lower, upper):

        rand_2_dig_number = (time() * 100000) % 1000

        start = int(rand_2_dig_number // 10)
        step = int(rand_2_dig_number % 10)

        upper -= lower
        n_digit_to_gen = len(str(upper)) + 1
        
        random_number = ""
        self.__upd_cur_index_mod_len(start)
        for i in range(n_digit_to_gen):
            random_number += self._randomDigits[self._cur_index]
            self.__upd_cur_index_mod_len(step)
        
        return (int(random_number) % upper) + lower

    def __upd_cur_index_mod_len(self, step):
        self._cur_index += step
        self._cur_index %= self._len


if __name__ == "__main__":
    a = Table("odd_table.txt")
    for i in range(100):
        print(a.next(100, 125))
