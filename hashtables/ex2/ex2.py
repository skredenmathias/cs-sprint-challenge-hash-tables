import random

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    final_route = []
    cache = {}
    counter = 0

    for ticket in tickets:
        if ticket.source == 'NONE':
            final_route.append(ticket.destination)

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    while len(final_route) != length:
        for key, value in cache.items():
            if final_route[counter] == key:
                final_route.append(value)
                counter += 1

    return final_route
