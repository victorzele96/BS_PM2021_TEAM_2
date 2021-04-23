from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase


# Login tests
class LoginTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()
        print("___Login SetUp___")
        cls.user = get_user_model().objects.create_user(username='admin', password='admin')
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()
        print("\n___Login TearDown___")
        cls.user.delete()

    def test_correct(self):
        user = authenticate(username='admin', password='admin')
        test = user is not None and user.is_authenticated
        self.assertTrue(test)
        print("\nCorrect Login - ", test)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='admin')
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Username Login - ", test)

    def test_wrong_password(self):
        user = authenticate(username='admin', password='wrong')
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Password Login - ", test)

    def test_wrong_input(self):
        user = authenticate(username='wrong', password='wrong')
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Input Login - ", test)
# Login tests


# Register tests
class RegisterTest(TestCase):

    pass
# Register tests
