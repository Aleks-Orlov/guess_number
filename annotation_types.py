from math import sqrt
from typing import Optional, Union


def add_numbers(dig_1: int, dig_2: int) -> int:
    return dig_1 + dig_2


def calculate_square_root(number: Union[int, float]) -> float:
    return sqrt(number)


def calc(your_number: Union[int, float]) -> Optional[str]:
    if your_number <= 0:
        return    
    calculate = calculate_square_root(your_number)
    return (f'Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {calculate}')


digit_1 = 10
digit_2 = 5

print('Сумма чисел: ', add_numbers(digit_1, digit_2))

print(calc(25.5))
