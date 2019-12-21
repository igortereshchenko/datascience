from lib import *

print( 'host_id: 956883, ', host_id_validator( '956883' ) )
print( 'host_id: 956 883, ', host_id_validator( '956 883' ) )
print( 'host_id: 956883g, ', host_id_validator( '956883g' ) )

print( 'bedrooms: 4, ', bedrooms_validator( '4' ) )
print( 'bedrooms: -9, ', bedrooms_validator( '-9' ) )
print( 'bedrooms: g, ', bedrooms_validator( 'g' ) )

print( 'room_type: Private room, ', room_type_validator( 'Private room' ) )
print( 'room_type: -9, ', room_type_validator( '-9' ) )
print( 'room_type: 536346 room, ', room_type_validator( '536346 room' ) )
print( 'room_type: Entire apt/home, ', room_type_validator( 'Entire apt/home' ) )

print( 'country: United States, ', country_validator( 'United States' ) )
print( 'country: -9, ', country_validator( '-9' ) )
print( 'country: united states, ', country_validator( 'united states' ) )
