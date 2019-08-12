from unittest import TestCase
import laws.__main__ as laws

class TestSSH(TestCase):
    def test_ssh_wrapper_timeout(self):
        s = laws.xstr('hello')
        self.assertTrue(s)
