#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

d = {}
def reconstruct_trip(tickets, length):
    route = []
    for i in tickets:
        d[i.source] = i.destination
    node = "NONE"
    while len(route) < length:
        route.append(d[node])
        node = d[node]
    print(route)
    return route
