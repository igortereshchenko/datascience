import NoskovIlyas.validator.lib as lib

assert lib.key_valid('Bronx') is True
assert lib.key_valid('12') is False
assert lib.key_valid('bronx') is False
assert lib.key_valid('Bronx dsada') is False

assert lib.spc_valid('321321312') is False
assert lib.spc_valid('Honeylocust Elm Planetree') is True
assert lib.spc_valid('Hone23121') is False

assert lib.horzgr_valid('yes') is True
assert lib.horzgr_valid('no') is True
assert lib.horzgr_valid('3213') is False
assert lib.horzgr_valid('Bronx') is True

assert lib.year_valid('2001') is True
assert lib.year_valid('no') is False
assert lib.year_valid('Bronx') is False
assert lib.year_valid('21') is False
