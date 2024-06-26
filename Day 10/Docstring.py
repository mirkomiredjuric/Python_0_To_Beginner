def format_name(name, lastname):
    """
    
    :param name: 
    :param lastname: 
    :return: 
    """ #this is docstring
    if name == "" or lastname == "":
        return "You didn't provide valid inputs."
    return f"{name} {lastname}"
