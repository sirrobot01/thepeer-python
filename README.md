# ThePeer Python UNOFFICIAL SDK


This is an unofficial SDK

## Installation

```shell
pip install thepeer
```

## Usage

````python
from thepeer import ThePeer

the_peer = ThePeer(token='your-secret-key')

the_peer.charge_link("link-id", 4300, 'The Yatch')

````


### Available methods

* validate_signature
    - `accepts`: 
        - payload (dict)
        - signature (str)
    - `returns`: boolean

    
* authorize_send
    - `accepts`: 
        - receipt (string)
        - event (string)
    - `returns`: (Response object)
    
* index_user
    - `accepts`:
        - name (string)
        - email (string)
        - identifier (string)
    - `returns`: (Response object)
        
* update_user
    - `accepts`:
        - reference (string)
        - identifier (string)
    - `returns`: (Response object)
        
* delete_user
    - `accepts`:
        - reference (string)
    - `returns`: (Response object)
    
* get_link
    - `accepts`:
        - lind_id (string)
    - `returns`: (Response object)

* get_user_links
    - `accepts`:
        - lind_id (string)
    - `returns`: (Response object)

* charge_link
    - `accepts`:
        - reference (string)
    - `returns`: (Response object)

* get_transaction
    - `accepts`:
        - transaction_id (string)
    - `returns`: (Response object)

* refund_transaction
    - `accepts`:
        - transaction_id (string)
        - reason (Optional[string])
    - `returns`: (Response object)
    
* authorize_direct_charge
    - `accepts`:
        - reference (string)
        - event (string)
    - `returns`: (Response object)

* test_crediting
    - `accepts`:
        - amount (integer)
        - user_reference (string)
    - `returns`: (Response object)

### TODO

- Testing

## Extra

Refer to the [documentation](https://docs.thepeer.co) for more information.
