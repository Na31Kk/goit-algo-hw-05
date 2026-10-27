import re
from typing import Callable

def generator_numbers(text: str):
    """Шукає в тексті дійсні числа та повертає їх як генератор."""
    pattern = r"\d+\.\d+"
    result = re.findall(pattern, text)
    for num in result:
        yield float(num)

def sum_profit(text: str, func: Callable):
    """Рахує загальну суму чисел, отриманих за допомогою функції-генератора."""
    return sum(func(text))
     
text = "Загальний дохід працівника складається з декількох частин: " \
"1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

