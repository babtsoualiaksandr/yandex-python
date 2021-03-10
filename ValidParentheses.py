import unittest
from collections import deque


def valid_parentheses(input_string):
    brackets = {
        ')': '(',
        ']': '['
    }

    def isClosedBracket(ch):
        return ''.join(brackets.keys()).find(ch) > -1
    
    def isOpenedBracket(ch):
        return ''.join(brackets.values()).find(ch) > -1

    myStack = deque()
    for symbol in input_string:
        if (isClosedBracket(symbol) or isOpenedBracket(symbol)):
            if isClosedBracket(symbol) and len(myStack) == 0:
                return False
            if isClosedBracket(symbol):
                if (brackets[symbol] != myStack.pop()):
                    return False
            else:
                myStack.append(symbol)
        else:
            pass
    return (len(myStack)==0)



class Test(unittest.TestCase):
    def test_default(self):
        self.assertEqual(valid_parentheses("skdhajshdkja()"), True)
        self.assertEqual(valid_parentheses("  ("), False)
        self.assertEqual(valid_parentheses(")test"), False)
        self.assertEqual(valid_parentheses(""), True)
        self.assertEqual(valid_parentheses("hi())("), False)
        self.assertEqual(valid_parentheses("hi(hi)()"), True)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
    unittest.TextTestRunner().run(suite)
