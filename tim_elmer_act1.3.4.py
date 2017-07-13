# this program will take an input value and determine if it 
# is an integer, odd, even, or a multiple of 6.
def f(x):
    if int(x) == x:
       if x % 2 == 0:
            if x % 3 ==0:
                print x, 'is a multiple of 6'
            else:
                print x, ' is an even number'
       else:
            print x, ' is an odd number' 
    else:
        print x, ' is not an intager'
     
        
    