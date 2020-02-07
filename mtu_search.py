# binary MTU search

def bin(mtu):
    high = 64   # set max here
    low = 0     # set min here
    mid = 0

    while(low <= high):
        mid = (low+high)//2
        if mid > mtu:   # set MTU here
            high = mid -1
        else:
            low = mid +1
    return high

mtu2 = int(input("input:"))
print(bin(mtu2))
