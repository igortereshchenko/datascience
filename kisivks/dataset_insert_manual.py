import kisivks.dataset_structure


def add_to_dataset(dataset: dict, provider_id: int, zip_code: int,
                   percent_of_beneficiaries_with_ra_oa: int,
                   percent_of_beneficiaries_with_stroke: int):
    dataset[provider_id] = {
        'zip_code': zip_code,
        'percent_of_beneficiaries_with_ra_oa': percent_of_beneficiaries_with_ra_oa,
        'percent_of_beneficiaries_with_stroke': percent_of_beneficiaries_with_stroke
    }


add_to_dataset(kisivks.dataset_structure.dataset, 368274, 43231, 69, 0)

print(kisivks.dataset_structure.dataset)