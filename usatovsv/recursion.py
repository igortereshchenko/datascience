import usatovsv.dataset_structure as d

uni_names = []


def rec(dataset: dict, n: 0):

    key = list(dataset.keys())
    
    if n > len(key)-1:
        return
    else:
        if d.dataset[key[n]].get("spc_latin") not in uni_names:
            uni_names.append(d.dataset[key[n]].get("spc_latin"))

        rec(dataset,n+1)
    return len(uni_names)

print(rec(d.dataset,0))