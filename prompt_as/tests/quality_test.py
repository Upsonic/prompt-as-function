

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







def quality_test():

    test_1 = Prompt_As_Test_System(hackernews, [([],{})], None, [None]).run_test()

    test_2 = Prompt_As_Test_System(my_ip, [([],{})], None, [None]).run_test()

    test_3 = Prompt_As_Test_System(save_user, [(["onuratakan", "6431"],{})], [True], [None]).run_test()


    test_4 = Prompt_As_Test_System(check_password, [(["onuratakan", "13532"],{})], [False], [None]).run_test()


    test_5 = Prompt_As_Test_System(check_password, [(["onuratakan", "6431"],{})], [True], [None]).run_test()


    print("\n\n\n\n\n*******************")

    print("All results:\n")

    print(test_1)
    print(test_2)
    print(test_3)
    print(test_4)
    print(test_5)