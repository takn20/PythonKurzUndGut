class ValueOutOfBoundsError( ValueError ) :
    def __init__( self, value, lower_bound, upper_bound ) :
        self.value = value
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
    
    def __str__( self ) :
        return '{} not within range {} -- {}.'.format( self.value, self.lower_bound, self.upper_bound )


def func1( value ) :
    func2( value )

def func2( value ) :
    try :
        func3( value )
    except ValueOutOfBoundsError as value_error :
        print( value_error )

def func3( value ) :
    if not value :
        raise ValueError
    raise ValueOutOfBoundsError( value, 1, 100 )


def main() :
    func1( 123 )
    func1( None )


if __name__ == "__main__" :
    main()


