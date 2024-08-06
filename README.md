# Prompt as Function
**"Don't write any code, just tell what to do!"**

This is a significant milestone for Large Language Models (LLMs) and the coding process. The `prompt-as` library serves as a foundation for using prompts to perform tasks in Python. We are currently developing this mindset for several features in our products. With our open-source initiative <3, you can use it just like we do.


```console
pip install prompt-as
```


```python
from prompt_as import prompt_as_config, pf 

prompt_as_config.OPENAI_API_KEY = "sk-**"

@pf
def sleep(second:str) -> bool:
    """
    Sleeps for the given seconds and returns True.
    """


```



# Testing and Settings

<details>
<h1>Testing</h1>

If you want to test this library on a large scale, you can use our test system as well.

```python

from prompt_as import prompt_as_config, pf

prompt_as_config.OPENAI_API_KEY = "sk-**"

@pf
def sleep(second:str) -> bool:
    """
    Sleeps for the given seconds and returns True.
    """



# Testing

from prompt_as import Prompt_As_Test_System


Prompt_As_Test_System(sleep_time, [(["2"], {})], [True], [False]).run_test()
# (function_name, test_args_and_kwargs, expected_outputs, bad_outputs)

```

</details>
