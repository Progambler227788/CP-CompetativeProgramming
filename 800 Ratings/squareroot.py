
def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        if x <=1:
            return x
        i = 1
        square = 1
        while x>=square:
              i+=1
              square = i * i
              print(i)
        return i
mySqrt(25)
    

        