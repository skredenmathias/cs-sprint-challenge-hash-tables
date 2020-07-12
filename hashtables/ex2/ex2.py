#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source # Starting airport
        self.destination = destination # next airport

# First flight: Source = None
# Final flight: destination = None, has a source

# Hash each ticket such that:
    #   cache[source] = destination

    #   thereby, the ith location (source) can be found by checking cache[i-1]
import random

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

# DCA
# DCA
# PDX
# DCA
# NONE
# DCA
# DCA
# NONE
# PDX
# DCA
# NONE
# NONE
# DCA
# DCA
# PDX
# DCA
# DCA
# NONE
# NONE
# NONE
# DCA
# PDX
# DCA
# PDX
# DCA
# DCA
# DCA
