import hashlib

the_previously_function_codes = {}

def get_old_codes(description):
    print("REQUESTED OLD CODES FOR: ", description)
    description = hashlib.sha256(description.encode()).hexdigest()
    if description in the_previously_function_codes:
        return the_previously_function_codes[description]["code"]
    else:
        return ""

def get_old_functions(description):

    description = hashlib.sha256(description.encode()).hexdigest()
    if description in the_previously_function_codes:
        return the_previously_function_codes[description]["name"]
    else:
        return ""








the_functions = {}

def get_function_index():
    global the_functions
    return list(the_functions)

def get_code_of_function(function_name:str):
    """
    Return code of given function
    """
    global the_functions
    return the_functions[function_name]

def set_function_to_code_base(function_name, function_code):
    global the_functions
    the_functions[function_name] = function_code



def reset_functions():
    global the_functions
    the_functions = {}
