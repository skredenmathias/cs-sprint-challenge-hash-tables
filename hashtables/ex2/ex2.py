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
    first_ticket = False
    last_ticket = False
    final_route = []
    cache = {}
    
    if Ticket.source = None:
        first_ticket = True
    
    if Ticket.destination = True:
        last_ticket = True

    for ticket in tickets:
        cache[Ticket.source] = Ticket.destination

    for source, destination in cache.items():
        if destination == source:

    key_list = list(cache.keys())

    while len(final_route) != length:
        key = random.choice(list(cache.keys()))



    return route


def random_sentences():
    sentence = ''
    for i in range(5):
        key = random.choice(list(cache.keys()))
        # for key, value in cache.items():
        for i in range(15):
            # sentence = ''
            sentence += key
            sentence += ' '
            # sentence += random.choice(value)
            sentence += ' '
            key = random.choice(cache[key])
    return sentence

    cache = {}
    # prev = None
    # for word in words.split():
    for i in range(len(words)):
        word = words[i]
        # TODO: analyze which words can follow other words
        if word not in cache:
            if i+1 in range(len(words)):
                cache[word] = [words[i+1]]
        else:
            if i+1 in range(len(words)):
                cache[word].append(words[i+1])