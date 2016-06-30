import sys

class UnknownKeyError(Exception):
    pass

class ApiKeyManager():
    def __init__(self):
        self.mailgun_key = None
        self.librato_key = None

    def get_key(self, key_name):
        try:
            key_variable = 'self.{key_name}_key'.format(key_name=key_name)
            if key_name in ['librato', 'mailgun'] and eval(key_variable):
                return eval(key_variable)
            else:
                return "{key_name} key is empty. Exiting".format(file_name=key_name)
                sys.exit()
        except AttributeError:
            raise UnknownKeyError('key_name doesn\'t exist')

    def set_keys(self, librato_key, mailgun_key):
        self.librato_key = librato_key
        self.mailgun_key = mailgun_key