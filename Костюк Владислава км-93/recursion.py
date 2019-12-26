def recursion(dataset):
    for provider_id in dataset.keys():
        zip_code = int(dataset[provider_id]['zip_code'])
        avarage_age = int(dataset[provider_id]['avarage_age'])

        if age > 30 and stroke >5:
            print('Zip_code:' + str(zip_code) + '\nProvider_id:' + str(provider_id) + '\nAvarage_age:' + str(avarage_age))
