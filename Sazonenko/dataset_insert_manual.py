import Sazonenko.dataset_structure as dt


def insert(dataset: dict, name: str, status: str, wire_htap: str, borocode: int):
    dataset[name] = {
        dt.STATUS: status,
        dt.WIRE_HTAP: wire_htap,
        dt.BOROCODE: borocode
    }


if __name__ == "__main__":
    insert(dt.dataset, 'TILIA AMERICANA', 'Dead', 'No', 5)
    print(dt.dataset)
