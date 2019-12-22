import usatovsv.validator.lib as v
# test
print(
v.cb_num_validator("123"),
v.cb_num_validator("4rt9fuf"),
v.spc_latin_validator("ULMUS SPECIES"),
v.spc_latin_validator("рослинна звичайна 4 5"),
v.wire_2nd_validator('333'),
v.wire_2nd_validator('True'),
v.zipcode_validator("324324")
)