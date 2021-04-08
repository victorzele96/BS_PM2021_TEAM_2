from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase


# Login tests
class LoginTest(TestCase):

    def setUp(self):
        print("\n___Login SetUp___")
        self.user = get_user_model().objects.create_user(username='admin', password='admin')
        self.user.save()

    def tearDown(self):
        print("___Login TearDown___\n")
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='admin', password='admin')
        test = user is not None and user.is_authenticated
        self.assertTrue(test)
        print("Correct Login - ", test)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='admin')
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("Wrong Username Login - ", test)

    def test_wrong_password(self):
        user = authenticate(username='admin', password='wrong')
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("Wrong Password Login - ", test)
# Login tests

# Register tests


# Register tests


