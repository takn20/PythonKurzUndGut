name1 = [ 'Micha', 'Tim', 'Tom', 'Willi' ]
name2 = [ 'Marcello', 'Karthi', 'Michael' ]
names = name1 + name2

print( 'All names:', names )
print( 'Last name:', names[ -1 ] )
print( 'Reversed list:', names[ : : -1 ] )
print( 'Every second name:', names[ : : 2 ] )
print( 'len: %d, min: %s, max: %s' % ( len( names ), min( names ), max( names ) ) )
# Ahaha, min and max is alphabetical ordering not length of name

some_numbers = [ 1, 2, 3 ]
list_iter = iter( some_numbers )
next( list_iter )
next( list_iter )
next( list_iter )
next( list_iter )

for number in some_numbers :
    print( number )

class FactorialIterator :
    def __init__( self, n = 0 ) :
        self.n = n
        self.result = 1
        self.iteration = 1
    
    def __iter__( self ) :
        return self
    
    def __next__( self ) :
        if self.iteration > self. n :
            raise StopIteration
        
        self.result *= self.iteration
        self.iteration += 1
        return self.result

factorial = FactorialIterator( 5 )

iterator = iter( factorial )
print( next( iterator ) )

for n in factorial :
    print( n )

def my_first_generator() :
    yield 'one'
    yield 'two'
    yield 'three'

generator = my_first_generator()
print( next( generator ) )
print( next( generator ) )
print( next( generator ) )

def my_second_generator() :
    n = 1
    print( 'before first' )
    yield n
    
    n *= 2
    print( 'before second' )
    yield n
    
    n *= 3
    print( 'before third' )
    yield n

for item in my_second_generator() :
    print( item )

## May 1, 2024
# factorial with a generator function, takes care of __iter__ and __next__ automatically

def factorial_generator( n = 0 ) :
    iteration = 1
    result = 1
    while iteration <= n :
        print( 'i =', iteration, ', result = ', result )
        yield result

        iteration += 1
        result *= iteration

generator = factorial_generator( 5 )
print( next( generator ) )

# Cool, but I will need time to think of this and use it

# 7.4 Named tuples

from collections import namedtuple
from math import sqrt

def line_length( point1, point2 ) :
    return sqrt( ( point1.x - point2.x ) ** 2 + ( point1.y - point2.y ) ** 2 )

Point = namedtuple( 'Point', [ 'x', 'y' ] )
point1 = Point( 1.0, 5.0 )
point2 = Point( 2.5, 1.5 )
line_length( point1, point2 )

# backwards compatible with tuple access, e.g., unpacking
x1, y1 = point1 

Person = namedtuple( 'Person', [ 'name', 'age', 'gender' ] )

from enum import Enum

dxdy = namedtuple( 'dxdy', [ 'dx', 'dy' ] )
class Direction( Enum ) :
    N = dxdy( 0, -1 )
    NE = dxdy( 1, -1 )
    E = dxdy( 1, 0 )
    SE = dxdy( 1, 1 )
    S = dxdy( 0, 1 )
    SW = dxdy( -1, 1 )
    W = dxdy( -1, 0 )
    NW = dxdy( -1, -1 )

print( Direction.NE.value )
northeast = Direction.NE 
print( northeast.value.dx )
print( northeast.value.dy )

try :
    Person = namedtuple( 'Person', [ 'name', 'class', 'age', 'gender' ] )
except ValueError as err :
    print( err )

try :
    Person = namedtuple( 'Person', [ 'name', 'age', 'gender', 'age' ] )
except ValueError as err :
    print( err )

# 7.5 Lambdas

add_one = lambda x : x + 1
double_it = lambda x : x * 2
multiply_them = lambda x, y : x * y
power_of = lambda x, y : x ** y

print( double_it( 7 ) )
print( power_of( 2, 8 ) )

# one line implementation versus 
# def add_one( x ) :
#   return x + 1

numbers = [ 1, 5, 4, 6, 8, 11, 3, 12 ]
is_even = lambda x : ( x % 2 == 0 )
numbers_even = list( filter( is_even, numbers ) )
print( numbers_even )

numbers = [ 1, 6, 8, 10, 14, 2, 11, 7, 0, 3, 2, 1 ]
numbers_filtered = list( filter( lambda x : ( x > 5 ), numbers ) )
print( numbers_filtered )

names = [ 'tim', 'tom', 'mike', 'KARL' ]
list( filter( lambda name : ( 'm' in name ), names ) )
list( filter( lambda name : ( 'm' in name or name.startswith( 'K' ) ), names ) )

# compare with list comprehensions, I would prefer them for readability
[ name for name in names if 'm' in name ]
[ name for name in names if 'm' in name or name.startswith( 'K' ) ]

list( map( lambda str : str.upper(), names ) )

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
list( map( lambda x : x * 2, numbers ) )
list( map( lambda x : x ** 2, numbers ) )

list( map( lambda str : str.capitalize(), [ 'tim', 'tom', 'jim' ] ) )
[ str.capitalize() for str in [ 'tim', 'tom', 'jim' ] ] 

numbers = [ 11, 2, 30, 333, 14, 4444, 100, 2222 ]
numbers.sort()
print( numbers )

numbers = [ 11, 2, 30, 333, 14, 4444, 100, 2222 ]
numbers.sort( key = lambda x : len( str( x ) ) )
print( numbers )

numbers = [ 11, 2, 30, 333, 14, 4444, 100, 2222 ]
numbers.sort( key = lambda x : str( x )[ -1 ] ) # sort by last digit
print( numbers )

ids = [ 'id1', 'id2', 'id30', 'id3', 'id12', 'id22', 'id100' ]
print( sorted( ids ) )
print( sorted( ids, key = lambda x : int( x[ 2 : ] ) ) )

## May 6, 2024
# from Chapt. 5
class SimplePerson :
    def __init__( self, name, age ) :
        self.name = name
        self.age = age 
    
    def __repr__( self ) :
        return f"{ self.name } { self.age }"
    
    def __lt__( self, other ) :
        return self.name < other.name or ( self.name == other.name and self.age < other.age )

persons = [
    SimplePerson( 'Mike', 50 ),
    SimplePerson( 'Jim', 7 ),
    SimplePerson( 'Tim', 50 ),
    SimplePerson( 'John', 14 ),
    SimplePerson( 'Peter', 50 ),
    SimplePerson( 'Fred', 14 ),
    SimplePerson( 'Peter', 40 ),
    SimplePerson( 'Peter', 55 ),
]

# here sorting w/ lambda and not function
persons.sort( key = lambda person : [ person.name, person.age ] )
persons

persons.sort( key = lambda person : [ person.age, person.name ] )
persons 
