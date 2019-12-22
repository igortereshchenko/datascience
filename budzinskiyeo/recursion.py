
def main(data, find_this=None, count_this=None):
    if find_this is None:
        find_this = ["brand"]
    if count_this is None:
        count_this = ["categories"]
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                main(value, find_this, count_this)
            else:
                if key in find_this:
                    if data[key]:
                        for element in count_this:
                            print("Brand : {}\nCount : {}\n".format(", ".join(data[key]), len(data[element])))
