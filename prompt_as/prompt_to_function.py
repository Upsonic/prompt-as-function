
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew, Process
import hashlib

try:
  from .utils.old_functions import get_function_index, get_code_of_function, set_function_to_code_base, get_old_functions, get_old_codes, the_functions, the_previously_function_codes
  from .utils.string_to_function import string_to_function
  from .utils.get_tiger_tools import get_tiger_tools
  from .utils.fix_string import fix_string
  from .utils.notes import get_notes
  from .utils.configs import OPENAI_API_KEY
except:
  from utils.old_functions import get_function_index, get_code_of_function, set_function_to_code_base, get_old_functions, get_old_codes, the_functions, the_previously_function_codes
  from utils.string_to_function import string_to_function
  from utils.get_tiger_tools import get_tiger_tools
  from utils.fix_string import fix_string
  from utils.notes import get_notes
  from utils.configs import OPENAI_API_KEY



def prompt_to_function(prompt:str, tester:bool=False, more=False, function_name=None):
    print("Started for: ", prompt)
    global the_previously_function_codes
    verbose_level = False
    if tester:
        verbose_level = True
    
    llm = ChatOpenAI(model="gpt-4-turbo", api_key=OPENAI_API_KEY(), verbose=verbose_level)


    # Executor agent for making executions for mission
    coder = Agent(
      role="Senior Python Developer with high level function as a service knowledge",
      goal="Writing functions by request",
      backstory="You are graduated from Computer Science department of University and worked in biggest tech companies.",
      verbose=verbose_level,
      allow_delegation=False,
      llm=llm
    )





                       
    
    pre_check_prompt = f"""
<SYSTEM>
Hi, we have a operation came from user before the start please check the currenty function index and select some functions for understanding system design
</SYSTEM>

<IDEA>
{prompt}
</IDEA>

<FUNCTION_INDEX>
{get_function_index()}
</FUNCTION_INDEX>

<USER>
Select some functions by IDEA to understand system design. You are free to learn more about system, save mechanism and anything that you want to know.
</USER>


DO USER REQUEST

"""



    def callback_function(output):
        print("The related functions: ", output.raw)
        global the_previously_function_codes
        description = hashlib.sha256(output.description.encode()).hexdigest()
        the_previously_function_codes[description] = {"code":"", "name":[]}
        for each_function in get_function_index():
            if each_function in output.raw:
                the_previously_function_codes[description]["code"] += "\n" + get_code_of_function(each_function)
                the_previously_function_codes[description]["name"].append(each_function)



    taskpre = Task(
      description=pre_check_prompt,
      expected_output="""
IF THERE RELEATED_FUNCTIONS LEN BIGGER THAN 0
<releated_functions_names>
- 
</releated_functions_names>
ELSE
<releated_functions_names>
pass
</releated_functions_names>
""",
      agent=coder,
      callback=callback_function
    )    
    print("\nNotes: ", get_notes())
    print("\nFunction index: ", get_function_index())



    

    class sub_class_(Task):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.description = self.description_
    
        @property
        def description_(self):
            return f"""
<SYSTEM>
Write a python function that makes  by the Function Plan

if there is a needed library then put into inside of function. 

Dont write any usage example. Just function please. 

Please prefer easy to use (prefer sqlite rather than psycopg2) libraries.

Please be careful about user function name suggestion. It should be exacly same otherwise user can be verry angry and fire all of us.
</SYSTEM>    

<USER_REQUEST>
{prompt}
</USER_REQUEST>

<NOTES>
{get_notes()}
</NOTES>

<OLD_FUNCTIONS>
{get_old_codes(pre_check_prompt)}
</OLD_FUNCTIONS>


<SYSTEM>
Please read the notes for taking some important point like db paths, log locations and used libraries, etc.
</SYSTEM>

"""
            
            
    
    task1 = sub_class_(
      description="",
      expected_output="""
<code>
The imports
The function
</code>
""",
      agent=coder,
    )

    task2 = Task(
      description=f"""
Please rewrite the function and please remove the localized things. 
Use parameters with annotation for localized things. 
If there is an parameter as object, rewrite the function with no parameter as object. 
BUT IF THE LOCALIZED THINGS DOESNT IMPORTANT FOR USER (Like online service URLs, static names and etc) DONT TRANSFORM IT. 
When you remove something please specify in docstring for an example

Dont change the function name.
""",
      expected_output="""
<code>
The imports
The function
</code>
""",
      agent=coder,        
      context=[task1],
    )    

    task3 = Task(
      description="""
<SYSTEM>
Dont write any other thing over than the requested output type. Just write the imports and the function after that and dont add any ``` or anything that not okey for python interpreter
</SYSTEM>

<USER>
Please rewrite the function with docstring, and be sure the output is in the requested format.
</USER>
""",
      expected_output="""
<code>
The imports
The function
</code>
""",
      agent=coder,        
      context=[task2],
    )    






    
    task4 = Task(
      description=f"""
<SYSTEM>
If there is needed library for the function, install it. Dont try to instal builtin library. Just install third party libraries.
</SYSTEM>
""",
      expected_output="""
<INSTALlLED_LIBRARIES>
- Library Name
</INSTALlLED_LIBRARIES>
""",
      tools=get_tiger_tools(),
      agent=coder,
      context=[task3]
    )        
    

    crew = Crew(
      agents=[coder],
      tasks=[taskpre, task1, task2, task3, task4],
      verbose=verbose_level,
      share_crew=False,  
    )
    

    if function_name == None or not function_name in the_functions:
        result = crew.kickoff()
    
    
        result = task3.output.raw
        
    
        result = fix_string(result)
        code_of_f = result

    


    

        
        print("\nGenerated Function: ", f"START{result}END")
        
        result = string_to_function(result)
    
        set_function_to_code_base(result.__name__, code_of_f)


    
        if not more:
            return result
        else:
            return {"function":result, "related": get_old_functions(pre_check_prompt), "related_codes": get_old_codes(pre_check_prompt)}
    else:
        print("USING OLD FUNCTION")
        result = the_functions[function_name]
        result = string_to_function(result)
        if not more:
            return result
        else:
            return {"function":result, "related": [function_name], "related_codes": ""}



