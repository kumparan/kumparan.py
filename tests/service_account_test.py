import unittest
import os

from kumparan import service_account


class TestSupervisedAccount(unittest.TestCase):

    def test_get_credentials_not_set(self):
        # Unset env variable
        del os.environ["SERVICE_ACCOUNT_CREDENTIALS"]

        with self.assertRaises(EnvironmentError):
            service_account.get_credentials()

    def test_get_credentials_invalid_json(self):
        # Set env variable
        os.environ["SERVICE_ACCOUNT_CREDENTIALS"] = "invalid json"

        with self.assertRaises(Exception):
            service_account.get_credentials()


if __name__ == '__main__':
    unittest.main()
