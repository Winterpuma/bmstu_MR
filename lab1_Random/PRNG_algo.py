import random

# Метод срединных квадратов
class MiddleSquares:
    _cur = 3485

    def __init__(self, x0):
        self._cur = x0

    def next(self):
        square_str = str(self._cur ** 2)
        start_index = len(square_str) // 4
        finish_index = start_index + 1 if len(square_str) % 2 else start_index
 
        self._cur = int(square_str[start_index:-finish_index])
        
        return self._cur

a = MiddleSquares(3485)


# Линейный конгруэнтный метод
class LinearCongruent:
    a = 106
    c = 1283
    _cur = 7

    def next(self, start, stop):
        stop += 1
        m = stop - start
        self._cur = (self.a * self._cur + self.c) % m + start
        return self._cur

    

b = LinearCongruent()


# Регистр сдвига с линейной обратной связью
class LFSR:
    def __init__(self, links=None):
        # по-умолчанию берем значения для регистра длиной 10
        # считаем, что первый символ самый большой
        self.links = links or (9, 4, 0)
        self.buffer = []
 
        self.__init_buffer()
 
 
    def next(self, start, stop):
        m = stop - start
        self.__shift_bits()
        return self.__convert_to_int() % m + start
 
 
    def __shift_bits(self):
        value = self.__form_bit()
        del self.buffer[len(self.buffer) - 1]
        self.buffer.insert(0, value)
 
 
    def __convert_to_int(self):
        value = "".join([str(item) for item in self.buffer])
        return int(value, 2)
 
 
    def __form_bit(self):
        # возвращает значение следующего бита
        value = 0
 
        for index in self.links:
            value += self.buffer[index]
 
        return value % 2
 
 
    def __init_buffer(self):
        # предзаполнение буфера
        for _ in range(self.links[0] + 1):
            self.buffer.append(random.randint(0, 1))


c = LFSR()
