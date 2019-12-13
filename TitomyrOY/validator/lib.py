from re import match


def name_validator(name):
    """
    if validation is correct return name
    :param name_of_product: str , name
    :return:str, name
    """
    if match("^([a-zA-Z()']\s{0,1})*$", name):
        return True
    return False


def size_validator(size):
    """
    if validation is correct return size
    :param name_of_product: float , size
    :return: float, size
    """
    if match('^\d+\.{0,1}\d*$', size):
        return True
    return False


def weight_validator(weight):
    """
    if validation is correct return weight
    :param name_of_product: float, weight
    :return: float, weight
    """
    if match('^\d+\.{0,1}\d*$', weight):
        return True
    return False


def features_validator(features):
    """
    if validation is correct return features
    :param name_of_product: str , features
    :return:str, features
    """
    if match('^(\[{"key":"([A-Z][a-z])*","value":"([A-Z][a-z])*"]}],{0,1})*$', features):
        return True
    return False
