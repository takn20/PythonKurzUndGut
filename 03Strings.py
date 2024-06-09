def modify_every_third_character_upper( values ) :
    for i in range( 0, len( values ), 3 ) :
        # print( values[ i ].upper() )
        values[ i ] = values[ i ].upper()
    # print( values )

alphabet = 'abcdefghijklmnopqrstuvwxyz'
list_alphabet = list( alphabet )
modify_every_third_character_upper( list_alphabet )
print( list_alphabet )