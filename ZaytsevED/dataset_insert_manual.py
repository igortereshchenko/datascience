from ZaytsevED.dataset_structure import dataset


def dataset_insert(dataset, prov_id, state, wh_benef, bl_benef):
    dataset[prov_id] = {
        'state': state,
        'white_beneficiaries': wh_benef,
        'black_beneficiaries': bl_benef
    }


dataset_insert(dataset, '784922', 'NY', 64, 81)
