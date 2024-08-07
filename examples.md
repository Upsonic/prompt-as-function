# Example @pf Functions

```python

@pf
def save_user(username:str, password:str):
    """
    Saves the given username and pass to an sqlite database.
    If there is no exception return True otherwise return False
    """

```


```python

@pf
def check_password(username:str, password:str):
    """
    Checks the given password is correct for given username username in the sqllite database.
    And return True or False bool
    """

```

```python

@pf
def my_ip():
    """
    Returns the IP of machine, if there is an exception it should return None
    """

```

```python

@pf
def hackernews():
    """
    Returns the latest hacker news posts (10) in a list format with their links. If there is an exception return None
    """

```

```python

@pf
def encrypt_via_fernet(data:str, encryption_key:str) -> str:
    """
    Encrypts data with encryption_key string and returns the encrypted data.
    I will give encryption_key in string format and you will use for key generation. 
    If there is an exception return None.
    If succed you will return string to me.
    """

```

```python

@pf
def decrypt_via_fernet(encrypted_data:str, encryption_key:str) -> str:
    """
    Decrypts data with encryption_key string and returns the decrypted data. 
    I will give encryption_key in string format and you will use for key generation. 
    If there is an exception return None.
    If succed you will return string to me.
    """

```

```python

@pf
def total_memory_size_in_gb()->int:
    """
    Returns the total memory in gigabytes of the machine. put "GB" at the end of the result If there is an exception return None
    """
 ```

```python
@pf
def available_disk_space_in_gb()->int:
    """
    Returns the available disk space in gigabytes of the machine. put "GB" at the end of the result  If there is an exception return None
    """
```

```python
@pf
def system_time_and_date()->str:
    """
    Returns the current system time and date. Returns None if there is an error fetching the time.
    """
```

```python
@pf
def operating_system() -> str:
    """
    Returns the name of the operating system. Returns None if unable to detect.
    """
```    

```python
@pf 
def all_running_processes()-> list:
    """
    Lists all currently running processes sort them two by two. Returns 'Process list cannot be retrieved' in case of an error.Lists all currently running processes
    """

```

```python 
@pf
def battery_status()-> str:
    """
    Returns the charge percentage of the machine's battery and whether it is charging. If unsuccessful, return None.
    """

```
```python
def network_status()-> str:
    """
    Checks if the machine is connected to a network. Returns 'Connected' or 'Disconnected'. If unsuccessful, return None.
    """
```
