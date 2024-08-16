from functools import wraps
import inspect

try:
    from .prompt_to_code import prompt_code
    from .prompt_to_function import prompt_to_function
except:
    from prompt_as.prompt_to_code import prompt_code
    from prompt_as.prompt_to_function import prompt_to_function


def pf(*args, tester=False, function_just=False):
    def decorator(func):
        @wraps(func)
        def real_decorator(*inner_args, **inner_kwargs):
            print("name: ", func.__name__)
            print("args: ", inner_args)
            print("kwargs: ", inner_kwargs)
            print("explanation: ", func.__doc__)

            training_prompt = (
                f"That named as '{func.__name__}'. USE THIS NAME AS FUNCTION NAME. "
                f"And the signature should be: {inspect.signature(func)}. "
                f"It is being called with the arguments {inner_args} and keyword arguments {inner_kwargs}. "
                f"And make this operation with args: {func.__doc__}"
            )
            if tester:
                print(training_prompt)
            if not function_just:
                result = prompt_code(
                    str(training_prompt), tester=tester, function_name=func.__name__
                )
            else:
                result = prompt_to_function(
                    str(training_prompt), tester=tester, function_name=func.__name__
                )
            return result

        return real_decorator

    # Allows usage as either a plain decorator (without parentheses)
    # or a decorator factory (with parentheses).
    if args and callable(args[0]):
        return decorator(args[0])
    else:
        return decorator
