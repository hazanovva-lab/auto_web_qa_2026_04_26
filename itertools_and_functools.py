import datetime
import time
from datetime import datetime
from time import sleep
from functools import lru_cache
#
# example = [[1, 2, 3, 4, 5], ["some", "something"]]
# """
# Встроенная функция chain делает из несколько списков один большой список.
# Встроенная функция repieat которая выполяняет какое значение нам нужно повторить, второе сколько раз.
# Встроенная функция combinations в котором первый аргумент передает массив значение, второй аргумент из скольки значение должно быть комбинирование.
# Встроенная функция permutations перебор всех комбинаций
# """
# # print(list(itertools.chain(*example)))
# # print(list(itertools.repeat(1, 5)))
# # print(list(itertools.combinations([1, 2, 3, 4], 2)))
# print(list(itertools.permutations([1, 2, 3, 4], 2)))
@lru_cache()
def slow_func(a: int):
    sleep(1)
    return a

print("Start")
start = datetime.now()

for i in range(5):
    slow_func(5)

print(f"End: {datetime.now() - start}")
