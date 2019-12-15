from MalakhatkaOV.dataset_structure import dataset


def wire_cont(ds, iter=0, count=0, borough=1):
    i = 0
    for tree in ds.values():
        if iter > i:
            i += 1
            continue
        elif tree['borocode'] == borough and tree['wire_other'] == 'Yes':
            count += 1
            i += 1
            return wire_cont(ds, iter=i, count=count)
        else:
            i += 1
    return count

print(wire_cont(dataset))
