from PindaMV.dataset_structure import dataset


def add_row(latin, year, wire, inf, year2, wire2, inf2):
    dataset.update({latin: {year: {'wire_other': wire, 'inf_other': inf}, year2: {'wire_other': wire2, 'inf_other': inf2}}})
    return dataset

new_ds = add_row('FRAXINUS PENNSYLVANICA', 2006, 'No', 'No', 2005, 'No', 'No')

print(new_ds)
