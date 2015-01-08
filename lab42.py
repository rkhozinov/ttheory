__author__ = 'rkhozinov'

tcz = 2.5
t0 = 1
tc = 1.5
tco = 3
tpb = 7
n = 6  # digit number
Cki = 1.14
Tki = 110
Cnx = 4.0
Tnx = 85
Praz = 0.5

aki = 1.21
anx = 1.25


def main(n1, n2):
    # n1 - individual hardware per objectyki
    # n2 - objects
    pki = sum((tco, tc * n, tcz, tpb, Tki))
    cpnx = sum((tco, tc * n, tcz, tpb, Tnx))
    yki = (aki * n1 * Praz * pki) / 3600
    ynx = (anx * n2 * Praz * cpnx) / 3600

    print "n1: {} n2: {}", format(n1, n2)
    print "Pki: {} sec".format(pki)
    print "Cpnx: {} sec".format(cpnx)
    print "Yki: {} Erl".format(yki)
    print"Ynx: {} Erl".format(ynx)
    print "Y: {} Erl".format(yki + ynx)


if __name__ == "__main__":
    main(n1=870, n2=120)
