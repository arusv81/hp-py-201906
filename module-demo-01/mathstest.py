from maths import sum,average

def test():
    print('executing main from maths module: {}'\
        .format(__name__))
    print('sum(1,2,3,4)={}'.format(sum(1,2,3,4)));
    print('average(1,2,3,4)={}'.format(average(1,2,3,4)));

if __name__=='__main__':
    test()
else:
    print('I am not an importable module {}'.format(__name__))