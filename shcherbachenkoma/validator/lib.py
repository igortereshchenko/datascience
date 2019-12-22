import re
re_provider_id = re.compile("^[+]?\d{6}?")
re_agency_name = re.compile("^(([a-wA-W]+)\s{0,1})+")
re_average_hcc_scor = re.compile("^([-+]?\d+\.?\d*\s*)+$")
re_percent_of_beneficiaries_with_asthma = re.compile("^\d+$")
def provider_id_validator(value):
    if not re_provider_id.match(value) or len(value) > 6:
        return False
    return value


def agency_name_validator(value):
    if not re_agency_name.match(value):
        return False
    return value

def average_hcc_score_validator(value):
    if not re_average_hcc_scor.match(value):
        return False
    return value


def percent_of_beneficiaries_with_asthma_validator(value):
    if not re_percent_of_beneficiaries_with_asthma.match(value) or int(value) > 100:
        return False
    return value
