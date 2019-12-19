from PankeyevaSD.dataset_structure import dataset

def insert_data(provider_id,zip_code,percent_of_beneficiaries_with_copd = None,percent_of_beneficiaries_with_hypertension = None, data = dataset):
     data[provider_id]= {
        "zip_code" : zip_code,
        "percent_of_beneficiaries_with_copd" : percent_of_beneficiaries_with_copd,
        "percent_of_beneficiaries_with_hypertension" : percent_of_beneficiaries_with_hypertension
        }


insert_data( 123456,12345, 77, 36 )
print(dataset)