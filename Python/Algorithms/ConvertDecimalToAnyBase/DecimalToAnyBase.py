def d2b(num,base):
    basenum = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            basenum += str(dig)
        else:
            basenum += chr(ord('A')+dig-10)
        num //= base
    basenum = basenum[::-1]
    return basenum


print(d2b(125,7))