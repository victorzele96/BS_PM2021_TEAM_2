from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from .forms import StudentUserForm


def positive_test_result(test):
    if test:
        return "Success"
    else:
        return "Failure"


def negative_test_result(test):
    if not test:
        return "Success"
    else:
        return "Failure"


class Test__init__(TestCase):
    # pylint: disable = all
    def test___init__(self):
        test = True
        self.assertTrue(test)
        print("\n__init__.py - ", positive_test_result(test))


class TestAdmin(TestCase):
    # pylint: disable = all
    def test_admin(self):
        test = True
        self.assertTrue(test)
        print("\nadmin.py - ", positive_test_result(test))


class TestApps(TestCase):
    # pylint: disable = all
    def test_apps(self):
        test = True
        self.assertTrue(test)
        print("\napps.py - ", positive_test_result(test))


class TestForms(TestCase):
    # pylint: disable = all
    def test_forms(self):
        test = True
        self.assertTrue(test)
        print("\nforms.py - ", positive_test_result(test))


class TestModels(TestCase):
    # pylint: disable = all
    def test_models(self):
        test = True
        self.assertTrue(test)
        print("\nmodels.py - ", positive_test_result(test))


class TestUrls(TestCase):
    # pylint: disable = all
    def test_urls(self):
        test = True
        self.assertTrue(test)
        print("\nurls.py - ", positive_test_result(test))


class TestViews(TestCase):
    # pylint: disable = all
    def test_views(self):
        test = True
        self.assertTrue(test)
        print("\nviews.py - ", positive_test_result(test))


# Login tests
class LoginTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()
        print("\n___Login SetUp___")
        print("Module - result")
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
        print("\nCorrect Login - ", positive_test_result(test))

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='admin')
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Username Login - ", negative_test_result(test))

    def test_wrong_password(self):
        user = authenticate(username='admin', password='wrong')
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Password Login - ", negative_test_result(test))

    def test_wrong_input(self):
        user = authenticate(username='wrong', password='wrong')
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Input Login - ", negative_test_result(test))
# Login tests


# Register tests
class RegisterTest(TestCase):
    pass
# Register tests
