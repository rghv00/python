#!/usr/bin/env python3

def bsr(l, k, s, e):
    if len(l) == 0:
        return False
    
    mid = len(l)//2

    print(mid, s, e)

    if l[mid] == k:
        print('Key {} is at index {}'.format(k, (s+e)//2))
        return True
    
    if k < l[mid]:
        return bsr(l[:mid], k, s, e-mid)
    else:
        return bsr(l[mid+1:], k, s+mid+1, e)

a = range(1, 16)
x = bsr(a, 4, 0, len(a)-1)
print(x)
