

def is_prime(number):
    if number<2:
        return False
    
    for divisor in range(2,number):
        if number%divisor==0:
            return False

    return True


def prime_range(min,max=None):

    if max is None:
        min,max=2,min

    result=[]

    for number in range(min,max):
        if is_prime(number):
            result.append(number)

    return result


    