from dovgaleo.dataset_structure import dataset


def recursion(dataset, provider_ids=[]):
    if len(provider_ids) == 0:
        return recursion(dataset, provider_ids=list(dataset.keys()))

    current = dataset[provider_ids[0]]
    if current['city'] == 'IRWINDALE' and current['total_episodes_non_lupa'] > 1000:
        print(f"{provider_ids[0]}\n{current['zip_code']}\n{current['city']}")

    if len(provider_ids[1:]) == 0: return
    recursion(dataset, provider_ids=provider_ids[1:])


recursion(dataset)
