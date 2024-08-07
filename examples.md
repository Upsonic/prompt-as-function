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

@pf
def network_status()-> str:
    """
    Checks if the machine is connected to a network. Returns 'Connected' or 'Disconnected'. If unsuccessful, return None.
    """
```

```python
@pf
def network_speed_tests()-> str:
    """
    It returns whether the machine is connected to the internet and upload, download and latency values ​​in Mb/sec. In case of error, it returns none.   
    """

```

```python
@pf
def system_locales()-> str:
    """
    Returns the current locale setting of the system. Returns None on error.    
    """
```

```python
@pf
def speaker_volume()-> str:
    """
    Returns the current speaker volume level as a percentage. Returns None on error.
    """
```
```python
@pf
def audio_volume()-> str:
    """
    Returns the current audio volume level as a percentage. Returns None if it cannot be retrieved.
    """
```

```python
@pf
def wifi_signal_strength()-> str:
    """
   Measures and returns of the  machine the WiFi signal strength as a percentage. Returns None on error.
    """

```

```python
@pf
def bluetooth_connection_status()-> str:
    """
    Checks if the machine is connected to a bluetooth. Returns 'Connected' or 'Disconnected'. Returns None if it cannot be retrieved.
    """
```

```python 
@pf
def machine_ram()-> int:
    """
    Returns the RAM of machine from int, if there is an exception it should return None.
    """

```

```python 
@pf
def get_btc_price()-> int:
    """
    Returns the BTC price from int , if there is an exception it should return None
    """
```

```python 
@pf
def get_eth_price()-> int:
    """
    Returns the ETH price from int, if there is an exception it should return None
    """

```


```python
@pf
def get_usd_to_bbd_price()-> str:
    """
    Returns the USD-BBD pair price, if there is an exception it should return None
    """

``` 

```python

@pf
def get_city_weather(city)-> int:
    """
    Returns the given city weather from int used web if there is an exception it should return None
    """


```


```python

@pf
def calculate_age(birthdate)-> int:
    """
    Calculates and return from int the age based on the provided birthdate. If the birthdate is invalid or in the future, returns None.
    """
```

```python 
@pf
def convert_temperature(temp, unit)-> str:
    """
    Converts a temperature from Celsius to Fahrenheit or vice versa. Input is temperature and 'C' for Celsius or 'F' for Fahrenheit.
    Returns None if the unit is invalid.

    """
```

```Python 
@pf
def parse_url(url)-> str:
    """
    Parses a URL and returns its components. if there is an exception it should return None
    """
```

```Python 
@pf
def add_single_digit(number_one, number_two) -> int:
"""
Adds two single digit numbers and returns in int format. if there is an exception it should return None
"""
```





