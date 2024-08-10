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

[Example @pf Functions](https://github.com/Upsonic/prompt-as-function/blob/master/examples.md)



# Testing and Settings

<details>
<h1>Model Settings</h1>
You can change the OpenAI model that have been used for `prompt-as`.

```python
from prompt_as import prompt_as_config, pf


prompt_as_config.OPENAI_MODEL = "gpt-4-turbo"
# Model Setting

prompt_as_config.OPENAI_API_KEY = "sk-**"

@pf
def sleep(second:str) -> bool:
    """
    Sleeps for the given seconds and returns True.
    """



```


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

<h2>Quality Testing</h2>

If you want to test the working quality of this library, you can use the many different quality tests created.

```python

from prompt_as.tests.quality_test import quality_test


quality_test.run_tests() 

```

</details>
