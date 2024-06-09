class Car :
    def __init__( self, brand, color, horse_power ) :
        self.brand = brand
        self.color = color
        self.horse_power = horse_power
        self.is_tuned = False
    
    def __str__( self ) :
        return f"Marke: { self.brand } / Farbe: { self.color } / PS: { self.horse_power } / Getuned: { self.is_tuned }"
    
    def __repr__( self ) :
        return self.__str__()
    
    def __eq__( self, other ) :
        if not isinstance( other, Car ) :
            return False
        
        return self.brand == other.brand and \
            self.color == other.color and \
            self.horse_power == other.horse_power
    
    def paint_with( self, new_color ) :
        self.color = new_color
    
    def apply_tuning_kit( self ) :
        self.horse_power += 150
        self.is_tuned = True 


# or with line break for legibility
    # return f"Marke: { self.brand } / Farbe: { self.color } /" + \
        # f" PS: { self.horse_power }"

my_car = Car( 'VW', 'yellow', 75 )
other_car = my_car
other_car = None

my_car.brand
my_car.color
my_car.horse_power

my_car.brand = 'Audi'
my_car.color = 'blue'
my_car.horse_power = 220

my_car
print( my_car )

my_ferrari = Car( 'Ferrari', 'red', 550 )
my_ferrari.apply_tuning_kit()
my_ferrari

class StaticExample :
    static_info = 'Class wide info'
    
    @staticmethod
    def generate_info() :
        print( 'Static methods can be called without creating objects.' )
        return 'Special information'
    
    def object_method( self ) :
        print( 'Object methods must be called on objects.' )
        print( 'Static methods and variables are accessible.' )
        return StaticExample.static_info

StaticExample.generate_info()
StaticExample.static_info 

def check_correct_type( obj ) :
    if isinstance( obj, Car ) :
        print( 'is of type car' )
    else :
        print( 'not of type car' )

def do_something( obj ) :
    if isinstance( obj, str ) :
        print( 'Object is of type string.' )
    # ... weitere Pruefungen
    elif isinstance( obj, Car ) : 
        print( 'Object is of type Car.' )

toms_car = Car( 'Audi', 'blue', 275 )
jims_car = Car( 'Audi', 'blue', 275 )
toms_car == jims_car 
