

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
def my_ip() -> str:
    """
    Returns the IP of machine in str, if there is an exception it should return None
    """


@pf
def hackernews() -> list:
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


@pf
def total_memory_size_in_gb()->int:
    """
    Returns the total memory in gigabytes of the machine. put "GB" at the end of the result If there is an exception return None
    """

@pf
def available_disk_space_in_gb() -> int:
    """
    Returns the available disk space in gigabytes of the machine in integer format. If there is an exception return None
    """

@pf
def get_current_system_time() -> str:
    """
    Returns the current system time in string format. If there is an exception return None
    """

@pf
def operating_system() -> str:
    """
    Returns the name of the operating system. Returns None if unable to detect.
    """
 
@pf 
def all_running_processes()-> list:
    """
    Lists format all currently running processes. Returns None in case of an error. Lists format all currently running processes
    """   
    
@pf
def battery_status()-> str:
    """
    Returns the charge percentage of the machine's battery and whether it is charging. If unsuccessful, return None.
    """

@pf
def network_status()-> str:
    """
    Checks if the machine is connected to a network. Returns 'Connected' or 'Disconnected'. If unsuccessful, return None.
    """

@pf
def network_speed_tests()-> str:
    """
    It returns whether the machine is connected to the internet and upload, download and latency values ​​in Mb/sec. In case of error, it returns none.   
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
    Prompt_As_Test_System(hackernews, [([],{})], None, [None], list),
    Prompt_As_Test_System(my_ip, [([],{})], None, [None], str),
    Prompt_As_Test_System(save_user, [(["onuratakan", "6431"],{})], [True], [None]),
    Prompt_As_Test_System(check_password, [(["onuratakan", "13532"],{})], [False], [None]),
    Prompt_As_Test_System(check_password, [(["onuratakan", "6431"],{})], [True], [None]),
    Prompt_As_Test_System(total_memory_size_in_gb, [([],{})], None, [None], int),
    Prompt_As_Test_System(available_disk_space_in_gb, [([],{})], None, [None], int),
    Prompt_As_Test_System(get_current_system_time, [([],{})], None, [None], int),
    Prompt_As_Test_System(operating_system, [([],{})], None, [None], str),
    Prompt_As_Test_System(all_running_processes, [([],{})], None, [None], list),
    Prompt_As_Test_System(battery_status, [([],{})], None, [None], str),
    Prompt_As_Test_System(network_status, [([],{})], None, [None], str),
    Prompt_As_Test_System(network_speed_tests, [([],{})], None, [None], str),
    


]

quality_test = QualityTest(test_systems)
