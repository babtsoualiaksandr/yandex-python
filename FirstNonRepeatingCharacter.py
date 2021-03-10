import unittest
from collections import deque


def first_non_repeating_letter(input_string: str):
    for iter in input_string:
        if input_string.upper().count(iter.upper()) == 1:
            return iter
    return ''
from time_measure import measure_time
measure_first = measure_time(first_non_repeating_letter)
print(measure_first('kjhhkWFFVnnnjjjk'))

       




