def add( value1, value2 ) :
    return value1 + value2

def multiply( value1, value2 ) :
    return value1 * value2

def is_adult( age ) :
    return age >= 18

def greet( name ) :
    print( "Hello", name )

def min_of_3( x, y, z ) :
    if x < y :
        if x < z :
            return x
        else :
            return z
    else :
        if y < z :
            return y
        else :
            return z

def min_of( x, y ) :
    if x < y :
        return x
    else :
        return y 

def min_of_3_better( x, y, z ) :
    return min_of( x, min_of( y, z ) )

def min_of_shorter( x, y ) :
    return x if x < y else y
