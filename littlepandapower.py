def mde(a,b,n):
    r = 1
    for bit in reversed(getbinary(b)):
        r = r*r % n
        if bit == 1:
            r = r * a % n
    return r

def getbinary(num):
    binary_arr = []
    while num:
        binary_arr.append(num%2)
        num >>= 1
    return binary_arr

def mmi(a,power,m):
    m0 = m
    x0 = 0
    x1 = 1
    if m == 0:
        return 0
    while a > 1:
        # quotient
        q = a/m
        t = m
        # euclids theorem
        m= a%m
        a = t
        # back subs
        t = x0
        x0 = x1-(q*x0)
        x1 = t
    if x1 < 0:
        x1 += m0
    return mde(x1,abs(power),m0)
    
        
def main():
    tc = input()
    while tc > 0:
        base, power, mod = map(int, raw_input().strip().split(' '))
        if power >= 0:
            print mde(base, power, mod)
        else:
            print mmi(base, power, mod)
        tc -= 1

if __name__ == "__main__":
    main()