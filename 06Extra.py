# Python Basics, Chapter 6 Extra

name = input( 'Wie ist Ihr Name? ' )
age = input( 'Wie alt sind Sie? ' )

age_futur = int( age ) + 10
print( 'Herzlich Willkommen, ', name, '!' )
print( 'In zehn Jahren sind Sie', age_futur, 'Jahre alt.' )

number = int( input( 'Bitte geben Sie eine ganze Zahl ein: ' ) )
print( number )

number = float( input( 'Bitte geben Sie eine rationale Zahl ein: ' ) )
print( number )

from getpass import getpass
user = input( 'User: ' )
password = getpass( 'Password:' )

import random

random.random()
random.randint( 0, 99 )
random.randrange( 0, 100 )

random.choice( [ 'Wasser', 'Bier', 'Apfelschorle', 'Cola' ] )

sequence = [ 'AB', 'BC', 'CD', 'DE' ]
random.shuffle( sequence ) # shuffles in-place, i.e. directly on the sequence, similar to sort(), reverse()? This confuses me sometimes
print( sequence )

def parameter_example( first, second ) :
    print( 'First:', first )
    print( 'Second:', second )

def parameter_example( first, second, third ) :
    print( 'First:', first )
    print( 'Second:', second )
    print( 'Third:', third )

# you can do position-based
parameter_example( 1, 11, 111 )
# name-based, more explicit, let's do that always
parameter_example( second = 11, third = 111, first = 1 ) 
# or start with position-based and then name-based 
# but not name-based and then position based (SyntaxError psotional argument follows keyword argument)
parameter_example( 1, third = 111, second = 11 )
#parameter_example( second = 11, first = 1, 111 ) # this gives a syntax error, PyLance also underlines it

def parameter_example_default( x, y, optional_info = 'No extra information.' ) :
    print( '(%.2f, %.2f)' % ( x, y ) )
    print( 'Extra information:', optional_info )

def print_flexible( *values ) :
    print( *values, sep = '|' )

#def sum_variable_arguments( info = 'Sum', *args ) : # default value not useful here at the beginning; put variables w/ default values at the end of the list
def sum_variable_arguments( info, *args ) : # variable arguments also have to be at the end of the list
    result = 0
    for value in args :
        result += value
    print( info, str( result ) )

def value_minimum( first_value, *values ) :
    result = first_value
    for value in values :
        result = min( result, value )
    return result 

def process_key_value_arguments( **kwargs ) :
    for key, value in kwargs.items() :
        print( '{}: {}'.format( key, value ) )

## April 24, 2024

time = 20
if time < 18 :
    print( 'Good day' )
else :
    print( 'Good evening' )

greeting = 'Good day' if time < 18 else 'Good evening'
print( greeting )

age = 38
'old enough' if age >= 18 else 'too young'
# no print statement necessary
'Good day' if time < 18 else 'Good evening'

# lists
seasons = [ 'spring', 'summer', 'fall', 'winter' ]
sizes_tshirt = [ 'XS', 'S', 'M', 'L', 'XL', 'XXL' ]

print( seasons[ 0 ] )
print( 'I like', seasons[ 1 ] )

seasons[ 1 ] = 'Zurich'
print( 'I like', seasons[ 1 ] )

# tupel
seasons = ( 'spring', 'summer', 'fall', 'winter' )
sizes_tshirt = ( 'XS', 'S', 'M', 'L', 'XL', 'XXL' )

seasons[ 1 ] = 'Zurich'

# enum
from enum import Enum, auto

class Season( Enum ) :
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()
    WINTER = auto()

class Size( Enum ) :
    XS = auto()
    S = auto()
    M = auto()
    L = auto()
    XL = auto()
    XXL = auto()

for season in Season :
    print( season, season.value )

class Direction( Enum ) :
    N = ( 0, -1 )
    NE = ( 1, -1 )
    E = ( 1, 0 )
    SE = ( 1, 1 )
    S = ( 0, 1 )
    SW = ( -1, 1 )
    W = ( -1, 0 )
    NW = ( -1, -1 )

# How to use this? What to use this for?
# Reading the how to https://docs.python.org/3/howto/enum.html 

# match

http_code = 201

match http_code :
    case 200 :
        print( 'OK' )
    case 201 :
        print( 'CREATED' )
    case 404 :
        print( 'NOT FOUND' )
    case 418 :
        print( 'I AM A TEAPOT' )
    case _ :
        print( 'UNMATCHED CODE' )

def get_info( day ) :
    match day :
        case 'Monday' :
            return "I don't like ..."
        case 'Thursday' | 'Friday' :
            return 'Nearly there!'
        case 'Saturday' | 'Sunday' :
            return 'Weekend!'
        case _ :
            return 'In between ...'

