def d_insert(ds, arg):
    ds.update(arg)
    return ds


dataset = {
    'one': {
        'roma': 'I',
        'arab': '1'
    },
    'two': {
        'roma': 'II',
        'arab': '2'
    }
}
test = {
    'three': {
        'roma': 'III',
        'arab': '3'
    }

}
dataset = d_insert(dataset, test)
print(dataset)
