'''
1. accept a range from user
2. find all primes in the range
3. find the sum and average of all primes
4. ask user if they want to try another round
'''

import consoleutils



def main():
    print(consoleutils)
    print(type(consoleutils))
    print(id(consoleutils))
    #print(help(consoleutils))
    
    print('dir={}'.format(dir(consoleutils)))

    name=consoleutils.read_str('your name ?')
    
    # names from module is not directly accessible
    #email=read_str('your email?')

    print('Hello {}, Welcome to Python!'.format(name))


main()


