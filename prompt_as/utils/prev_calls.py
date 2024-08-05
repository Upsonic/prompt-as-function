from functools import wraps
from collections import defaultdict




func_param_storage = defaultdict(dict)

def save_args_decorator(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
       # Save the function parameters
       func_param_storage[func.__name__]['args'] = args
       func_param_storage[func.__name__]['kwargs'] = kwargs
       # Execute the function
       result = func(*args, **kwargs)
       func_param_storage[func.__name__]['result'] = result
       return result
   return wrapper



def reset_calls():
    global func_param_storage
    func_param_storage = defaultdict(dict)

def get_previosly_last_return_of_near_element(element):
    if element in func_param_storage:
        print(func_param_storage[element])
        return func_param_storage[element]["result"]
    else:
        return ""
def get_previosly_last_call_of_near_element(element):
    if element in func_param_storage:
        return str(func_param_storage[element])
    else:
        return ""
