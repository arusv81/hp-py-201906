'''
1. accept a range from user
2. find all primes in the range
3. find the sum and average of all primes
4. ask user if they want to try another round
'''
import maths
import consoleutils
import primes



def main():
    global primes
    repeat=True
    while repeat:
        lo= consoleutils.read_int('min? ',2)
        hi= consoleutils.read_int('max?')
        
        primes=primes.prime_range(lo,hi)

        total=maths.sum(*primes)
        avg=maths.average(*primes)
        print('primes={}'.format(primes))
        print('total primes found is {}'.format(len(primes)))
        print('sum of primes {}'.format(total))
        print('average of primes {}'.format(avg))

        repeat=consoleutils.read_bool('try again?',True)
    


main()


