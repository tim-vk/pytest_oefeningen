# Niet spieken!


























# Foei, Jij bent nu aan het spieken. De volgende training moet je koekjes meenemen.

def order_beer(value):

    if type(value) is not int:
        if type(value) is str and not value.isdigit():
            raise TypeError("Only ints are allowed")
    return int(value)
