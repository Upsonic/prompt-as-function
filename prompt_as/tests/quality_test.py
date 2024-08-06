

try:
    from .test_system import Prompt_As_Test_System
    from ..prompt_as_f_decorator import pf
except ImportError:
    from test_system import Prompt_As_Test_System
    from prompt_as_f_decorator import pf



@pf
def save_user(username:str, password:str):
    """
    Saves the given username and pass to an sqlite database.
    If there is no exception return True otherwise return False
    """


@pf
def check_password(username:str, password:str):
    """
    Checks the given password is correct for given username username in the sqllite database.
    And return True or False bool
    """







@pf
def my_ip():
    """
    Returns the IP of machine, if there is an exception it should return None
    """






@pf
def hackernews():
    """
    Returns the latest hacker news posts (10) in a list format with their links. If there is an exception return None
    """



@pf
def encrypt_via_fernet(data:str, encryption_key:str) -> str:
    """
    Encrypts data with encryption_key string and returns the encrypted data.
    I will give encryption_key in string format and you will use for key generation. 
    If there is an exception return None.
    If succed you will return string to me.
    """

@pf
def decrypt_via_fernet(encrypted_data:str, encryption_key:str) -> str:
    """
    Decrypts data with encryption_key string and returns the decrypted data. 
    I will give encryption_key in string format and you will use for key generation. 
    If there is an exception return None.
    If succed you will return string to me.
    """









class QualityTest:
    def __init__(self, test_systems):
        self.test_systems = test_systems

    def run_tests(self):
        results = []
        for test_system in self.test_systems:
            result = test_system.run_test()
            results.append(result)

        print("\n\n\n\n\n*******************")
        print("All results:\n")
        for result in results:
            print(result)

# Example usage:
test_systems = [
    Prompt_As_Test_System(hackernews, [([],{})], None, [None]),
    Prompt_As_Test_System(my_ip, [([],{})], None, [None]),
    Prompt_As_Test_System(save_user, [(["onuratakan", "6431"],{})], [True], [None]),
    Prompt_As_Test_System(check_password, [(["onuratakan", "13532"],{})], [False], [None]),
    Prompt_As_Test_System(check_password, [(["onuratakan", "6431"],{})], [True], [None])
]

quality_test = QualityTest(test_systems)
