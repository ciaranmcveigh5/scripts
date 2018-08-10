import unittest
import random

def add(x, y):
    result = x + y
    return result

def generatePrivateKey():
    privateKey = []
    while result <= 100:
        for i in range(1, 256):
            rand = random.random()
            if rand >= 0.5:
                privateKey.append('1')
            else:
                privateKey.append('0')
        result = ''.join(privateKey)
        result = int(result, 2)
    return result

class TestMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_generate_private_key_length(self):
        self.assertEqual(len(generatePrivateKey()), 255)

if __name__ == '__main__':
    unittest.main()
