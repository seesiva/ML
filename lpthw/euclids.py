"""
Compute the greatest common divisor of two nonnegative integers p and q as follows: If q is 0, the answer is p.
 If not, divide p by q and take the remainder r. The answer is the greatest common divisor of q and r.
"""

def gcd(p,q):
    if q==0:
        return p
    else:
        r=p % q
        return r

if __name__=="__main__":
    print gcd(13,2)