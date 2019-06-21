import sys

def main(name,args):
    file=open(args[0])
    data=file.read() # reads entire file in one go
    print(data)
    file.close() # good idea to close the file

if __name__=='__main__':
    main(sys.argv[0],sys.argv[1:])