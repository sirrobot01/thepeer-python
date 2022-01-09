from typing import Optional

from thepeer.errors import InvalidEventError


class User:
    def index_user(self, name, identifier, email):
        data = {
            'name': name, 'identifier': identifier, 'email': email
        }
        return self.make_request('POST', 'users/', data=data)

    def get_users(self, page: Optional[int] = None, perPage: Optional[int] = None):
        params = {
            'page': page, 'perPage': perPage
        }
        return self.make_request('GET', 'users/', params=params)

    def update_user(self, reference: str, **kwargs):
        return self.make_request('PUT', f'users/{reference}', data=kwargs)

    def delete_user(self, reference: str):
        return self.make_request('DELETE', f'users/{reference}')


class Checkout:
    Events = [
        'success', 'insufficient_funds', 'business_decline', 'user_decline'
    ]

    def authorize_checkout(self, reference: str, event: str):
        if event not in self.Events:
            raise InvalidEventError(f"'{event}' not valid. Valid choices {','.join(self.Events)}")
        data = {
            'event': event
        }
        return self.make_request('POST', f'checkout/{reference}', data=data)

class Send:
    Events = [
        'success', 'insufficient_funds'
    ]
    
    def authorize_send(self, receipt: str, event: str):
        if event not in self.Events:
            raise InvalidEventError(f"'{event}' not valid. Valid choices {','.join(self.Events)}")
        data = {
            'event': event
        }
        return self.make_request('POST', f'send/{receipt}', data=data)


class Charge:
    Events = [
        'success', 'insufficient_funds', 'business_decline', 'user_decline'
    ]
    
    def authorize_direct_charge(self, reference: str, event: str):
        if event not in self.Events:
            raise InvalidEventError(f"'{event}' not valid. Valid choices {','.join(self.Events)}")
        data = {
            'event': event
        }
        return self.make_request('POST', f'debit/{reference}', data=data)
    
    def charge_link(self, link_id: str, amount: int, remark: str):
        data = {"amount": amount, "remark": remark}
        return self.make_request('POST', f'link/{link_id}/charge', data=data)
        



class Transaction:
    pass


class Link:
    pass