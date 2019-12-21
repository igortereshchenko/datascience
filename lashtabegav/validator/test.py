import lib as validate


country = input('Введите название страны на англ.\n')

print("Верно." if validate.country_validator(country) else "Не верно.")


number_of_reviews = input('Введите кол-во отзывов\n')

print("Верно." if validate.number_of_reviews_validator(int(number_of_reviews)) else "Не верно.")


review_scores_value = input('Введите значение отзыва\n')

print("Верно." if validate.review_scores_value_validator(int(review_scores_value)) else "Не верно.")

