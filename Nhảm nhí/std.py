def std(x,mode=0):
    tb=0
    for i in x:
        tb=tb+i
    tb=tb/len(x)
    if mode==1:
        return tb
    else:
        std=[]
        for i in x:
            std.append(abs(tb-i))
        return(std)
