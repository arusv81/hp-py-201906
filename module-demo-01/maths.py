

def sum(*args):
    result=0
    for number in args:
        result+=number

    return result


def average(*args):
    return sum(*args)/len(args)

def min(x,y):
    return x if x>y else y


def main():
    print(f'sum(1,2,3,4)={sum(1,2,3,4)}');
    print(f'average(1,2,3,4)={average(1,2,3,4)}');

#main()