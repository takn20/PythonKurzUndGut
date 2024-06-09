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
