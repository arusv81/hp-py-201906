def count_primes(min,max):
    primes=[];
    number=min
    while number<max:
        divisor=2
        while divisor<number:
            if number%divisor==0:
                break
            divisor+=1
                
        if divisor==number:
            primes.append(number)
        number+=1
            
    print(len(primes))

count_primes(2,10)
count_primes(50,100)