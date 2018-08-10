# Task
# Since the weather was good, some students decided to go for a walk in the park after the first lectures of the new
# academic year. There they saw a squirrel, which climbed a tree in a spiral at a constant angle to the ground. They
# calculated that in one loop the squirrel climbes h meters (vertical height), the height of the tree is equal to H
# (v in Ruby), and the length of its circumference equals S.
#
# These calculations were exhausting, so now the students need your help to figure out how many meters the path length
# of squirrel climbed when it reached the tree top. The result should be rounded to 4 decimal places.
#
# Code Limit
# Less than 52 characters (JavaScript & Python)
#
# Less than 48 characters (Ruby)
#
# Example
# For h = 4, H = 16, S = 3, the output should be 20.
#
# For h = 8, H = 9, S = 37, the output should be 42.5869.

import unittest
import math



# def squirrel(h, H, S):
#     c = h**2 + S**2
#     hypo = math.sqrt(c)
#     ratio = H/h
#     distance = round((ratio * hypo), 4)
#     return distance

def squirrel(h, H, S):
    c = math.sqrt(h**2 + S**2)
    print(h)
    print(H/h)
    d = round(((H/h) * c), 4)
    return d

squirrel=lambda h,H,S:round(H*abs(1j+S/h),4)


class TestMethods(unittest.TestCase):

    def test(self):
        self.assertEqual(squirrel(4, 16, 3), 20)

if __name__ == '__main__':
    unittest.main()