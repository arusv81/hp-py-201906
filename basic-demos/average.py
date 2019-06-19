import sys

def average(* args):
    sum=0
    for value in args:
        sum+=value

    return sum/len(args)


def main(name, args):    
    values=[float(value) for value in args]
    result=average(*values)
    print(result)

if __name__=='__main__':
    main(sys.argv[0], sys.argv[1:])
