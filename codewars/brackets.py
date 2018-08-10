import unittest

def isBalanced(s):
    s = list(s)
    brackets = {'(': '1', '{': '2', '[': '3', ')': '-1', '}': '-2', ']': '-3'}
    stack = list()
    if int(brackets[s[0]]) < 0:
        return 'NO'
    for item in s:
        print(item)
        if not stack and int(brackets[item]) > 0:
            stack.extend(brackets[item])
            print(stack)
            print('1')
        elif not stack and int(brackets[item]) < 0:
            print('2')
            return 'NO'
        elif int(brackets[item]) > 0:
            stack.extend(brackets[item])
            print('3')
        elif int(brackets[item]) == (int(str(stack[-1])) * -1):
            stack.pop()
            print('4')
        elif int(brackets[item]) < 0 and int(brackets[item]) != (int(str(stack[-1])) * -1):
            print(brackets[item])
            print('-' + str(stack[-1:]))
            print('5')
            return 'NO'
    if stack:
        return 'NO'
    return 'YES'

print(isBalanced('[]{}[{()()((()))}]'))


# class TestCases(unittest.TestCase):
#
#     def test_set_hand_accepts_valid_values(self):
#         self.assertTrue(PokerHand.setHand("2S KH KD JD 5C"))
#
#     def test_constructor_raises_error_for_invalid_values(self):
#         # Value not in array
#         with self.assertRaises(ValueError):
#             PokerHand("0S KH KD JD 5C")
#
# if __name__ == '__main__':
#     unittest.main()