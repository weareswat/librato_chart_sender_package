import sys

class UnknownKeyError(Exception):
    pass

class ApiKeyManager():
    def __init__(self):
        self.mailgun_key = None
        self.librato_key = None

    def get_key(self, key_name):
        try:
            return eval('self.{key_name}_key'.format(key_name=key_name))
        except AttributeError:
            raise UnknownKeyError('key_name doesn\'t exist')

    def set_keys(self, librato_key, mailgun_key):
        self.librato_key = librato_key
        self.mailgun_key = mailgun_key