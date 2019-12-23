#There are some examples on how to use correct input of data with validators:
provider_id=provider_id_validator(pattern_provider_id, "Enter provider ID : ")

city=city_validator(pattern_city, "Enter the city name : ")

total_lupa_episodes=total_lupa_episodes_validator(pattern_total_lupa_episodes, "Enter the number of total lupa episodes : ")

average_age=average_age_validator(pattern_average_age, 	"Enter the average age : ")

#Where  provider_id_validator, city_validator, total_lupa_episodes_validator, average_age_validator are validation functions that validate input data
#Also pattern_provider_id, pattern_city, pattern_total_lupa_episodes, pattern_average_age are patterns made using regular expressions for each type of data