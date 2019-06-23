def is_prime(number):
    '''
    checks if the given number is prime or not

    >>> is_prime(0)
    False

    >>> is_prime(2)
    True

    >>> is_prime(9)
    True

    >>> is_prime(-4)
    False

    >>> is_prime(-2)
    True
    '''
    number=abs(number)

    if number<2: return False

    for checker in range(2,number):
        if number%checker==0:
            return False
    return True

class RangeError(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.error_message=message
        

def prime_count(min,max):
    '''
    Finds the total primes in the given range.abs
    Note: min<max

    >>> prime_count(2,10)
    4
    >>> prime_count(2,100)
    25

    >>> prime_count(100,2)
    Traceback (most recent call last):
     ...
    modules.primeutils.RangeError: min[100] should be less than max[2]
    '''
    if max<=min:
         raise RangeError('min[{}] should be less than max[{}]'.format(min,max)) #ArgumentError('min[{}] should be less than max[{}]'.format(min,max))

    count=0
    for number in range(min,max):
        if is_prime(number): 
            count+=1

    return count




