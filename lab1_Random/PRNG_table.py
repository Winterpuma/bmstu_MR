from time import time
from random import randint
        

def generate_random_file(filename, n = 7919):
    numbers = ""

    for i in range(n):
        numbers += str(randint(0, 9))

    f = open(filename, "w")
    f.write(numbers)
    f.close()


class MyTableMethod:

    _randomDigits = ""
    _len = 0
    _cur_index = 0
    
    def __init__(self, filename):
        f = open(filename)
        for line in f.read().split('\n'):
            self._randomDigits += line
        f.close()

        self._len = len(self._randomDigits)

    # [lower; upper]
    def next(self, lower, upper):
        upper -= lower - 1
        n_digit_to_gen = len(str(upper)) + 1
        
        random_number = ""
        self.__upd_cur_index_mod_len(self.__get_1_time_dependent_number())

        for i in range(n_digit_to_gen):
            random_number += self._randomDigits[self._cur_index]
            self.__upd_cur_index_mod_len(self.__get_1_time_dependent_number())

        return (int(random_number) % upper) + lower


    def __upd_cur_index_mod_len(self, step):
        self._cur_index += step
        self._cur_index %= self._len


    def __get_2_time_dependent_numbers(self):
        rand_number = (time() * 1000) % 1000

        start = int(rand_number // 10)
        step = int(rand_number % 10) + 1
        
        return start, step


    def __get_1_time_dependent_number(self):
            rand_number = time() * 1000
            return int(rand_number % 10) + 1
