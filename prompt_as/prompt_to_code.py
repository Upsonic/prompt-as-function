
import os
import ast


import logging

# Get the logger for 'httpx'
httpx_logger = logging.getLogger("httpx")

# Set the logging level to WARNING to ignore INFO and DEBUG logs
httpx_logger.setLevel(logging.WARNING)



from langchain_openai import ChatOpenAI

from crewai import Agent, Task, Crew, Process


from crewai_tools import tool

import hashlib



import inspect 

import time


try:
  from .utils.get_tiger_tools import get_tiger_tools
  from .utils.fix_string import fix_string
  from .utils.generate_file_tree import generate_file_tree
  from .utils.string_to_function import string_to_function
  from .utils.str_to_python_vars import str_to_python_var
  from .utils.notes import get_notes, add_note, reset_notes
  from .utils.old_functions import get_old_codes, get_old_functions, the_previously_function_codes, get_code_of_function, set_function_to_code_base, the_functions, get_function_index, reset_functions
  from .utils.prev_calls import save_args_decorator, get_previosly_last_return_of_near_element, get_previosly_last_call_of_near_element, reset_calls
  from .prompt_to_function import prompt_to_function
  from .utils.configs import OPENAI_API_KEY
except:
    from utils.get_tiger_tools import get_tiger_tools
    from utils.fix_string import fix_string
    from utils.generate_file_tree import generate_file_tree
    from utils.string_to_function import string_to_function
    from utils.str_to_python_vars import str_to_python_var
    from utils.notes import get_notes, add_note, reset_notes
    from utils.old_functions import get_old_codes, get_old_functions, the_previously_function_codes, get_code_of_function, set_function_to_code_base, the_functions, get_function_index, reset_functions
    from utils.prev_calls import save_args_decorator, get_previosly_last_return_of_near_element, get_previosly_last_call_of_near_element, reset_calls
    from prompt_to_function import prompt_to_function
    from utils.configs import OPENAI_API_KEY



def prompt_code(prompt, tester=False, custom_the_result=None, function_name=None):
    start_time = time.time()
    verbose_level = False
    if tester:
        print("Verbose activated")
        verbose_level = True

    function_start_time = time.time()
    the_result = prompt_to_function(prompt, tester=tester, more=True, function_name=function_name) if custom_the_result == None else custom_the_result
    function_end_time = time.time()
    the_tool_func = the_result["function"]
    the_tool = save_args_decorator(the_result["function"])
    the_releated_functions = the_result["related"]
    the_releated_codes = the_result["related_codes"]


        
    previosly_calls = ""
    for each_f in the_releated_functions:
        previosly_calls += "\n\nFunction:"+ each_f + "\nCALL" + get_previosly_last_call_of_near_element(each_f)

    llm = ChatOpenAI(model="gpt-4-turbo", api_key=OPENAI_API_KEY(), verbose=verbose_level)


    
    coder = Agent(
      role="Senior Python Developer with high level function as a service knowledge",
      goal="Running functions by request",
      backstory="You are graduated from Computer Science department of University and worked in biggest tech companies.",
      verbose=verbose_level,
      llm=llm
    )
    

    task_prompt = f"""
<USER>
{prompt} - please make this with {the_tool.__name__} function.
</USER>

<NOTES>
{get_notes()}
</NOTES> 

<OLD_CALLS>
{previosly_calls}
</OLD_CALLS>


<SYSTEM>
- Please read the notes for taking some important point like db paths, log locations and used libraries, db tables, etc.

- working directory (Dont use any other directory for any purpose) don't use sub folders if you need a file please specify above this:
{os.getcwd()}

- Think like a software developer and seperate the database tables, note them, create databases and somethings.

</SYSTEM>


DO USER REQUEST

"""
    


    the_tool = tool(the_tool)
    the_tool.func
    file_reader_tool = tool(generate_file_tree)

    
    task1 = Task(
      description=task_prompt,
      expected_output="""
RUNNED or NOT RUNNED
""",
      agent=coder,        
      tools=[the_tool, file_reader_tool, tool(add_note)]
    )



    class sub_class(Task):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.description = self.description_
    
        @property
        def description_(self):
            return f"""
<CALL>
{get_previosly_last_call_of_near_element(the_tool_func.__name__)}
</CALL>

<USER>
Extract some important points like table names, file locations and decisions. 
After that take notes via add_note tool.
If nothing important just pass don't add any note.
Dont take notes for requlary things
</USER>
"""

    
    task2 = sub_class(
      description="",
      expected_output="""
IF NOTES LEN BIGGER THAN 0
<TOOK_NOTES>
-
</TOOK_NOTES>   
ELSE
<TOOK_NOTES>
PASS
</TOOK_NOTES>   
""",
      agent=coder,
      tools=[tool(add_note)]
    )
    
    crew = Crew(
      agents=[coder],
      manager_llm=llm,
      tasks=[task1, task2],
      verbose=verbose_level,     
      share_crew=False
    )
    
    
    result = crew.kickoff()
    the_result = get_previosly_last_return_of_near_element(the_tool_func.__name__)
    end_time = time.time()

    function_time = int(function_end_time - function_start_time)
    print("FUNCTION TIME", function_time)
    total_time = int(end_time - start_time)
    interpreting_time = total_time - function_time
    print("INTERPRETING TIME", interpreting_time)
    print("TOTAL TIME", total_time)
    return the_result




















