def recursion():
    if int(male_beneficiaries/female_beneficiaries) > 0.3:
        print(agency-name,male_beneficiaries/female_beneficiaries*100,male_beneficiaries,female_beneficiaries)
        return recursion()


