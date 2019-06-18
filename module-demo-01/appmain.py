'''
1. accept a range from user
2. find all primes in the range
3. find the sum and average of all primes
4. ask user if they want to try another round
'''



def main():
    
    repeat=True
    while repeat:
        lo= read_int('min? ',2)
        hi= read_int('max?')
        primes=prime_range(lo,hi)
        total=sum(*primes)
        avg=average(*primes)
        print('total primes found is {}'.format(len(primes)))
        print('sum of primes {}'.format(total))
        print('average of primes {}'.format(avg))

        repeat=read_bool('try again?',False)
    


main()


