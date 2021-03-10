class RomanNumerals:
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
        1 : 'I',
        5 : 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D' ,
        1000: 'M'
    }

    @classmethod
    def to_roman(cls, input_int):
        result = ''
        print(input_int)
        if input_int in cls.from_to.keys():
            return cls.from_to[input_int]
        thousand = input_int // 1000
        rest_1000 = input_int - thousand * 1000
        print(rest_1000)
        result += result + ('M'* thousand)

        five_hundred = rest_1000 // 500
        rest_500 = rest_1000 - five_hundred * 500
        print(rest_500)
        result += result + ('D'* five_hundred)

        centurion = rest_500 // 100
        rest_100 = rest_500 - centurion * 100
        print(rest_100)
        result += result + ('C'* centurion)


        fifty = rest_100 // 50
        rest_50 = rest_100 - fifty * 50
        print(rest_50)
        result += result + ('L'* five_hundred)

        ten = rest_50 // 10
        rest_10 = rest_50 - ten * 10
        print(rest_10)
        result += result + ('X'* five_hundred)

        five = rest_50 // 5
        rest_5 = rest_50 - five * 5
        print(rest_5)
        result += result + ('V'* five_hundred)

        one = rest_5 // 1
        rest_1 = rest_5 - one * 1
        print(rest_1)
        result = ('M'* thousand) + ('D'* five_hundred) + ('C'* centurion) + ('L'* five_hundred) + ('I'* five_hundred)

        print(thousand, five_hundred, centurion, fifty, ten, five, one)
        print(result)

        return result

    @classmethod
    def from_roman(cls, input_symbal):
        input_symbal = 'M'
        return to_from['input_symbal']
