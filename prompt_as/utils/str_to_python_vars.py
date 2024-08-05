import ast

def str_to_python_var(s):
    s = s.replace("<RESULT_OF_TOOL>", "")
    s = s.replace("</RESULT_OF_TOOL>", "")
    if (s[0] == s[-1]) and s.startswith(("'", '"')):  
        s = s[1:-1]       
    print("TRANSFORMING: ", s)
    try:
        # Attempt to evaluate the string and convert
        # it to a Python object
     
        return ast.literal_eval(s)
    except (SyntaxError, ValueError):
        # If it raises a SyntaxError, this means that the string 
        # is not a Python datatype (e.g., it's a regular string)
        print("Error on transforming to python object")
        return s
    

