'''
1. accept a range from user
2. find all primes in the range
3. find the sum and average of all primes
4. ask user if they want to try another round
'''
from maths import *
from consoleutils import read_int, read_bool

import primes as p

from primes import prime_range



def main():
    
    repeat=True
    while repeat:
        lo= read_int('min? ',2)
        hi= read_int('max?')
        
        primes=p.prime_range(lo,hi)

        total=sum(*primes) #maths.sum has replaced builtin sum function
        avg=average(*primes) #maths.average() has no conflict
        smallest=min(*primes); #maths.min() overwrites a more useful builtin min
        print('primes={}'.format(primes))
        print('total primes found is {}'.format(len(primes)))
        print('sum of primes {}'.format(total))
        print('average of primes {}'.format(avg))
        print('smallest prime in series is {}'.format(smallest))
        repeat=read_bool('try again?',True)
    


main()


