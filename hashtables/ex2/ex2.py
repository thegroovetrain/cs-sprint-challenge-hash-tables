#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ht = {}
    for ticket in tickets:
        ht[ticket.source] = ticket.destination

    route = []
    curr = ht['NONE']
    while curr is not 'NONE':
        route.append(curr)
        curr = ht[curr]

    return route + ['NONE']