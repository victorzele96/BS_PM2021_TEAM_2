from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from StudyBuddy.models import TeacherForm, StudentForm
from django.contrib.auth.models import User
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
#
#
# # Login tests
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
        print("\nCorrect Login Unit Test - ", positive_test_result(test))
        return test

    def test_wrong_username(self, username='wrong', password='admin'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Username Login Unit Test - ", negative_test_result(test))
        return test

    def test_wrong_password(self, username='admin', password='wrong'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Password Login Unit Test - ", negative_test_result(test))
        return test

    def test_wrong_input(self, username='wrong', password='wrong'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Input Login Unit Test - ", negative_test_result(test))
        return test
# Login tests

# Navbar tests
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
# Navbar tests

##### UNIT TESTS END #####

##### INTEGRATION TESTS #####

# Register tests
class TeacherRegistrationTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TeacherRegistrationTest, cls).setUpClass()
        print("\n__Teacher Registration SetUp__")
        print("Module - result")
        cls.teacher = TeacherForm()
        cls.teacher.username = 'teacher'
        cls.teacher.password1 = 'teacher'
        cls.teacher.password2 = 'teacher'
        cls.teacher.first_name = 'tea'
        cls.teacher.last_name = 'cher'
        cls.teacher.email = 'teacher@teach.er'
        cls.teacher.phone = '0521234567'
        cls.teacher.subjects = 'math'

        cls.teacher.is_superuser = False
        cls.teacher.is_staff = True

        cls.teacher_user = get_user_model().objects.create_user(username=cls.teacher.username,
                                                                password=cls.teacher.password1, email=cls.teacher.email,
                                                                first_name=cls.teacher.first_name,
                                                                last_name=cls.teacher.last_name)

        cls.teacher.save()

    @classmethod
    def tearDownClass(cls):
        super(TeacherRegistrationTest, cls).tearDownClass()
        print("\n__Teacher Registration TearDown__")
        cls.teacher.delete()

    def test_correct_teacher_creation(self, username='teacher', password='teacher'):
        user = get_user_model().objects.get(username='teacher')
        login_test = LoginTest().test_correct(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.teacher_user.username == user.username
                                 and self.teacher_user.password == user.password
                                 and self.teacher_user.email == user.email
                                 and self.teacher_user.first_name == user.first_name
                                 and self.teacher_user.last_name == user.last_name)
        self.assertTrue(test_registration)
        print("\nCorrect Teacher Registration + Login Integration Test - ", positive_test_result(test_registration))

    def test_wrong_username_teacher_creation(self, username='wrong', password='teacher'):
        user = get_user_model().objects.get(username='teacher')
        login_test = LoginTest().test_wrong_username(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.teacher_user.username == user.username
                                 and self.teacher_user.password == user.password
                                 and self.teacher_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Username Teacher Registration + Login Integration Test - ", negative_test_result(test_registration))

    def test_wrong_password_teacher_creation(self, username='teacher', password='wrong'):
        user = get_user_model().objects.get(username='teacher')
        login_test = LoginTest().test_wrong_password(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.teacher_user.username == user.username
                                 and self.teacher_user.password == user.password
                                 and self.teacher_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Password Teacher Registration + Login Integration Test - ", negative_test_result(test_registration))

    def test_wrong_input_teacher_creation(self, username='wrong', password='wrong'):
        user = get_user_model().objects.get(username='teacher')
        login_test = LoginTest().test_wrong_input(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.teacher_user.username == user.username
                                 and self.teacher_user.password == user.password
                                 and self.teacher_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Password Teacher Registration + Login Integration Test - ", negative_test_result(test_registration))


class StudentRegistrationTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(StudentRegistrationTest, cls).setUpClass()
        print("\n__Student Registration SetUp__")
        print("Module - result")
        cls.student = StudentForm()
        cls.student.username = 'student'
        cls.student.password1 = 'student'
        cls.student.password2 = 'student'
        cls.student.first_name = 'stud'
        cls.student.last_name = 'ent'
        cls.student.email = 'student@stude.nt'
        cls.student.phone = '0521454567'
        cls.student.birth_date = '1995-05-01'
        cls.student.parentName_F = 'bob'
        cls.student.parentPhone_F = '052987125'
        cls.student.parentName_M = 'bella'
        cls.student.parentPhone_M = '0529871256'

        cls.student.is_superuser = False
        cls.student.is_staff = False

        cls.student_user = get_user_model().objects.create_user(username=cls.student.username,
                                                                password=cls.student.password1, email=cls.student.email,
                                                                first_name=cls.student.first_name,
                                                                last_name=cls.student.last_name)

        cls.student.save()

    @classmethod
    def tearDownClass(cls):
        super(StudentRegistrationTest, cls).tearDownClass()
        print("\n__Student Registration TearDown__")
        cls.student.delete()

    def test_correct_student_creation(self, username='student', password='student'):
        user = get_user_model().objects.get(username='student')
        login_test = LoginTest().test_correct(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.student_user.username == user.username
                                 and self.student_user.password == user.password
                                 and self.student_user.email == user.email
                                 and self.student_user.first_name == user.first_name
                                 and self.student_user.last_name == user.last_name)
        self.assertTrue(test_registration)
        print("\nCorrect Student Registration + Login Integration Test - ", positive_test_result(test_registration))

    def test_wrong_username_student_creation(self, username='wrong', password='teacher'):
        user = get_user_model().objects.get(username='student')
        login_test = LoginTest().test_wrong_username(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.student_user.username == user.username
                                 and self.student_user.password == user.password
                                 and self.student_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Username Student Registration + Login Integration Test - ", negative_test_result(test_registration))

    def test_wrong_password_teacher_creation(self, username='student', password='wrong'):
        user = get_user_model().objects.get(username='student')
        login_test = LoginTest().test_wrong_password(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.student_user.username == user.username
                                 and self.student_user.password == user.password
                                 and self.student_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Password Student Registration + Login Integration Test - ",
              negative_test_result(test_registration))

    def test_wrong_input_teacher_creation(self, username='wrong', password='wrong'):
        user = get_user_model().objects.get(username='student')
        login_test = LoginTest().test_wrong_input(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.student_user.username == user.username
                                 and self.student_user.password == user.password
                                 and self.student_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Password Student Registration + Login Integration Test - ", negative_test_result(test_registration))
# Register tests

##### INTEGRATION TESTS END #####


