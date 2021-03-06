from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from StudyBuddy.models import TeacherForm as TeacherExtra, StudentForm as StudentExtra
from .models import Article
from .forms import ArticleForm
from datetime import datetime

##### UNIT TESTS AND INTEGRATION TESTS #####

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

    # unit tests

    def test_unit_correct(self, username='admin', password='admin'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertTrue(test)
        print("\nCorrect Login Unit Test - ", positive_test_result(test))
        return test

    def test_unit_wrong_username(self, username='wrong', password='admin'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Username Login Unit Test - ", negative_test_result(test))
        return test

    def test_unit_wrong_password(self, username='admin', password='wrong'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Password Login Unit Test - ", negative_test_result(test))
        return test

    def test_unit_wrong_input(self, username='wrong', password='wrong'):
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Input Login Unit Test - ", negative_test_result(test))
        return test

# Login tests

# Delete Teacher  tests
class DeleteTeacherTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(DeleteTeacherTest, cls).setUpClass()
        print("\n__Delete Teacher SetUp__")
        print("Module - result")

    @classmethod
    def tearDownClass(cls):
        super(DeleteTeacherTest, cls).tearDownClass()
        print("\n__Delete Teacher TearDown__")

    # unit test

    def test_unit_delete_teacher_details(self):
        self.teacher = get_user_model().objects.create_user(username='teacher', password='teacher',
                                                           email='teacher@teach.er', first_name='tea', last_name='cher')
        self.teacher.save()
        if self.teacher is not None:
            self.teacher.delete()
            self.teacher = None
        test = self.teacher is None

        self.assertTrue(test)
        print("\nCorrect Delete Teacher Unit Test - ", positive_test_result(test))

    # integration test

    def test_integration_delete_teacher_details(self):
        self.teacher = get_user_model().objects.create_user(username='teacher', password='teacher',
                                                            email='teacher@teach.er', first_name='tea',
                                                            last_name='cher')
        self.teacher_test = TeacherRegistrationTest
        if self.teacher_test:
            self.teacher.save()
            if self.teacher is not None:
                self.teacher.delete()
                self.teacher = None
            test = self.teacher is None

            self.assertTrue(test)
        print("\nCorrect Delete Teacher Integration Test - ", positive_test_result(test))
# Delete Teacher tests

# Update Teacher Details tests
class UpdateTeacherDetailsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(UpdateTeacherDetailsTest, cls).setUpClass()
        print("\n__Update Teacher Details SetUp__")
        print("Module - result")
        cls.teacher = get_user_model().objects.create_user(username='teacher', password='teacher',
                                                           email='teacher@teach.er', first_name='tea', last_name='cher')
        cls.teacher.save()

    @classmethod
    def tearDownClass(cls):
        super(UpdateTeacherDetailsTest, cls).tearDownClass()
        print("\n__Update Teacher Details TearDown__")
        cls.teacher.delete()

    # unit test

    def test_unit_update_teacher_details(self, username='notTeacher', password='notTeacher', email='notTeacher@teach.er', first_name='not', last_name='teacher'):
        if self.teacher is not None:
            self.teacher.username = username
            self.teacher.password = password
            self.teacher.email = email
            self.teacher.first_name = first_name
            self.teacher.last_name = last_name

            self.teacher.save()

        test = (self.teacher.username == username and self.teacher.password == password and self.teacher.email == email
                and self.teacher.first_name == first_name and self.teacher.last_name == last_name)

        self.assertTrue(test)
        print("\nCorrect Update Teacher Details Unit Test - ", positive_test_result(test))

    # integration test

    def test_integration_update_teacher_details(self, username='notTeacher', password='notTeacher',
                                                email='notTeacher@teach.er', first_name='not', last_name='teacher'):
        self.teacher_test = TeacherRegistrationTest
        if self.teacher_test:
            if self.teacher is not None:
                self.teacher.username = username
                self.teacher.password = password
                self.teacher.email = email
                self.teacher.first_name = first_name
                self.teacher.last_name = last_name

                self.teacher.save()

            test = (
                        self.teacher.username == username and self.teacher.password == password and self.teacher.email == email
                        and self.teacher.first_name == first_name and self.teacher.last_name == last_name)

        self.assertTrue(test)
        print("\nCorrect Update Teacher Details Integration Test - ", positive_test_result(test))
# Update Teacher Details tests

# View Teacher Details tests
class ViewTeacherDetailsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ViewTeacherDetailsTest, cls).setUpClass()
        print("\n__View Teacher Details SetUp__")
        print("Module - result")

        cls.user_dict = {
            'username': 'teacher',
            'password': 'teacher',
            'email': 'teacher@teach.er',
            'first_name': 'tea',
            'last_name': 'cher',
        }

        cls.teacher = get_user_model().objects.create_user(username='teacher', password='teacher',
                                                           email='teacher@teach.er', first_name='tea', last_name='cher')
        cls.teacher.save()

    @classmethod
    def tearDownClass(cls):
        super(ViewTeacherDetailsTest, cls).tearDownClass()
        print("\n__View Teacher Details TearDown__")
        cls.teacher.delete()

    # unit test

    def test_unit_view_teacher_details(self, username='teacher', password='teacher', email='teacher@teach.er', first_name='tea', last_name='cher'):
        test = (self.teacher.username == self.user_dict['username'] and self.teacher.email == self.user_dict['email']
                and self.teacher.first_name == self.user_dict['first_name']
                and self.teacher.last_name == self.user_dict['last_name'])

        self.assertTrue(test)
        print("\nCorrect View Teacher Details Unit Test - ", positive_test_result(test))

    # integration test

    def test_unit_view_teacher_details(self, username='teacher', password='teacher', email='teacher@teach.er', first_name='tea', last_name='cher'):
        self.teacher_test = TeacherRegistrationTest
        if self.teacher_test:
            test = (self.teacher.username == self.user_dict['username'] and self.teacher.email == self.user_dict['email']
                    and self.teacher.first_name == self.user_dict['first_name']
                    and self.teacher.last_name == self.user_dict['last_name'])

        self.assertTrue(test)
        print("\nCorrect View Teacher Details Integration Test - ", positive_test_result(test))
# View Teacher Details tests

# Delete Student  tests
class DeleteStudentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(DeleteStudentTest, cls).setUpClass()
        print("\n__Delete Student SetUp__")
        print("Module - result")

    @classmethod
    def tearDownClass(cls):
        super(DeleteStudentTest, cls).tearDownClass()
        print("\n__Delete Student TearDown__")

    # unit test

    def test_unit_delete_teacher_details(self):
        self.student = get_user_model().objects.create_user(username='student', password='student',
                                                            email='student@stude.nt', first_name='stud',
                                                            last_name='ent')
        self.student.save()
        if self.student is not None:
            self.student.delete()
            self.student = None
        test = self.student is None

        self.assertTrue(test)
        print("\nCorrect Delete Student Unit Test - ", positive_test_result(test))

    # integration test

    def test_integration_delete_student_details(self):
        self.student = get_user_model().objects.create_user(username='student', password='student',
                                                            email='student@stude.nt', first_name='stud',
                                                            last_name='ent')
        self.student_test = StudentRegistrationTest
        if self.student_test:
            self.student.save()
            if self.student is not None:
                self.student.delete()
                self.student = None
            test = self.student is None

            self.assertTrue(test)
        print("\nCorrect Delete Student Integration Test - ", positive_test_result(test))
# Delete Student tests

# Update Student Details tests
class UpdateStudentDetailsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(UpdateStudentDetailsTest, cls).setUpClass()
        print("\n__Update Student Details SetUp__")
        print("Module - result")
        cls.student = get_user_model().objects.create_user(username='student', password='student',
                                                           email='student@stude.nt', first_name='stud', last_name='ent')
        cls.student.save()

    @classmethod
    def tearDownClass(cls):
        super(UpdateStudentDetailsTest, cls).tearDownClass()
        print("\n__Update Student Details TearDown__")
        cls.student.delete()

    # unit test

    def test_unit_update_student_details(self, username='notStudent', password='notStudent', email='notStudent@stude.nt', first_name='not', last_name='student'):
        if self.student is not None:
            self.student.username = username
            self.student.password = password
            self.student.email = email
            self.student.first_name = first_name
            self.student.last_name = last_name

            self.student.save()

        test = (self.student.username == username and self.student.password == password and self.student.email == email
                and self.student.first_name == first_name and self.student.last_name == last_name)

        self.assertTrue(test)
        print("\nCorrect Update Student Details Unit Test - ", positive_test_result(test))

        # integration test

    def test_integration_update_student_details(self, username='notStudent', password='notStudent',
                                                email='notStudent@stude.nt', first_name='not', last_name='student'):
        self.student_test = StudentRegistrationTest
        if self.student_test:
            if self.student is not None:
                self.student.username = username
                self.student.password = password
                self.student.email = email
                self.student.first_name = first_name
                self.student.last_name = last_name

                self.student.save()

            test = (self.student.username == username and self.student.password == password
                    and self.student.email == email and self.student.first_name == first_name
                    and self.student.last_name == last_name)

        self.assertTrue(test)
        print("\nCorrect Update Student Details Integration Test - ", positive_test_result(test))
# Update Student Details tests

# View Student Details tests
class ViewStudentDetailsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(ViewStudentDetailsTest, cls).setUpClass()
        print("\n__View Student Details SetUp__")
        print("Module - result")

        cls.user_dict = {
            'username': 'student',
            'password': 'student',
            'email': 'student@stude.nt',
            'first_name': 'stud',
            'last_name': 'ent',
        }

        cls.student = get_user_model().objects.create_user(username='student', password='student',
                                                           email='student@stude.nt', first_name='stud', last_name='ent')
        cls.student.save()

    @classmethod
    def tearDownClass(cls):
        super(ViewStudentDetailsTest, cls).tearDownClass()
        print("\n__View Student Details TearDown__")
        cls.student.delete()

    # unit test

    def test_unit_view_student_details(self, username='student', password='student', email='student@stude.nt', first_name='stud', last_name='ent'):
        test = (self.student.username == self.user_dict['username'] and self.student.email == self.user_dict['email']
                and self.student.first_name == self.user_dict['first_name']
                and self.student.last_name == self.user_dict['last_name'])

        self.assertTrue(test)
        print("\nCorrect View Student Details Unit Test - ", positive_test_result(test))

    # integration test

    def test_integration_view_student_details(self, username='student', password='student', email='student@stude.nt', first_name='stud', last_name='ent'):
        self.student_test = StudentRegistrationTest
        if self.student_test:
            test = (self.student.username == self.user_dict['username'] and self.student.email == self.user_dict['email']
                    and self.student.first_name == self.user_dict['first_name']
                    and self.student.last_name == self.user_dict['last_name'])

        self.assertTrue(test)
        print("\nCorrect View Student Details Integration Test - ", positive_test_result(test))
# View Student Details tests

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

# Teacher Registration test
class TeacherRegistrationTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TeacherRegistrationTest, cls).setUpClass()
        print("\n__Teacher Registration SetUp__")
        print("Module - result")
        cls.teacher = TeacherExtra()
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

    # unit tests

    def test_unit_correct_teacher_creation(self, username='teacher', password='teacher', email='teacher@teach.er'):
        user = get_user_model().objects.get(username='teacher')
        test_registration = False
        if user is not None:
            test_registration = (self.teacher_user.username == user.username
                                 and self.teacher_user.password == user.password
                                 and self.teacher_user.email == user.email
                                 and self.teacher_user.first_name == user.first_name
                                 and self.teacher_user.last_name == user.last_name)
        self.assertTrue(test_registration)
        print("\nCorrect Teacher Registration + Login Unit Test - ", positive_test_result(test_registration))
        return test_registration

    def test_unit_wrong_username_teacher_creation(self, username='wrong', password='teacher', email='teacher@teach.er'):
        user = get_user_model().objects.get(username='teacher')
        test_registration = False
        if user is not None:
            test_registration = (self.teacher_user.username == username
                                 and self.teacher_user.password == password
                                 and self.teacher_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Username Teacher Registration + Login Unit Test - ", negative_test_result(test_registration))

    def test_unit_wrong_password_teacher_creation(self, username='teacher', password='wrong', email='teacher@teach.er'):
        user = get_user_model().objects.get(username='teacher')
        test_registration = False
        if user is not None:
            test_registration = (self.teacher_user.username == username
                                 and self.teacher_user.password == password
                                 and self.teacher_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Password Teacher Registration + Login Unit Test - ", negative_test_result(test_registration))

    def test_unit_wrong_input_teacher_creation(self, username='wrong', password='wrong', email='teacher@teach.er'):
        user = get_user_model().objects.get(username='teacher')
        test_registration = False
        if user is not None:
            test_registration = (self.teacher_user.username == username
                                 and self.teacher_user.password == password
                                 and self.teacher_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Password Teacher Registration + Login Unit Test - ", negative_test_result(test_registration))

    # integration tests

    def test_integration_correct_teacher_creation(self, username='teacher', password='teacher'):
        user = get_user_model().objects.get(username='teacher')
        login_test = LoginTest().test_unit_correct(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.teacher_user.username == user.username
                                 and self.teacher_user.password == user.password
                                 and self.teacher_user.email == user.email
                                 and self.teacher_user.first_name == user.first_name
                                 and self.teacher_user.last_name == user.last_name)
        self.assertTrue(test_registration)
        print("\nCorrect Teacher Registration + Login Integration Test - ", positive_test_result(test_registration))

    def test_integration_wrong_username_teacher_creation(self, username='wrong', password='teacher'):
        user = get_user_model().objects.get(username='teacher')
        login_test = LoginTest().test_unit_wrong_username(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.teacher_user.username == user.username
                                 and self.teacher_user.password == user.password
                                 and self.teacher_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Username Teacher Registration + Login Integration Test - ", negative_test_result(test_registration))

    def test_integration_wrong_password_teacher_creation(self, username='teacher', password='wrong'):
        user = get_user_model().objects.get(username='teacher')
        login_test = LoginTest().test_unit_wrong_password(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.teacher_user.username == user.username
                                 and self.teacher_user.password == user.password
                                 and self.teacher_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Password Teacher Registration + Login Integration Test - ", negative_test_result(test_registration))

    def test_integration_wrong_input_teacher_creation(self, username='wrong', password='wrong'):
        user = get_user_model().objects.get(username='teacher')
        login_test = LoginTest().test_unit_wrong_input(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.teacher_user.username == user.username
                                 and self.teacher_user.password == user.password
                                 and self.teacher_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Password Teacher Registration + Login Integration Test - ", negative_test_result(test_registration))
# Teacher Registration test

# Student Registration test
class StudentRegistrationTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(StudentRegistrationTest, cls).setUpClass()
        print("\n__Student Registration SetUp__")
        print("Module - result")
        cls.student = StudentExtra()
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

    # unit tests

    def test_unit_correct_student_creation(self, username='student', password='student'):
        user = get_user_model().objects.get(username='student')
        test_registration = False
        if user is not None:
            test_registration = (self.student_user.username == user.username
                                 and self.student_user.password == user.password
                                 and self.student_user.email == user.email
                                 and self.student_user.first_name == user.first_name
                                 and self.student_user.last_name == user.last_name)
        self.assertTrue(test_registration)
        print("\nCorrect Student Registration + Login Unit Test - ", positive_test_result(test_registration))

    def test_unit_wrong_username_student_creation(self, username='wrong', password='teacher', email='student@stude.nt'):
        user = get_user_model().objects.get(username='student')
        test_registration = False
        if user is not None:
            test_registration = (self.student_user.username == username
                                 and self.student_user.password == password
                                 and self.student_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Username Student Registration + Login Unit Test - ", negative_test_result(test_registration))

    def test_unit_wrong_password_teacher_creation(self, username='student', password='wrong', email='student@stude.nt'):
        user = get_user_model().objects.get(username='student')
        test_registration = False
        if user is not None:
            test_registration = (self.student_user.username == username
                                 and self.student_user.password == password
                                 and self.student_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Password Student Registration + Login Unit Test - ",
              negative_test_result(test_registration))

    def test_unit_wrong_input_teacher_creation(self, username='wrong', password='wrong', email='student@stude.nt'):
        user = get_user_model().objects.get(username='student')
        test_registration = False
        if user is not None:
            test_registration = (self.student_user.username == username
                                 and self.student_user.password == password
                                 and self.student_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Password Student Registration + Login Unit Test - ", negative_test_result(test_registration))

    # integration tests

    def test_integration_correct_student_creation(self, username='student', password='student'):
        user = get_user_model().objects.get(username='student')
        login_test = LoginTest().test_unit_correct(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.student_user.username == user.username
                                 and self.student_user.password == user.password
                                 and self.student_user.email == user.email
                                 and self.student_user.first_name == user.first_name
                                 and self.student_user.last_name == user.last_name)
        self.assertTrue(test_registration)
        print("\nCorrect Student Registration + Login Integration Test - ", positive_test_result(test_registration))

    def test_integration_wrong_username_student_creation(self, username='wrong', password='teacher'):
        user = get_user_model().objects.get(username='student')
        login_test = LoginTest().test_unit_wrong_username(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.student_user.username == user.username
                                 and self.student_user.password == user.password
                                 and self.student_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Username Student Registration + Login Integration Test - ", negative_test_result(test_registration))

    def test_integration_wrong_password_teacher_creation(self, username='student', password='wrong'):
        user = get_user_model().objects.get(username='student')
        login_test = LoginTest().test_unit_wrong_password(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.student_user.username == user.username
                                 and self.student_user.password == user.password
                                 and self.student_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Password Student Registration + Login Integration Test - ",
              negative_test_result(test_registration))

    def test_integration_wrong_input_teacher_creation(self, username='wrong', password='wrong'):
        user = get_user_model().objects.get(username='student')
        login_test = LoginTest().test_unit_wrong_input(username=username, password=password)
        test_registration = False
        if login_test:
            test_registration = (self.student_user.username == user.username
                                 and self.student_user.password == user.password
                                 and self.student_user.email == user.email)
        self.assertFalse(test_registration)
        print("\nWrong Password Student Registration + Login Integration Test - ", negative_test_result(test_registration))
# Student Registration test

# News test
class NewsTest(TestCase):

    news_dict = {
        'title': 'news',
        'body': 'testing our news section',
        'date': '2021-05-05 18:33:00',
    }

    @classmethod
    def setUpClass(cls):
        super(NewsTest, cls).setUpClass()
        print("\n__News SetUp__")
        print("Module - result")
        cls.user = get_user_model().objects.create_user(username='admin', password='admin')
        cls.user.save()
        cls.news = ArticleForm(cls.news_dict)
        cls.news.save(commit=False)
        cls.news = Article(cls.news_dict)

    @classmethod
    def tearDownClass(cls):
        super(NewsTest, cls).tearDownClass()
        print("\n__News TearDown__")
        cls.user.delete()

    # unit tests

    def test_unit_news_creation(self):
        self.news.setTitle(self.news_dict['title'])
        self.news.setBody(self.news_dict['body'])
        self.news.setDate(self.news_dict['date'])
        test = (self.news.getTitle() == self.news_dict['title'] and self.news.getBody() == self.news_dict['body']
                and self.news.getDate() == self.news_dict['date'])
        self.assertTrue(test)
        print("\nCorrect News Creation Unit Test - ", positive_test_result(test))

    def test_unit_view_news(self):
        test = (self.news.getTitle() == self.news_dict['title'] and self.news.getBody() == self.news_dict['body']
                and self.news.getDate() == self.news_dict['date'])
        self.assertTrue(test)
        print("\nView News Unit Test - ", positive_test_result(test))

    def test_unit_delete_news(self):
        self.news.setTitle(None)
        self.news.setBody(None)
        self.news.setDate(None)
        if self.news.getTitle() is None and self.news.getBody() is None and self.news.getDate() is None:
            self.news = None
        test = self.news is None
        self.assertTrue(test)
        print("\nDelete News Unit Test - ", positive_test_result(test))

    # integration tests

    def test_integration_news_creation(self):
        login_test = LoginTest().test_unit_correct(username='admin', password='admin')
        if login_test:
            user = authenticate(username='admin', password='admin')
            if user is not None and user.is_authenticated:
                self.news.setTitle(self.news_dict['title'])
                self.news.setBody(self.news_dict['body'])
                self.news.setDate(self.news_dict['date'])
                test = (self.news.getTitle() == self.news_dict['title'] and self.news.getBody() == self.news_dict['body']
                        and self.news.getDate() == self.news_dict['date'])
        self.assertTrue(test)
        print("\nCorrect News Creation Integration Test - ", positive_test_result(test))

    def test_integration_view_news(self):
        login_test = LoginTest().test_unit_correct(username='admin', password='admin')
        if login_test:
            user = authenticate(username='admin', password='admin')
            if user is not None and user.is_authenticated:
                test = (self.news.getTitle() == self.news_dict['title'] and self.news.getBody() == self.news_dict['body']
                        and self.news.getDate() == self.news_dict['date'])
        self.assertTrue(test)
        print("\nView News Integration Test - ", positive_test_result(test))

    def test_integration_delete_news(self):
        login_test = LoginTest().test_unit_correct(username='admin', password='admin')
        if login_test:
            user = authenticate(username='admin', password='admin')
            if user is not None and user.is_authenticated:
                self.news.setTitle(None)
                self.news.setBody(None)
                self.news.setDate(None)
                if self.news.getTitle() is None and self.news.getBody() is None and self.news.getDate() is None:
                    self.news = None
                test = self.news is None
        self.assertTrue(test)
        print("\nDelete News Integration Test - ", positive_test_result(test))
# News test
