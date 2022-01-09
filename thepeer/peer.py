from typing import Optional

import requests
from requests import Response
from thepeer.errors import TokenNotFound, Errors
from urllib.parse import urljoin

from thepeer.base import Send, Charge, Checkout, Transaction, Link


class ThePeer(Send, Checkout, Charge, Transaction, Link):
    BASE_URL = 'https://api.thepeer.co'
    AUTH_KEY = 'X-API-Key'
    
    def __init__(self, token):
        self.token = token
        
    def prepare_url(self, path: str = ''):
        return urljoin(self.BASE_URL, path)
    
    def make_request(self, method: str, path: str, params: Optional[dict] = None,
                     data: Optional[dict] = None, headers: Optional[dict] = None):
        if data is None:
            data = {}
        if params is None:
            params = {}
        if headers is None:
            headers = {}
            
        if not method:
            method = 'get'
            
        if not self.token:
            raise TokenNotFound
        
        headers.update({
            self.AUTH_KEY: self.token,
            'Accept': 'application/json'
        })
        
        response = getattr(requests, method.lower())(url=self.prepare_url(path), params=params,
                                                data=data, headers=headers)
        return self.process_response(response)
    
    @staticmethod
    def process_response(response: Response):
        status_code = response.status_code
        if status_code == 200 or status_code == 201:
            return response
        else:
            exc = Errors.get(status_code)
            err_message = response.json().get('message')
            errors = response.json().get('errors')
            if errors:
                raise Exception([exc(err.name for err in errors)])
            else:
                raise exc(err_message)
            
        
        