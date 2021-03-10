import unittest
import functools

rot13_in = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rot13_out = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

def rot13(message):
    result =''
    for symbol in message:
        print(symbol)
        idx = rot13_in.index(symbol)
        result += rot13_out[idx]

    result = functools.reduce(lambda s,x: s + rot13_out[rot13_in.index(x)], message )
    print(res)
    return result

class Test(unittest.TestCase):
    def test_default(self):
        self.assertEqual( rot13("test"),"grfg")
        self.assertEqual( rot13("Test"),"Grfg")
        

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)