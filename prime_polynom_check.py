
def checkPrimitive(tPoly):
    saveInput = tPoly
    k = degree(tPoly)
    # find first divisor
    divisor = (1 << (k-1)) -1

    # divide through all polynoms < testPolynom
    while(divisor > 0b10):
        g = degree(divisor)
        tPoly = saveInput
        # XOR
        while(k >= g):
            divisor = divisor << (k-g)
            tPoly = tPoly ^ divisor
            divisor = divisor >> (k-g)
            k = degree(tPoly)
            if not(tPoly):
                print(bin(saveInput), 'is not primitive.')
                return False
        # try next divisor
        divisor -= 1
    print(bin(saveInput), " is primitive.")

# check poly degree
def degree(Poly):
    k=0
    while(Poly):
        Poly = Poly >> 1
        k += 1
    return k

# output
print("Input polynom: ")
test = input()
checkPrimitive(test) 