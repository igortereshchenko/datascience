from re import match

def size_validator(size):
    """
    if validation is correct return size
    :param size_of_product: float , size
    :return: float, size
    """
    if match('^\d+\.{0,1}\d*$', size):
        return True
    return False


def weight_validator(weight):
    """
    if validation is correct return weight
    :param weight_of_product: float, weight
    :return: float, weight
    """
    if match('^\d+\.{0,1}\d*$', weight):
        return True
    return False


def features_validator(features):
    """
    if validation is correct return features
    :param features_of_product: str , features
    :return:str, features
    """
    if match('^\[({"key":"(([A-Z][a-z]*)\s{0,1})*","value":\["(([A-Z][a-z]*)\s{0,1})*"\]\},{0,1})*\]$', features):
        return True
    return False