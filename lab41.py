# -*- coding: utf-8 -*-
__author__ = 'rkhozinov'

# structure of abonents
nhx = 4000
nki = 4000
nkk = 1000
nt = 300
ncl = 100

# average of calls
Tnx = 100
Tki = 130
Tkk = 120
Tt = 100
Tcl = 100

tco = 3  # listening time
tc = 1 # connection time
tn = 1.5 # entering number time
tpb = 2.5
t0 = 0
magic=6

# calls results
pp = 0.6
pzn = 0.2
pno = 0.1
posh = 0.05
ptex = 0.05

def main():
    tpnx = sum((tco, tc*magic, tpb, Tnx, t0))
    tzn=sum(tco, tc, tcz)
    print tpnx


if __name__ == '__main__':
    main()



