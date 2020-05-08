
def intersection(arrays):
    #opt: could use a list of dicts in place of d to handle repeat numbers
    #would need to be traversed with nested look like 2d arary
    d = {}
    result = []
    for i in range(len(arrays)):
        for x in range(len(arrays[i])):
            if arrays[i][x] not in d:
                d[arrays[i][x]] = 1
            else: 
                d[arrays[i][x]] += 1
        
        for k, v in d.items():
            if v == len(arrays):
                result.append(k)
    print(result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
