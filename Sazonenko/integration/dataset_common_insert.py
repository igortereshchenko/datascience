from Sazonenko.validator.lib import *
from maliarenkoma.validator.lib import *
from Sazonenko.integration.dataset_structure_common import *


def input_data(dataset):
    key = spc_common_validator(input('enter a name: '))
    data = {SPC_LATIN: spc_latin_validator(input(' input spc latin: ')),
                      STATUS: status_validator(input('input status: ')),
                      WIRE_HTAP:wire_htap_validator(input('input wire_htap: ')),
                      BOROCODE:borocode_validator(input('input borocode:')),
                      INF_OTHER:inf_other_validator(input('input inf_other:')),
                      CEN_YEAR:cen_year_validator(input('input cen_year:')),
                      ZIP_CITY:zip_city_validator(input('input zip_city:'))
    }
    dataset.update({key: data})

print(input_data(dataset))
