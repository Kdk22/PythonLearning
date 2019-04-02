def food(Burger: str, Drinks: str = 'Coca-Cola') -> str:
    ''' function(args:expression(type), args: expression(type) = 'Default value') -> (type that function returns)

        One is positional argument and another is keyword argument
    '''

    print("Annotation: ", food.__annotations__)
    print(Burger, Drinks)
    return Burger + ' and ' + Drinks

food('Ham')

# Sorter Docstring
# Type checking 
# Let IDEs show what types a function expects and returns

