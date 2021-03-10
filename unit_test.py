"""
    pytest -q /Users/alexander/Documents/yandex/test_1/test/unit_test.py -s
"""
from FirstNonRepeatingCharacter import first_non_repeating_letter

from RomanNumerals import RomanNumerals




class TestClass:
    def test_first_non_repeating_letter(self):
        print('Basic Tests')
        print('should handle simple tests')
        assert first_non_repeating_letter('a') == 'a'
        assert (first_non_repeating_letter('stress') == 't')
        assert (first_non_repeating_letter('moonmen') == 'e')

        print('should handle empty strings')
        assert (first_non_repeating_letter('') == '')

        print('should handle all repeating strings') 
        assert (first_non_repeating_letter('abba') == '')
        assert (first_non_repeating_letter('aa') == '')

        print('should handle odd characters')
        assert (first_non_repeating_letter('~><#~><') == '#')
        assert (first_non_repeating_letter('hello world == eh?') == 'w')

        print('should handle letter cases')
        assert (first_non_repeating_letter('sTreSS') == 'T')
        assert (first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!') == ',')


    def test_RomanNumerals(self):
        assert (RomanNumerals.to_roman(1000) == 'M' )
        assert (RomanNumerals.to_roman(1990) == 'MCMXC')

        assert (RomanNumerals.from_roman('XXI') == 21 )
        assert (RomanNumerals.from_roman('MMVIII') == 2008)