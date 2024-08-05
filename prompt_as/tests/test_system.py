



import time
import traceback
class Prompt_As_Test_System:

    def __init__(self, function, test_cases, expected_outputs, bad_outputs):
        self.function = function
        self.test_cases = test_cases
        self.expected_outputs = expected_outputs
        self.bad_outputs = bad_outputs

    def run_test(self):
        the_text = ""

        total_cases = len(self.test_cases) if self.test_cases else 0
        successes = 0

        for index, test_case in enumerate(self.test_cases):
            try:
                args, kwargs = test_case
                start_time = time.perf_counter()
                output = self.function(*args, **kwargs)
                end_time = time.perf_counter()

                if self.expected_outputs:
                    assert output in self.expected_outputs

                if self.bad_outputs:
                    assert output not in self.bad_outputs

                successes += 1
                the_text += f"Test {index+1} Passed in {end_time - start_time} seconds: output = {output}"

            except Exception as e:

                the_text += f"Test {index+1} Failed: {e}"

        the_text += f"{successes}/{total_cases} tests passed"

        print(the_text)
        return the_text