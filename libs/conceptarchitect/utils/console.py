
import sys

# if you are running python 2, use raw_input instead of input
if sys.version_info.major<3:
    input=raw_input  


def read_str(prompt,defaultValue=None):
    answer=input(prompt)
    if answer==None and defaultValue!=None:
        return defaultValue
    else:
        return answer

def read_int(prompt,defaultValue=0):
    str=read_str(prompt)
    if str==None:
        return defaultValue
    else:
        return int(str)


def read_float(prompt,defaultValue=0.0):
    str=read_str(prompt)
    if str==None:
        return defaultValue
    else:
        return float(str)

def read_bool(prompt,defaultValue=True):
    str=read_str(prompt)
    if str==None:
        return defaultValue

    str=str.lower();    
    trues={'true','yes','t','y','ok'};
    falses={'false','no','f','n','cancle'};

    if str in trues:
        return True
    elif str in falses:
        return False
    else:
        return defaultValue

