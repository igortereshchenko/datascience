import maliarenkoma.dataset_structure as ds


def add(dataset: dict, name: str, cen_year: int, inf_other: bool, zip_city: list):
    dataset[name] = {
        ds.CEN_YEAR: cen_year,
        ds.INF_OTHER: inf_other,
        ds.ZIP_CITY: zip_city
    }


if __name__ == "__main__":
    add(ds.dataset, "test", 2005, False, ["a", "b"])
    print(ds.dataset)
