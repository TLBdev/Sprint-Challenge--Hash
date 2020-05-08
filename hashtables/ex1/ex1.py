
def get_indices_of_item_weights(weights, length, limit):
    d = {}
    for i in range(len(weights)):
        if limit - weights[i] not in d:
            d[limit - weights[i]] = [i]
        else: 
            d[limit - weights[i]].append(i)
    
    for k, v in d.items():
        if limit - k in d:
            if k == limit - k:
                return[d[k][-1], d[k][-2]]
            if d[k] > d[limit - k]:
                print(d[k][0], d[limit - k][0])
                return[d[k][0], d[limit - k][0]]
            else:
                print(d[limit - k], d[k])
                return [d[limit - k][0], d[k][0]]

    return None
