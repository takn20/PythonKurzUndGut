cities = list()
names = []
print( type( cities ) )
print( type( names ) )

cities = [ "Kiel", "Bremen", "Zürich" ]
names.append( "Tim" )
names.append( "Tom" )
print( names )

names.insert( 0, "Anton" )
names.insert( 0, "Andreas" )
print( names )

names.insert( len( names ), "Last" )
names.append( "Last2" )
print( names )

print( "Tim?", "Tim" in names, "/", "Micha?", "Micha" in names )
print( names[ 2 ] )
print( names[ -1 ] )

# out of range IndexError
#print( names[ -77 ] )

print( "names:", names )
names[ 1 ] = "Mike"
print( "names[ 1 ] = 'Mike'", names )
del names[ 2 ]
print( "del names[ 2 ]", names )
del names[ 4 ]
print( "del names[ 4 ]", names )
names.remove( "Tom" )
print( 'names.remove( "Tom" ):', names )

# ValueError
#names.remove( "Tim" )

for i in range( len( names ) ) :
    #print( i, "-th name:", names[ i ] )
    print( f"{ i+1 }-th name: { names[ i ] }")

for name in names :
    print( name )

city_names = [ "Zürich", "Luzern", "Konstanz", "Bremen", "Kiel" ]
print( "Original:", city_names )
city_names.sort()
print( "Sorted:", city_names )

numbers_to_be_sorted = [ 1, 7, 2, 9, 11, 6, 3 ]
print( numbers_to_be_sorted )
numbers_to_be_sorted.sort()
print( numbers_to_be_sorted )
numbers_to_be_sorted.clear()
city_names.clear()
names.clear()

print( numbers_to_be_sorted )
print( city_names )
print( names )

names = [ "Tim", "Tom", "Mike" ]
names.append( [ "Maike", "Peter", "John" ] )
print( names, len( names ) )

names.remove( [ "Maike", "Peter", "John" ] )
names.extend([ "Maike", "Peter", "John" ] )
print( names, len( names ) )

names += [ "Michael" ]
names += [ "Sophie" ]
print( names, len( names ) )

names.remove( "Michael" )
names.remove( "Sophie" )
names += [ "Michael", "Sophie" ] 
print( names, len( names ) )

#############################################
## Sets
#############################################

names = set()
wrong_names = {}
type( names )
type( wrong_names )
other_names = set( [ "James", "Jim" ] ) # giving a list to a set creator

names.add( 'Tim' )
names.add( 'Tom' )
names.update( [ 'Mike', 'Peter', 'John' ] ) # vs. extend for lists
'Jens' in names
'Mike' in names
names.remove( 'John' ) # why not delete?
names -= { 'Peter', 'Mike' } # acts on names versus, no print out # why no += ?
names - { 'Peter', 'Mike' } # prints names without these names, does not act on variable names 

for name in names : # no index because sets don't have positions
    print( name )

names.clear()

# operations on sets

set_number1 = { 1, 2, 3, 4, 5, 6, 7, 8 }
set_number2 = { 2, 3, 5, 7, 9, 11, 13 }
print( 'Union: %s' % ( ( set_number1 | set_number2 ) ) )
print( 'Intersection: %s' % ( ( set_number1 & set_number2 ) ) )
print( 'Difference 1-2: %s' % ( ( set_number1 - set_number2 ) ) )
print( 'Symmetric difference: %s' % ( ( set_number1 ^ set_number2 ) ) )

#############################################
## Dictionaries, keys, values
#############################################

city_inhabitants_dict = dict()
bern_berlin_dict = { 'Bern' : 170_000, 'Berlin' : 3_500_000 }
bern_berlin_dict

city_inhabitants_dict[ 'Zurich' ] = 400_000
city_inhabitants_dict[ 'Hamburg' ] = 2_000_000
city_inhabitants_dict[ 'Kiel' ] = 250_000
city_inhabitants_dict.update( { 'Bern' : 170_000, 'Berlin' : 3_500_000 } )

'Zurich' in city_inhabitants_dict
'Bremen' in city_inhabitants_dict
400_000 in city_inhabitants_dict.values() # gives True or False but not key
1_234_567 in city_inhabitants_dict.values()

city_inhabitants_dict.get( 'Zurich' )
city_inhabitants_dict.get( 'Bremen' )
print( city_inhabitants_dict.get( 'Bremen' ) ) # need extra print to get 'none' as output
type( city_inhabitants_dict.get( 'Bremen' ) )

if not city_inhabitants_dict.get( 'Bremen' ) :
    print( 'City not in dictionary' )

city_inhabitants_dict[ 'Zurich' ]
city_inhabitants_dict[ 'Bremen' ] # returns KeyError :-) would be good for error handling

city_inhabitants_dict.get( 'Bremen', 999 ) # with get(): if key does not exist, return a default value

city_inhabitants_dict[ 'Bern' ] = 180_000
city_inhabitants_dict

del city_inhabitants_dict[ 'Bern' ] # just deletes
city_inhabitants_dict.pop( 'Kiel' ) # outputs the value and deletes the entry
city_inhabitants_dict

city_inhabitants_dict.items()
city_inhabitants_dict.keys()
city_inhabitants_dict.values()

for city in city_inhabitants_dict.keys() :
    print( city )

for inhabitants in city_inhabitants_dict.values() :
    print( inhabitants )

for entry in city_inhabitants_dict.items() :
    print( entry )

city_inhabitants_dict.clear()

#############################################
## Next Steps: Comprehensions
#############################################

