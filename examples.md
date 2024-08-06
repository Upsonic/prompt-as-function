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

