from classCar import Car

class CarManagementApplication :
    def __init__(self) :
        self.available_cars = [ 
            Car( 'Renault', 'blue', 75 ),
            Car( 'Renault', 'petrol', 175 ), 
            Car( 'Ferrari', 'red', 455 ), 
            Car( 'BMW', 'green', 255 ),
            Car( 'BMW', 'yellow', 125 ),
            Car( 'VW', 'white', 65 ),
            Car( 'VW', 'blue', 105) ]
    
    def filter_by_brand( self, brand ) :
        for current_car in self.available_cars :
            if current_car.brand == brand :
                print( current_car )
    
    def filter_by_minimum_horse_power( self, minimum_horse_power ) :
        for i in range( len( self.available_cars ) ) :
            if self.available_cars[ i ].horse_power > minimum_horse_power :
                print( self.available_cars[ i ] )
        
def main() :
    app = CarManagementApplication()
    #print( 'App started.' )

    print( 'Renaults on offer:' )
    app.filter_by_brand( 'Renault' )

    print()

    print( 'Cars with more than 150 bhp:' )
    app.filter_by_minimum_horse_power( 150 )
    
if __name__ == "__main__" :
    main()