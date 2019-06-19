

def sum(*args):
    result=0
    for number in args:
        result+=number

    return result


def average(*args):
    return sum(*args)/len(args)

def min(x,y):
    return x if x<y else y

