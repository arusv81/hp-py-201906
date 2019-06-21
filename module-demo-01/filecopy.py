import sys

def copy(src,trgt):
        with open(src,'rb') as s:
            with open(trgt,'wb') as t:
                while True:
                    buff=s.read(1024) # read upto 1024 bytes
                    if(len(buff)==0): # nothing to read
                        break;
                    t.write(buff)
                    print('.',end=' ')

def main(name,args):
    if(len(args)<2):
        print('insufficeint argument: {} <src> <target>'.format(name))
    else:
        copy(args[0],args[1])
    

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])