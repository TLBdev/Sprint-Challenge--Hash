
def has_negatives(a):
    d = {}
    result = []
    for i in a:
        d[i] = True
    
    for k, v in d.items(): 
        if k > 0 and 0 - k in d:
            result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
