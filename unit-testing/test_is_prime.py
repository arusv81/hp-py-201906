import unittest
import modules.primeutils as p



class Tests_is_prime(unittest.TestCase):
    def test_0_is_not_prime(self):
        self.assertFalse(p.is_prime(0))
        
    # wrong assert to show a failure
    def test_1_is_not_prime(self):
        self.assertEqual(True,p.is_prime(1),'1 should not be prime')
        
    def test_2_is_prime(self):
        self.assertEqual(True,p.is_prime(2))

    def test_negative_is_same_as_positive(self):
        pos_prime=p.is_prime(17)
        neg_prime=p.is_prime(-17)
        pos_non_prime=p.is_prime(18)
        neg_non_prime=p.is_prime(-18)

        self.assertEqual(pos_prime,neg_prime)
        self.assertEqual(pos_non_prime,neg_non_prime)
        

    def test_4_primes_under_10(self):
        count=0
        for n in range(0,10):
            if p.is_prime(n):
                count+=1
        self.assertEqual(4,count)


if __name__=='__main__':
    unittest.main()
