def recursion(data,count = [0],get_last_key=False,last_key=None,req=0):
    if not get_last_key:
        last_key = list(data.keys())[-1]
        get_last_key = True
    for key in data.keys():
        if 'red' in data[key]:
            count[0]+=1
        elif isinstance(data[key],dict):
            recursion(data[key],count,get_last_key,last_key,req+1)
    if last_key == key:
        result = int(count[0])
        count[0]=0
        return result
