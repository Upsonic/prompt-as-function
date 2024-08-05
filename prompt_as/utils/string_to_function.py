

def string_to_function(func_string):
    context = {}
    exec(func_string, context)

    for key, value in reversed(list(context.items())):
        if callable(value):
            return value  # returns the first callable object name
    
    raise ValueError("No function was found in the string.")
