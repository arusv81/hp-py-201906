

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

    
def test():
    print('executing test from primes: {}'\
        .format(__name__))
    is_prime_test_data={ 2: True, 3: True, -2: True, 9: False, 21: False, 17: True};

    total=0
    passed=0
    failed=0
    for (test_value,expected_result) in is_prime_test_data.items():
        actual_result= is_prime(test_value)
        if actual_result==expected_result:
            passed+=1
        else:
            failed+=1
            print('failed for {}. expected {} found {}'.format(test_value,expected_result,actual_result))

        total+=1

    if total==passed:
        print('all test passed')            
    else:
        print('{} of {} test failed'.format(failed,total))


    prime_range_tests=[(2,10,4),(50,100,10),(0,100,26)]

    for (min,max,expected) in prime_range_tests:
        actual=len(prime_range(min,max))
        if actual!=expected:
            print('failed for prime_range({0}-{1}) expected ={2} found {3}'.format(min,max,expected,actual))



if __name__=='__main__':
    test()