[ value for value in range( 10 ) ] # creates a list but not assigned to a variable
[ value * value for value in range( 10 ) ]
[ n for n in range( 10 ) if n % 2 == 0 ]

tuples = [ ( i, j ) for i in range( 3 ) for j in range( 5 ) ]
tuples

tuples = [ ( i, j, k ) for i in range( 3 ) for j in range( 3 ) for k in range( 3 ) ]
tuples

{ i for i in range( 10 ) if i % 2 == 1 }
# { for i in range( 10 ) if i % 2 == 1 } # returns invalid syntax without the 'i' in the beginning
{ n : n ** 2 for n in range( 10 ) if n % 2 == 0 }
{ n : n ** 2 for n in range( 0, 10, 2 ) } # without condition

## Slicing!

numbers = [ value for value in range( 13 ) ]
print( numbers[ 0 : 3 ] )
print( numbers[ 2 : 8 ] )
print( numbers[ -3 : ] )
print( numbers[ : : 2 ] )
print( numbers[ 2 : 10 : 2 ] )
print( numbers[ 10 : 2 : -2 ] )

names = [ 'Anne', 'Babs', 'Jane', 'Jennifer', 'Lilli', 'Sophie', 'Svenja' ]
print( names[ 4 : 6 ] )
print( names[ -3 : -1 ] )

numbers = [ 2, 3, 9, 10, 11, 12 ]
numbers[ : 0 ] = [ 0, 1 ] # insert at the beginning, I would prefer insert
numbers.insert( 0, [ 0, 1 ] ) # CAUTION, adding one list at the position, better to do it twice
numbers.insert( 0, 1 )
numbers.insert( 0, 0 )
#numbers.remove( item ) # caution, provide the value not the index
del numbers[ : 2 ]
numbers[ len( numbers ) : ] = [ 13, 14 ]
numbers
numbers[ 4 : 4 ] = [ 4, 5, 6, 7, 8 ] # if not start or end position, then need to provide the index twice
numbers[ 4 : ] = [ 4, 5, 6, 7, 8 ] # would replace from index 4
numbers[ : 4 ] = [ 4, 5, 6, 7, 8 ] # would replace until index 4
numbers[ 4 : 8 ] = [ 44, 55, 66, 77, 88 ]
numbers[ 4 : 10 ] = [] 

## Sortierung mit sort(), sorted()

city_names = [ 'Zurich', 'Luzern', 'Konstanz', 'Bremen', 'Kiel' ]
city_names.sort()
city_names.sort( reverse = True )
city_names.sort( key = len, reverse = True )

def last_character( input ) :
    return input[ -1 ]

city_names.sort( key = last_character, reverse = True )

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

# took me some time to understand this; not easy but useful 
# there's also __eq__, __gt__, __le__, __ge__ (what is the lazyness about?)

def get_age( person ) :
    return person.age

persons.sort( key = get_age )

def get_name_age( person ) :
    return person.name, person.age

def get_age_name( person ) :
    return person.age, person.name

# Python magically can compare these
#[ 'Fred', 14 ] < [ 'Jim', 7 ]
#True

sorted_by_name_age = sorted( persons, key = get_name_age )
sorted_by_age_name = sorted( persons, key = get_age_name )
sorted_by_age_name

# Swap entries

def swap( values, first, second ) :
    value1 = values[ first ]
    value2 = values[ second ]
    values[ first ] = value2 
    values[ second ] = value1 

def swap_via_tuple( values, first, second ) :
    values[ first ], values[ second ] = values[ second ], values[ first ]

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
swap( numbers, 3, 5 )
swap( numbers, 2, 6 )
print( numbers )

swap_via_tuple( numbers, 1, 7 )
swap_via_tuple( numbers, 0, 8 )
print( numbers )

def reverse( values, start, end = -1 ) :
    if end == -1 :
        end = len( values ) - 1
    while start < end :
        swap( values, start, end )
        start += 1
        end -= 1

# reverse, reversed

numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
numbers.reverse()
print( numbers )

print( list( reversed( numbers ) ) )

elements = [ '1st', '2nd', '3rd', '4th', 'LAST' ]
elements.reverse()
print( elements )

# Revere does not exist for type set, they have no order
# also useful for lists: pop()

# Multidimensional lists

list_two_dimensional = [
    [ 1, 1, 1, 1 ],
    [ 2, 2, 2, 2 ],
    [ 3, 3, 3, 3 ],
    [ 4, 4, 4, 4 ]
]

def print_two_dimensional( values ) :
    for line in values :
        print( line )

print_two_dimensional( list_two_dimensional )

# From docs.python.org/3.10/tutorial/datastructures.html

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[ [ row[ i ] for row in matrix ] for i in range( 4 ) ]
# It took me ten minutes to understand this magic :-)

world = [
    list( '################' ),
    list( '##  P         ##' ),
    list( '####   $ X  ####' ),
    list( '###### $  ######' ),
    list( '################' )
]

def print_two_dimensional_world( values ) :
    for line in values :
        print( ''.join( line ) )

triangle = [
    [ 1 ],
    [ 2, 2 ],
    [ 3, 3, 3 ]
]

print_two_dimensional( triangle )

list_persons = [
    [ 'Klaus', 'Bärbel' ],
    [ 'Knut' ],
    [ 'Inge', 'Ute', 'Petra' ],
    [ 'Mike', 'Harald', 'Sophie', 'Pia' ]
]

print_two_dimensional_world( list_persons )
