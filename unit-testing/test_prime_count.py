import unittest
import modules.primeutils as p

class Tests_prime_count(unittest.TestCase):

    def test_4_primes_between_2_and_10(self):
        result=p.prime_count(2,10)
        self.assertEqual(4,result)

    def test_25_primes_between_2_and_100(self):
        result=p.prime_count(2,100)
        self.assertEqual(25,result)

    def test_max_should_be_greater_than_min(self):
        with self.assertRaises(Exception) as cm:
            p.prime_count(100,1)
        
        e=cm.exception

        self.assertIsInstance(e,p.RangeError)

if __name__=='__main__':
    unittest.main()
