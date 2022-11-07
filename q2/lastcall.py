from bfs import *


lastCallResultDict = {}
def lastcall(func):
    """
    This wrapper function prevents duplicated calculations
    >>> f(4)
    16
    >>> f(4)
    I already told you the answer is 16
    16
    """
    def wrap(*args, **kwargs):
        # Generate a key
        allVarTuple = func.__code__.co_varnames
        finalVarList = list(args)
        for argumentName, argumentValue in kwargs.items():
            argumentIndex = allVarTuple.index(argumentName)
            finalVarList.insert(argumentIndex, argumentValue)
        key = tuple(finalVarList)

        # Check if this function with this key was already called 
        if lastCallResultDict.get(func) == None:
            lastCallResultDict[func] = {}
            res = func(*args, **kwargs)
            lastCallResultDict[func][key] = res
        elif lastCallResultDict[func].get(key) == None:
            res = func(*args, **kwargs)
            lastCallResultDict[func][key] = res
        else:
            res = lastCallResultDict[func][key]
            print("I already told you the answer is", res)  
            #return # This is commnented out to prevent 'None' type bugs
        return res
    return wrap



@lastcall
def f(x: int):
    return x**2

if __name__ == "__main__":
    import doctest
    doctest.testmod()
