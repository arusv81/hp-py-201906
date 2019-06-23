

import modules.primeutils as p

lo=int(input('lo?'))
hi=int(input('hi?'))

count=p.prime_count(lo,hi)

print('total primes in range {0} and {1} is {2}'.format(lo,hi,count))

