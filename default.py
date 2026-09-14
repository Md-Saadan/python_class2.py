# default args
def default_args(a,b,c=600):
    print("a:",a)
    print("b:",b)
    print("c:",c)

# default_args(100,200)
default_args(200,500,700)

# Mix Arbitatary args
def Mix_args1(a,b,*c):
    print("a:",a)
    print("b:",b)
    print("c*:",c)

# default_args(100,200)
Mix_args1(200,500,"MOUSE","KEYBOARD","CPU","MONITOR")

# Mix Arbitatary Keywoard args
def Mix_args2(a,b,**c):
    print("a:",a)
    print("b:",b)
    print("**c:",c)

Mix_args2(200,500,MOUSE=200,KEYBOARD=500,CPU=600,MONITOR=7000)

# Mix Arbitatary Keywoard args
def Mix_args3(a,*b,**c):
    print("a:",a)
    print("*b:",b)
    print("**c:",c)

Mix_args3(200,"Ali","Maaz","MD","AH","Adeem",MOUSE=200,KEYBOARD=500,CPU=600,MONITOR=7000)
