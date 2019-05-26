import sys
from fileio import *
from ed import *

mode=sys.argv[1]
kp=sys.argv[2]
mp=sys.argv[3]

if (mode == 'e')or(mode=='E'):
    msg=input("Message to encrypt: ")
    encr(msg,kp,mp)

elif (mode == 'd')or(mode=='D'):
    try:
        msg2=decr(kp,mp)
        print(msg2)
    except:
        print("Something went wrong ...")
else:
    print("Wrong argument\n[e/d] [path to key file] [path to message]")
