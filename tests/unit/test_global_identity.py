
from tests import *

from global_identity.global_identity import GlobalIdentity


class TestExample(unittest.TestCase):

    def setup_method(self, method):
        GlobalIdentity.GLOBAL_IDENTITY_SERVER = 'dlpgi.dlp-payments.com'

    def test_authentication_user(self):
        global_identity = GlobalIdentity('40b2c09d-253b-4ade-ab40-cca08a30c551')
        response = global_identity.authenticate_user('account@email.com', 'account password')
        self.assertFalse(response['Success'])

        GlobalIdentity.GLOBAL_IDENTITY_SERVER = 'private-anon-1d6afe5fd-globalidentity.apiary-mock.com'

        response = global_identity.authenticate_user('account@email.com', 'account password')
        self.assertTrue(response['Success'])

    def test_validate_token(self):
        global_identity = GlobalIdentity('40b2c09d-253b-4ade-ab40-cca08a30c551')
        response = global_identity.validate_token('token')
        self.assertFalse(response['Success'])

        GlobalIdentity.GLOBAL_IDENTITY_SERVER = 'private-anon-1d6afe5fd-globalidentity.apiary-mock.com'

        response = global_identity.validate_token('token')
        self.assertTrue(response['Success'])

    def test_authenticate_application(self):
        global_identity = GlobalIdentity('40b2c09d-253b-4ade-ab40-cca08a30c551')
        response = global_identity.validate_application('00000000-0000-0000-0000-000000000000', 'secretekey', 'bananas')
        self.assertFalse(response['Success'])

        GlobalIdentity.GLOBAL_IDENTITY_SERVER = 'private-anon-1d6afe5fd-globalidentity.apiary-mock.com'

        response = global_identity.validate_application('00000000-0000-0000-0000-000000000000', 'secretekey', 'bananas')
        self.assertTrue(response['Success'])

    def test_is_user_in_role(self):
        global_identity = GlobalIdentity('40b2c09d-253b-4ade-ab40-cca08a30c551')
        response = global_identity.is_user_in_role('00000000-0000-0000-0000-000000000000', 'bananas')
        self.assertFalse(response['Success'])

        GlobalIdentity.GLOBAL_IDENTITY_SERVER = 'private-anon-1d6afe5fd-globalidentity.apiary-mock.com'

        response = global_identity.is_user_in_role('00000000-0000-0000-0000-000000000000', ['bananas'])
        self.assertTrue(response['Success'])
