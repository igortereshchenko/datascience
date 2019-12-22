def add_info(unique_number_of_patient, agency_name, average_hcc_score, percent_of_beneficiaries_with_asthma, dataset):
    dataset[unique_number_of_patient] = {"agency_name": agency_name, "average_hcc_score": average_hcc_score,
                                         "percent_of_beneficiaries_with_asthma": percent_of_beneficiaries_with_asthma}
