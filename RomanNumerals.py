import app_logger
class RomanNumerals:
    logger = app_logger.get_logger(__name__)
    to_from = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    from_to = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    @classmethod
    def to_roman(cls, input_int):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while input_int > 0:
            for _ in range(input_int // val[i]):
                roman_num += syb[i]
                input_int -= val[i]
            i += 1
        return roman_num

    @classmethod
    def from_roman(cls, input_symbal):
        cls.logger.info(f"log from classmethod {input_symbal} ")
        result_int = 0
        for iter in input_symbal:
            result_int += cls.to_from[iter]
        cls.logger.warning(f"log from classmethod result {result_int} ")
        return result_int
