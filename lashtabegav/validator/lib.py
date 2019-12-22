import pycountry


def country_validator(country):
    countries = (i.name for i in list(pycountry.countries))
    if country not in countries:
        return False
    else:
        return True



def number_of_reviews_validator(number_of_reviews):
    if isinstance(number_of_reviews, int) and number_of_reviews >= 0:
        return True
    else:
        return False


def review_scores_value_validator(review_scores_value):
    if isinstance(review_scores_value, int) and 0 <= review_scores_value <= 100:
        return True
    else:
        return False

# host_id генерируется, его проверять не придется
