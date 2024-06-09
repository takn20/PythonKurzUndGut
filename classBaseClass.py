class BaseClass :
    def method( self ) :
        print( "called method" )
    
    def other_method( self ) : 
        pass

class SubClass( BaseClass ) :
    def method( self ) :
        super().method()
        print( "more actions" )
    
    # other_method will be used as is
    def additional_method( self ) :
        pass

obj= SubClass()
obj.method()