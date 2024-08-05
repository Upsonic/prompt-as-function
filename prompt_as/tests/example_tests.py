import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.test_system import Test

from prompt_as.prompt_as_f_decorator import prompt_as_f


@prompt_as_f
def save_user(username:str, password:str):
    """
    Saves the given username and pass to an sqlite database.
    If there is no exception return True otherwise return False
    """


@prompt_as_f
def check_password(username:str, password:str):
    """
    Checks the given password is correct for given username username in the sqllite database.
    And return True or False bool
    """







@prompt_as_f
def my_ip():
    """
    Returns the IP of machine, if there is an exception it should return None
    """






@prompt_as_f
def hackernews():
    """
    Returns the latest hacker news posts (10) in a list format with their links. If there is an exception return None
    """



@prompt_as_f
def encrypt_via_fernet(data:str, encryption_key:str) -> str:
    """
    Encrypts data with encryption_key string and returns the encrypted data.
    I will give encryption_key in string format and you will use for key generation. 
    If there is an exception return None.
    If succed you will return string to me.
    """

@prompt_as_f
def decrypt_via_fernet(encrypted_data:str, encryption_key:str) -> str:
    """
    Decrypts data with encryption_key string and returns the decrypted data. 
    I will give encryption_key in string format and you will use for key generation. 
    If there is an exception return None.
    If succed you will return string to me.
    """













test_1 = Test(hackernews, [([],{})], None, [None]).run_test()

test_2 = Test(my_ip, [([],{})], None, [None]).run_test()

test_3 = Test(save_user, [(["onuratakan", "6431"],{})], [True], [None]).run_test()


test_4 = Test(check_password, [(["onuratakan", "13532"],{})], [False], [None]).run_test()


test_5 = Test(check_password, [(["onuratakan", "6431"],{})], [True], [None]).run_test()


print("\n\n\n\n\n*******************")

print("All results:\n")

print(test_1)
print(test_2)
print(test_3)
print(test_4)
print(test_5)