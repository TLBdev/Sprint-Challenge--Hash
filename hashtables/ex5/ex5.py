def finder(files, queries):
    result = []
    d = {}
    for i in files:
        split = i.split('/')
        if split[-1] not in d:
            d[split[-1]] = [i]
        else: 
            d[split[-1]].append(i)
    for i in queries:
        if i in d:
            for x in range(len(d[i])): 
                result.append(d[i][x])
    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
