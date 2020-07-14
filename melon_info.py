"""Print out all the melons in our inventory."""


from melons import melon_names, seedless, price, flesh-color,weight,rind-color,locale


def print_melon(name, seedless, price, flesh-color, weight, rind-color, locale):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
