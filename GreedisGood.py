import unittest
import functools


rules = {
    (1, 3): 1000,
    (6, 3): 600,
    (5, 3): 500,
    (4, 3): 400,
    (3, 3): 300,
    (2, 3): 200,
    (1, 1): 100,
    (5, 1): 50,
    (1, 2): 200,
    (5, 2): 100   
}

key = [1,2,3,4,5,6]

def score(dice):
    print('='*13,dice)
    x = dict((x, dice.count(x)) for x in set(dice) if dice.count(x) > 0)
    print(type(x), x)
    
    sum = 0

    for iter in x.items():
        val, count = iter
        print(val, count, val in key, '***', key)        
        if (val in key) and count > 3:
            x = (val, 3)
        else:      
            x = (val, count)

        print('=================******',x, rules.keys())
        if (x in rules.keys()):
            sum += rules[x]
        
        if (val in [1,5]) and count - 3 >=1:
            x = (val, 1)
            if (x in rules.keys()):
                sum += rules[x]
        

    return sum


class Test(unittest.TestCase):
    def test_default(self):
        self.assertEqual( score( [2, 3, 4, 6, 2] ), 0)
        self.assertEqual( score(  [4, 4, 4, 3, 3] ), 400)
        self.assertEqual(score([2, 4, 4, 5, 4]), 450)
        self.assertEqual(score([3, 3, 3, 3, 3]), 300)
        self.assertEqual(score([1, 1, 1, 1, 3]), 1100)
        self.assertEqual(score([4, 1, 1, 6, 5]), 250)
        


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)


    