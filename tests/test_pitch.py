import unittest
from app.models import Pitch,Comment

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch= 'you good')

    def test_password_setter(self):
        self.assertTrue(self.new_pitch.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises ( AttributeError ):
                self.new_pitch.pitch

    def test_password_verification(self):
            self.assertTrue ( self.new_pitch.verify_pitch( 'you good' ) )

    def tearDown(self):
        Pitch.query.delete ( )
        Comment.query.delete ( )

    def test_check_instance_variables(self):
            self.assertEquals ( self.new_pitch.users_id , 12345 )

    def test_save_pitch(self):
        self.new_pitch.save_pitch ( )
        self.assertTrue ( len ( Pitch.query.all ( ) ) > 0 )

