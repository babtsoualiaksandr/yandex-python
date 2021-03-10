import unittest

def rgb(r, g, b):
    # your code here :)
    def toHex(dec):
        if dec < 5:
            return ''.join(hex(dec).split('x')).upper()
        return ''.join(hex(dec).split('x')).upper().replace('0', '')

    def valid(x):
        if (x > -1 and x < 256):
            return x
        elif x < 0:
            return 0
        elif x > 255:
            return 255

    def int_to_str_hex(x):
        
        return str(toHex(valid(x)))

    result = int_to_str_hex(r) + int_to_str_hex(g) + int_to_str_hex(b)
    return result


def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb_(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))





class WidgetTestCase(unittest.TestCase):
    def test_default(self):
        self.assertEqual(rgb_(0,0,0),"000000", "testing zero values")
        self.assertEqual(rgb_(1,2,3),"010203", "testing near zero values")
        self.assertEqual(rgb_(255,255,255), "FFFFFF", "testing max values")
        self.assertEqual(rgb_(254,253,252), "FEFDFC", "testing near max values")
        self.assertEqual(rgb_(-20,275,125), "00FF7D", "testing out of range values")


if __name__ == '__main__':
    unittest.main()

