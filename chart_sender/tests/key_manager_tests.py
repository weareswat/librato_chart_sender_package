from unittest2 import TestCase
from chart_sender.lib.key_manager import ApiKeyManager, UnknownKeyError


class ApiKeyManagerTests(TestCase):

    def test_key_presence(self):
        key_manager = ApiKeyManager()
        librato_key, mailgun_key = '123254tqrafedws-librato', 'key-bsef31vsf3qe'
        key_manager.set_keys(librato_key, mailgun_key)

        self.assertEqual(key_manager.get_key('librato'), librato_key)
        self.assertEqual(key_manager.get_key('mailgun'), mailgun_key)

    def test_unknown_key(self):
        key_manager = ApiKeyManager()
        librato_key, mailgun_key = '123254tqrafedws-librato', 'key-bsef31vsf3qe'
        key_manager.set_keys(librato_key, mailgun_key)
        self.assertRaises(UnknownKeyError, key_manager.get_key, 'unknown_key')

    def test_empty_key(self):
        key_manager = ApiKeyManager()
        librato_key, mailgun_key = '123254tqrafedws-librato', 'key-bsef31vsf3qe'
        key_manager.set_keys(librato_key, mailgun_key)
        self.assertRaises(UnknownKeyError, key_manager.get_key, None)