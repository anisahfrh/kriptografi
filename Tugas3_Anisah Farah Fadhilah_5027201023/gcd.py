def _gcd(x, y):  
    if(y == 0):
        return x
    else:  
        return _gcd(y, x % y)   
num = _gcd(66528, 52920)
print(num)