get_info( 'Wednesday' )

values = ( 2, 3, 4 )
values = [ 2, 3, 4 ]

match values :
    case [ 1, 2, 3, 4 ] :
        print( 'Four in a row' )
    case [ 1, 2, 3 ] | [ 2, 3, 4 ] :
        print( 'Three in a row' )
    case [ 1, 2, 4 ] | [ 1, 3, 4 ] :
        print( 'Three not in a row' )
    case _ :
        print( 'Single or double' )

# see PEP 635, 636 Structural Pattern Matching why I can match a list or tuple to list or tuple
# https://peps.python.org/pep-0636/ 

class Gender( Enum ) :
    MALE = auto()
    FEMALE = auto()

def classify( person ) :
    match person :
        case ( name, age, 'male' | Gender.MALE ) :
            print( f"{ name } is a man and { age } years old." )
        case ( name, age, 'female' | Gender.FEMALE ) :
            print( f"{ name } is a woman and { age } years old." )
        case ( name, _, gender ) if gender is not None :
            print( f"{ name } is { gender }, no age specified." )
        case ( name, age, _ ) if age is not None :
            print( f"{ name } is { age } years old, no gender specified." )

classify( [ 'Micha', 50, 'male' ] )
classify( [ 'Lilli', 42, Gender.FEMALE ] )
classify( [ 'No gender', 42, None ] )
classify( [ 'No age', None, 'ALL' ] )

# break, continue, else in loops

for i in range( 10 ) :
    if i == 4 :
        break
    print( i )

for i in range( 10 ) :
    if i in [ 2, 4, 6, 8 ] :
        continue
    print( i )

# why not? It skips 0
for i in range( 1, 10 , 2 ) :
    print( i )

# April 26, 2024

i = 0
while i < 10 :
    print( i )
    i += 1
    if i == 4 :
        break

i = 0
while i < 10 :
    if i in [ 2, 4, 6, 8 ] :
        i += 1 # not optimal to have this line twice
        continue
    print( i )
    i += 1

i = 0
while i < 4 :
    print( i )
    i += 1

for i in range( 4 ) :
    print( i )

# inverting condition

i = 0
while i < 10 :
    if i != 2 and i != 4 and i != 6 and i != 8 :
        print( i )
    i += 1

i = 0
while i < 10 :
    if i not in [ 2, 4, 6, 8 ] :
        print( i )
    i += 1

# else in for loop

for i in range( 1, 7 ) :
    print( i )
else :
    print( 'Landed here because for loop was not exited with break.' )

for i in range( 1, 7 ) :
    print( i )
    if i == 4 :
        break
else :
    print( 'Landed here because for loop was not exited with break.' )

# else in while loop

i = 0
while i < 7 :
    i += 1
    print( i )
    if i == 8 :
        break
else :
    print( 'Landed here because while loop was not exited with break.' )

# eval()

eval( '2 + 5' )
eval( 'sum( [ 2, 3, 5, 8 ])' )
x = 14
y = 2
eval( 'x / y' )

eval( 'print( "Minimum:", min( x, y ) )' )
eval( 'x + y + z', { 'x' : 1, 'y' : 2, 'z' : 3 } )

# April 29, 2024
# recursive

def fac( n ) :
    if n == 0 or n == 1 :
        return 1
    else :
        print( 'Calling fac( ', str( n - 1 ),' )' )
        return n * fac( n - 1 )

fac( 5 )

# Fibonacci numbers with recursive solution, but a lot of function calls, and some calls are identical (e.g., fib(n - 3))
# Fast Fibonacci computation https://www.nayuki.io/page/fast-fibonacci-algorithms 
# Reading also about Karatsuba multiplication :-) so geeky https://en.wikipedia.org/wiki/Karatsuba_algorithm 

def flood_fill( values2dim, x, y ) :
    # x is column and y is row
    if x < 0 or y < 0 or x >= len( values2dim[ 0 ] ) or y >= len( values2dim ) :
        return
    if values2dim[ y ][ x ] == ' ' :
        values2dim[ y ][ x ] = '*' 
        flood_fill( values2dim, x, y - 1 )
        flood_fill( values2dim, x + 1, y ) 
        flood_fill( values2dim, x, y + 1 )
        flood_fill( values2dim, x - 1, y )

def print2dnice( lines ) :
    for line in lines :
        print( "".join( line ) )

second_world = [ list( '   #      # ' ),
                 list( '    #      #' ),
                 list( '#   #     # ' ), 
                 list( ' # #     #  ' ), 
                 list( '  #     #   ' ) ]

print2dnice( second_world )
print( '-------- Filling --------' )
flood_fill( second_world, 5, 0 )
print2dnice( second_world )
