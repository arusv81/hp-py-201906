

def sum(*args):
    result=0
    for number in args:
        result+=number

    return result


def average(*args):
    return sum(*args)/len(args)

def min(x,y):
    return x if x<y else y

# if __name__=='__main__':
#     print('executing main from maths module: {}'\
#         .format(__name__))
#     print('sum(1,2,3,4)={}'.format(sum(1,2,3,4)));
#     print('average(1,2,3,4)={}'.format(average(1,2,3,4)));


