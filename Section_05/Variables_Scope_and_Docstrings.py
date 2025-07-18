def sum(a,b):
    # a and b are local variables
    c=a+b
    q=1
    #print(q)
    return c

def greet():
    print("Hello!")
    
q=2# global variable. It can access from outside the fuction >>>>>
print(q)
print(sum(5,4))
print(q)

def add(a,b):
    """
    Returns the sum of the two numbers
    
    
    

    Args:
        a (int): First number
        b (int): Second number
    
    returns:
    int:The sum of the two numbers ::
    
    
    """


    return a+b

print(add(4,6).__doc__)