from dataset_structure import dataset

def recursion(dataset):
    if len(dataset) == 0:
        return False
    agency = dataset.pop(next(iter(dataset)))
    agency_name = agency.get("agency_name")
    female_beneficiaries = int(agency.get("female_beneficiaries"))
    male_beneficiaries = int(agency.get("male_beneficiaries"))
    if male_beneficiaries/female_beneficiaries > 0.3:
        print(agency_name, male_beneficiaries, female_beneficiaries, male_beneficiaries / female_beneficiaries * 100)
    recursion(dataset)

print(recursion(dataset))













