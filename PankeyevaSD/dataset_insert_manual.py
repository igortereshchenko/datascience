from PankeyevaSD.dataset_structure import dataset

def insert_data(provider_id,zip_code,percent_of_beneficiaries_with_copd = None,percent_of_beneficiaries_with_hypertension = None, data = dataset):
     data[provider_id]= {
        "zip_code" : zip_code,
        "percent_of_beneficiaries_with_copd" : percent_of_beneficiaries_with_copd,
        "percent_of_beneficiaries_with_hypertension" : percent_of_beneficiaries_with_hypertension
        }

provider="123456"
zip_code="23456"
percent_of_beneficiaries_with_copd="87"
percent_of_beneficiaries_with_hypertension="34"
insert_data(provider, zip_code, percent_of_beneficiaries_with_copd, percent_of_beneficiaries_with_hypertension)
print(dataset)
