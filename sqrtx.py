class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x<=3:
            return 1
        if x==5:
            return 2
        else:
            i=0
            while i< ((x//2) +1):

                if i*i>x:
                    return i-1
                elif i*i==x:
                    return i
                i+=1
