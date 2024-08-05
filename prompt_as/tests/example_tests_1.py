import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.test_system import Test

from prompt_as.prompt_as_f_decorator import prompt_as_f


@prompt_as_f
def hackernews():
    """
    Returns the latest hacker news posts (10) in a list format with their links. If there is an exception return None
    """





Test(hackernews, [([],{})], None, [None]).run_test()

