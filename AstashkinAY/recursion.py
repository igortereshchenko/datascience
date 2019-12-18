from datetime import datetime

example = {
    "956883": {
        "name": "Stylish Queen Anne Apartment",
        "host_name": "Maija",
        "host_since": "2011-08-11"
    },
    "5177328": {
        "name": "Bright & Airy Queen Anne",
        "host_name": "Andrea",
        "host_since": "2013-02-21"
    },
    "16708587": {
        "name": "New Modern House-Amazing water view",
        "host_name": "Jill",
        "host_since": "2014-06-12"
    }
}

lst = [value for value in example.values()]


def iterate(d, i):
    obj = d[i]
    dt = datetime.strptime(obj['host_since'], '%Y-%m-%d')
    dif = (datetime.now() - dt).days
    if dif > 365:
        print(f"name: {obj['name']}, host_name: {obj['host_name']}")
    if i is not len(d)-1:
        iterate(d, i + 1)


iterate(lst, 0)

