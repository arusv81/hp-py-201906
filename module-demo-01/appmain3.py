'''
1. accept a range from user
2. find all primes in the range
3. find the sum and average of all primes
4. ask user if they want to try another round
'''

import consoleutils as cu
import maths
from primes import prime_range

def main():
    print('starting module {}'.format(__name__))
    repeat=True
    while repeat:
        lo=cu. read_int('min? ',2)
        hi=cu. read_int('max?')
        
        primes=prime_range(lo,hi)

        total=maths.sum(*primes) 
        avg=maths.average(*primes)
        smallest=min(*primes); 
        print('primes={}'.format(primes))
        print('total primes found is {}'.format(len(primes)))
        print('sum of primes {}'.format(total))
        print('average of primes {}'.format(avg))
        print('smallest prime in series is {}'.format(smallest))
        repeat=cu.read_bool('try again?',True)
    


main()


