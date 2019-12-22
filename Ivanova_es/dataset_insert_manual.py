import Ivanova_es.dataset_structure as d
def add_data(dataset: dict, latin_name: str, cen_year: int, whire_htap: bool, horz_plant: bool):
    dataset[latin_name] = {
        'cen_year': cen_year,
        'whire_htap': whire_htap,
        'horz_plant': horz_plant
        }

add_data(d.dataset, 'FRAXINUS PENNSYLVANICA', 2006, False, False)
print(d.dataset)