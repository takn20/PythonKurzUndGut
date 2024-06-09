value = int( '7211' )
value = int( 'error' )

try :
    value = int( '7211' )
    print( 'Result after parsing:', value )
except ValueError :
    print( 'Cannot parse to integer.' )


try :
    value = int( 'error' )
    print( 'Result after parsing:', value )
except ValueError :
    print( 'Error, cannot parse to integer.' )

try :
    value = int( 'error' )
    print( 'Result after parsing:', value )
except IndexError :
    pass


names = [ 'Tim', 'Tom', 'Mike' ]
for i in range( 5 ) :
    try :
        value = int( names[ i ] )
    except ValueError :
        print( 'Error, cannot parse to integer.' )
    except IndexError :
        print( 'Error, wrong index.' )

try :
    print( 'Invalid index:', names[ 42 ] )
except :
    print( 'Unspecified error ocurred, seems to be wrong index.' )


try :
    print( 'Invalid index:', names[ 42 ] )
except :
    print( 'Unspecified error ocurred, seems to be wrong index.' )
finally :
    print( 'Always executed regardless of error or not.' )

## May 31, 2024

file = open( 'test.txt', encoding = 'utf-8' )
try :
    pass
finally :
    file.close()

# or more elegantly
with open( 'test.txt', encoding = 'utf-8' ) as file :
    # operations
    pass

# micromamba activate /opt/homebrew/Caskroom/miniforge/base 

#raise ValueError( 'Out of bounds.' )

def ensure_value_in_range( value, lower_bound, upper_bound ) :
    if value < lower_bound or value > upper_bound :
        raise ValueError( 'Value out of bounds.' )
    pass


ensure_value_in_range( 5, 2, 7 )
ensure_value_in_range( 42, 2, 7 )

def ensure_value_in_range( value, lower_bound, upper_bound ) :
    if value < lower_bound or value > upper_bound :
        raise ValueError( f"Value { value } out of bounds { lower_bound } - { upper_bound }." )
    else :
        pass


## June 4, 2024

class CustomerNotFoundException( Exception ) :
    def __init__( self, customer_id, customer_name ) :
        self.id = customer_id
        self.name = customer_name
    
    def __str__( self ) :
        return f"Customer { self.name } with id { self.id } not found."

#raise CustomerNotFoundException( 4711, 'Michael' )

class ValueOutOfBoundsError( ValueError ) :
    def __init__( self, value, lower_bound, upper_bound ) :
        self.value = value
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
    
    def __str__( self ) :
        return '{} not within range {} -- {}.'.format( self.value, self.lower_bound, self.upper_bound )

def ensure_value_in_range( value, lower_bound, upper_bound ) :
    if value < lower_bound or value > upper_bound :
        raise ValueOutOfBoundsError( value, lower_bound, upper_bound )
    pass

ensure_value_in_range( 5, 2, 7 ) # always test positive anpyd negative cases
ensure_value_in_range( 42, 2, 7 )

# Propagation of exceptions until handled or main and abort

import math

def reciprocal_squareroot( value ) :
    if value < 0 :
        raise ValueError( 'Value must not be negative but was ' + str( value ) + '.' )
    
    return 1 / math.sqrt( value )

print( reciprocal_squareroot( 4 ) )
print( reciprocal_squareroot( 16 ) )

print( reciprocal_squareroot( -4 ) )

#assert False, "Oh no, this assertion failed."

## June 7, 2024

message = 'EXPECTED VALUE'

# if assertion is true, nothing happens
assert message == 'EXPECTED VALUE'
assert message == 'ERROR'

# provide more information
message = 'UNEXPECTED'
assert message == 'info', 'Message should be "info" but was "' + message + '"'

# good practice, assert at the beginning of functions, methods; assure preconditions

def years_to_retirement( age ) : 
    assert age >= 0, "Only positive numbers are allowed."
    
    return 65 - age 


def years_to_retirement( age, working_years ) : 
    assert 18 <= age <= 65, "Age must be in range 18 -- 65."
    assert 10 < working_years < 50, "Working years must be in range 11 -- 49."

    return 65 - age 

# 9.3 Automatic Resource Management

file = open( 'test.txt', encoding = 'utf-8' )
try :
    line = read_first_line()
    # more
finally :
    file.close()

# more elegant

with open( 'test.txt', encoding = 'utf-8' ) as file :
    line = read_first_line()

# no try - finally - file.close necessary, handled in the background by context manager
