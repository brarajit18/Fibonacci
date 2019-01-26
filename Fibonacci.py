# -*- coding: utf-8 -*-
import array

class Fibonacci():
    """This class creates the fibonacci series
    upto the certain input limit (i.e. numCount),
    which controls the length of output array.
    Syntax Example:
        fibo = Fibonacci()
        x = 20; #value 20 to get first 20 numbers of fibonacci series
        print (fibo.Fibonacci(x))
    """    
    def Fibonacci(self, numCount):
        fibo = array.array('I')
        for i in range(0,numCount):
            if i == 0 or i == 1:
                fibo.append(i)
            else:
                fibo.append(fibo[i-2] + fibo[i-1])
        return fibo

if __name__ == '__main__':
    fibo = Fibonacci()
    x = 20; #value 20 to get first 20 numbers of fibonacci series
    print (fibo.Fibonacci(x))