from lib import *

print( 'host_id: 151245, ', host_id_validator( '151245' ) )
print( 'host_id: 151a245, ', host_id_validator( '151a245' ) )

print( 'price: $12.23, ', price_validator( '$12.23' ) )
print( 'price: 12.23, ', price_validator( '12.23' ) )

print( 'minimum_nights: 7, ', minimum_nights_validator( '7' ) )
print( 'minimum_nights: 7.0, ', minimum_nights_validator( '7.0' ) )

print( 'weekly_price: $15, ', weekly_price_validator( '$15' ) )
print( 'weekly_price: 15, ', weekly_price_validator( '15' ) )