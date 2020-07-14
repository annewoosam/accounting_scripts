"""Print out all the melons in our inventory."""


from melons import melons # you only have to import the dictionary name versus each 
#item tracked rather than specifying the melon names and the attribute or characteristic/feature name individually


def print_melon(melons): # the dictionary name is passed as the parameter
# so that interpreter knows where to pull attributes from 
    """Print each melon with corresponding attribute information."""

    for name, attributes in melons.items(): # the name is the first feature or key whose features are being defined; 
    #the attributes are the characteristics you define. Every key must have the same characteristics.
       print(name.upper()) # this prints the watermelon name in uppercase

       for attribute,value in attributes.items():#items are the characteristics which have a value such as 
       # None, a boolean, a string, a float or an int. Here the code says that for every attribute and value print 
       # the attribute and value fields line by line
           print(f'{attribute}:{value}')
       print('-')

print_melon(melons)