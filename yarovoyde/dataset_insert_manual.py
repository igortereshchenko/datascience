from yarovoyde.dataset_structure import dataset

def data_insert(provider_id, city, percent_of_beneficiaries_with_cancer, percent_of_beneficiaries_with_diabetes):
    dataset.update(
        {
            provider_id:
                {
                    'city':city,
                    'percent_of_beneficiaries_with_cancer':percent_of_beneficiaries_with_cancer,
                    'percent_of_beneficiaries_with_diabetes':percent_of_beneficiaries_with_diabetes
                }
        }
    )
    print(dataset)