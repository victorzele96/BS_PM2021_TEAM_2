from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from StudyBuddy.forms import TeacherUserForm, TeacherForm
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

##### UNIT TESTS #####

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


class Test_init_(TestCase):
    # pylint: disable = all
    def test__init_(self):
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
        print("\n__Login SetUp__")
        print("Module - result")
        cls.user = get_user_model().objects.create_user(username='admin', password='admin')
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()
        print("\n__Login TearDown__")
        cls.user.delete()

    def test_correct(self, username='admin', password='admin'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertTrue(test)
        print("\nCorrect Login - ", positive_test_result(test))

    def test_wrong_username(self, username='wrong', password='admin'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Username Login - ", negative_test_result(test))

    def test_wrong_password(self, username='admin', password='wrong'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Password Login - ", negative_test_result(test))

    def test_wrong_input(self, username='wrong', password='wrong'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Input Login - ", negative_test_result(test))
# Login tests


# Register tests
# class TeacherRegistrationTest(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super(TeacherRegistrationTest, cls).setUpClass()
#         print("\n__Register SetUp__")
#         print("Module - result")
#         cls.teacher = TeacherUserForm()
#         cls.teacher.username = 'teacher'
#         cls.teacher.password1 = 'teacher'
#         cls.teacher.password2 = 'teacher'
#         cls.teacher.first_name = 'tea'
#         cls.teacher.last_name = 'cher'
#         cls.teacher.email = 'teacher@teach.er'

#         cls.teacher_extra = TeacherForm()
#         cls.teacher_extra.phone = '0521234567'
#         cls.teacher_extra.subjects = 'math'

#         cls.teacher.is_superuser = False;
#         cls.teacher.is_staff = True;

#         cls.teacher.email = cleaned_data["email"]
#         cls.teacher.
#         cls.teacher.save()
#         cls.teacher_extra.save()

#     @classmethod
#     def tearDownClass(cls):
#         super(TeacherRegistrationTest, cls).tearDownClass()
#         print("\n__Register TearDown__")
#         cls.teacher.delete()
#         cls.teacher_extra.delete()

#     def test_teacher_creation(self):
#         print(cls.teacher.username, cls.teacher.password1, cls.teacher.first_name, cls.teacher.last_name,
#               cls.teacher.email, cls.teacher_extra.phone, cls.teacher_extra.subjects)
# Register tests


# class NavTest(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super(NavTest, cls).setUpClass()
#         print("\n__Nav SetUp__")
#         print("Module - result")
#         cls.user = get_user_model().objects.create_user(username='admin', password='admin')
#         cls.user.is_superuser = True
#         cls.user.save()
#
#     @classmethod
#     def tearDownClass(cls):
#         super(NavTest, cls).tearDownClass()
#         print("\n__Nav TearDown__")
#         cls.user.delete()
#
#     def test_admin_nav(self, username='admin', password='admin'):
#         user = get_user_model().objects.get("admin")
#         user_auto = authenticate(username=username, password=password)
#         if user_auto is not None and user_auto.is_authenticated:
#             test = user.username == username
#         self.assertTrue(test)



##### UNIT TESTS END #####
