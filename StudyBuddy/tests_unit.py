import django
from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from StudyBuddy.models import TeacherForm as TeacherExtra, StudentForm as StudentExtra
from .models import Article, StudentClassroom, Classroom, Subject, ClassSubject
from .models import Exercise, Subject_Exam, Subject_Exercise, Student_Exercises
from .models import Private_Chat, Class_Chat
from .forms import ArticleForm
from datetime import datetime

# _____ UTILITY FUNCTIONS _____


def positive_test_result(test):
    """
        Returns Success for True and Failure for False

        Args:
            test (boolean): test result

        Returns:
            String: Success or Failure
    """
    if test:
        return "Success"
    else:
        return "Failure"


def negative_test_result(test):
    """
        Returns Success for False and Failure for True

        Args:
            test (boolean): test result

        Returns:
            String: Success or Failure
    """
    if not test:
        return "Success"
    else:
        return "Failure"


# _____ UNIT TESTS _____

# Login tests
class LoginTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for login functions

        Args:
    """

    @classmethod
    def setUpClass(cls):
        """
            Creating a user which can be used in all the functions
            and printing the testing class start
        """
        super(LoginTest, cls).setUpClass()
        print("\n__Login SetUp__")
        print("Module - result")
        cls.user = get_user_model().objects.create_user(username='admin', password='admin')
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the user after the class finishes all its functions
            and printing the testing class end
        """
        super(LoginTest, cls).tearDownClass()
        print("\n__Login TearDown__")
        cls.user.delete()

    # unit tests

    def test_unit_correct(self, username='admin', password='admin'):
        """
            Testing the correct username and password input

            Args:
                username (String): username input which is set as admin by default
                password (String): password input which is set as admin by default

            Returns:
                Boolean: True or False
        """
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertTrue(test)
        print("\nCorrect Login Unit Test - ", positive_test_result(test))
        return test

    def test_unit_wrong_username(self, username='wrong', password='admin'):
        """
            Testing the incorrect username input and correct password input

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as admin by default

            Returns:
                Boolean: True or False
        """
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Username Login Unit Test - ", negative_test_result(test))
        return test

    def test_unit_wrong_password(self, username='admin', password='wrong'):
        """
            Testing the correct username input and incorrect password input

            Args:
                username (String): username input which is set as admin by default
                password (String): password input which is set as wrong by default

            Returns:
                Boolean: True or False
        """
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Password Login Unit Test - ", negative_test_result(test))
        return test

    def test_unit_wrong_input(self, username='wrong', password='wrong'):
        """
            Testing the incorrect username input password input

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as wrong by default

            Returns:
                Boolean: True or False
        """
        user = authenticate(username=username, password=password)
        test = user is not None and user.is_authenticated
        self.assertFalse(test)
        print("\nWrong Input Login Unit Test - ", negative_test_result(test))
        return test

# Login tests


# Delete Teacher  tests
class DeleteTeacherTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for deleting teacher user
    """
    @classmethod
    def setUpClass(cls):
        """
            Printing the testing class start
        """
        super(DeleteTeacherTest, cls).setUpClass()
        print("\n__Delete Teacher SetUp__")
        print("Module - result")

    @classmethod
    def tearDownClass(cls):
        """
            Printing the testing class end
        """
        super(DeleteTeacherTest, cls).tearDownClass()
        print("\n__Delete Teacher TearDown__")

    # unit test

    def test_unit_delete_teacher_details(self):
        """
            Delete teacher user testing function

            Returns:
                Boolean: True or False
        """
        self.teacher = get_user_model().objects.create_user(username='teacher', password='teacher',
                                                            email='teacher@teach.er', first_name='tea',
                                                            last_name='cher')
        self.teacher.save()
        if self.teacher is not None:
            self.teacher.delete()
            self.teacher = None
        test = self.teacher is None

        self.assertTrue(test)
        print("\nCorrect Delete Teacher Unit Test - ", positive_test_result(test))
# Delete Teacher tests


# Update Teacher Details tests
class UpdateTeacherDetailsTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for updating teacher user information
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating a teacher user which can be used in all the functions
            and printing the testing class start
        """
        super(UpdateTeacherDetailsTest, cls).setUpClass()
        print("\n__Update Teacher Details SetUp__")
        print("Module - result")
        cls.teacher = get_user_model().objects.create_user(username='teacher', password='teacher',
                                                           email='teacher@teach.er', first_name='tea',
                                                           last_name='cher')
        cls.teacher.save()

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the teacher user after the class finishes
            and printing the testing class end
        """
        super(UpdateTeacherDetailsTest, cls).tearDownClass()
        print("\n__Update Teacher Details TearDown__")
        cls.teacher.delete()

    # unit test

    def test_unit_update_teacher_details(self, username='notTeacher', password='notTeacher',
                                         email='notTeacher@teach.er', first_name='not', last_name='teacher'):
        """
            Update teacher user information testing function

            Args:
                username (String): username input which is set as notTeacher by default
                password (String): password input which is set as notTeacher by default
                email (String): email input which is set as notTeacher@teach.er by default
                first_name (String): first name input which is set as not by default
                last_name (String): last name input which is set as teacher by default

            Returns:
                Boolean: True or False
        """
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
# Update Teacher Details tests


# View Teacher Details tests
class ViewTeacherDetailsTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for viewing teacher user information
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating a teacher user which can be used in all the functions
            and printing the testing class start
        """
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
        """
            Deleting the teacher user after the class finishes all its functions
            and printing the testing class end
        """
        super(ViewTeacherDetailsTest, cls).tearDownClass()
        print("\n__View Teacher Details TearDown__")
        cls.teacher.delete()

    # unit test

    def test_unit_view_teacher_details(self, username='teacher', password='teacher', email='teacher@teach.er',
                                       first_name='tea', last_name='cher'):
        """
            View teacher user information testing function

            Args:
                username (String): username input which is set as teacher by default
                password (String): password input which is set as teacher by default
                email (String): email input which is set as teacher@teach.er by default
                first_name (String): first name input which is set as tea by default
                last_name (String): last name input which is set as cher by default

            Returns:
                Boolean: True or False
        """
        test = (self.teacher.username == self.user_dict['username'] and self.teacher.email == self.user_dict['email']
                and self.teacher.first_name == self.user_dict['first_name']
                and self.teacher.last_name == self.user_dict['last_name'])

        self.assertTrue(test)
        print("\nCorrect View Teacher Details Unit Test - ", positive_test_result(test))
# View Teacher Details tests


# Delete Student  tests
class DeleteStudentTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for deleting student user information
    """
    @classmethod
    def setUpClass(cls):
        """
            Printing the testing class start
        """
        super(DeleteStudentTest, cls).setUpClass()
        print("\n__Delete Student SetUp__")
        print("Module - result")

    @classmethod
    def tearDownClass(cls):
        """
            Printing the testing class end
        """
        super(DeleteStudentTest, cls).tearDownClass()
        print("\n__Delete Student TearDown__")

    # unit test

    def test_unit_delete_teacher_details(self):
        """
            Delete teacher user information testing function

            Returns:
                Boolean: True or False
        """
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
# Delete Student tests


# Update Student Details tests
class UpdateStudentDetailsTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for updating student user information
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating a student user which can be used in all the functions
            and printing the testing class start
        """
        super(UpdateStudentDetailsTest, cls).setUpClass()
        print("\n__Update Student Details SetUp__")
        print("Module - result")
        cls.student = get_user_model().objects.create_user(username='student', password='student',
                                                           email='student@stude.nt', first_name='stud', last_name='ent')
        cls.student.save()

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the student user after the class finishes
            and printing the testing class end
        """
        super(UpdateStudentDetailsTest, cls).tearDownClass()
        print("\n__Update Student Details TearDown__")
        cls.student.delete()

    # unit test

    def test_unit_update_student_details(self, username='notStudent', password='notStudent',
                                         email='notStudent@stude.nt', first_name='not', last_name='student'):
        """
            Update student user information testing function

            Args:
                username (String): username input which is set as notStudent by default
                password (String): password input which is set as notStudent by default
                email (String): email input which is set as notStudent@stude.nt by default
                first_name (String): first name input which is set as not by default
                last_name (String): last name input which is set as student by default

            Returns:
                Boolean: True or False
        """
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
# Update Student Details tests


# View Student Details tests
class ViewStudentDetailsTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for viewing student user information
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating a student user which can be used in all the functions
            and printing the testing class start
        """
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
        """
            Deleting the student user after the class finishes
            and printing the testing class end
        """
        super(ViewStudentDetailsTest, cls).tearDownClass()
        print("\n__View Student Details TearDown__")
        cls.student.delete()

    # unit test

    def test_unit_view_student_details(self, username='student', password='student', email='student@stude.nt',
                                       first_name='stud', last_name='ent'):
        """
            View student user information testing function

            Args:
                username (String): username input which is set as student by default
                password (String): password input which is set as student by default
                email (String): email input which is set as student@stude.nt by default
                first_name (String): first name input which is set as stud by default
                last_name (String): last name input which is set as ent by default

            Returns:
                Boolean: True or False
        """
        test = (self.student.username == self.user_dict['username'] and self.student.email == self.user_dict['email']
                and self.student.first_name == self.user_dict['first_name']
                and self.student.last_name == self.user_dict['last_name'])

        self.assertTrue(test)
        print("\nCorrect View Student Details Unit Test - ", positive_test_result(test))
# View Student Details tests


# Teacher Registration test
class TeacherRegistrationTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for registering teacher user information
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating a teacher user which can be used in all the functions
            and printing the testing class start
        """
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

        cls.teacher_user = get_user_model().objects.create_user(username=cls.teacher.username,
                                                                password=cls.teacher.password1, email=cls.teacher.email,
                                                                first_name=cls.teacher.first_name,
                                                                last_name=cls.teacher.last_name)
        cls.teacher_user.is_superuser = False
        cls.teacher_user.is_staff = True
        cls.teacher_user.save()

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the teacher user after the class finishes
            and printing the testing class end
        """
        super(TeacherRegistrationTest, cls).tearDownClass()
        print("\n__Teacher Registration TearDown__")
        cls.teacher_user.delete()

    # unit tests

    def test_unit_correct_teacher_creation(self, username='teacher', password='teacher', email='teacher@teach.er'):
        """
            Create teacher user information testing function with correct input

            Args:
                username (String): username input which is set as teacher by default
                password (String): password input which is set as teacher by default
                email (String): email input which is set as teacher@teach.er by default

            Returns:
                Boolean: True or False
        """
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
        """
            Create teacher user information testing function with incorrect username input

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as teacher by default
                email (String): email input which is set as teacher@teach.er by default

            Returns:
                Boolean: True or False
        """
        user = get_user_model().objects.get(username='teacher')
        test_registration = False
        if user is not None:
            test_registration = (self.teacher_user.username == username
                                 and self.teacher_user.password == password
                                 and self.teacher_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Username Teacher Registration + Login Unit Test - ", negative_test_result(test_registration))

    def test_unit_wrong_password_teacher_creation(self, username='teacher', password='wrong', email='teacher@teach.er'):
        """
            Create teacher user information testing function with incorrect password input

            Args:
                username (String): username input which is set as teacher by default
                password (String): password input which is set as wrong by default
                email (String): email input which is set as teacher@teach.er by default

            Returns:
                Boolean: True or False
        """
        user = get_user_model().objects.get(username='teacher')
        test_registration = False
        if user is not None:
            test_registration = (self.teacher_user.username == username
                                 and self.teacher_user.password == password
                                 and self.teacher_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Password Teacher Registration + Login Unit Test - ", negative_test_result(test_registration))

    def test_unit_wrong_input_teacher_creation(self, username='wrong', password='wrong', email='teacher@teach.er'):
        """
            Create teacher user information testing function with incorrect username and password inputs

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as wrong by default
                email (String): email input which is set as teacher@teach.er by default

            Returns:
                Boolean: True or False
        """
        user = get_user_model().objects.get(username='teacher')
        test_registration = False
        if user is not None:
            test_registration = (self.teacher_user.username == username
                                 and self.teacher_user.password == password
                                 and self.teacher_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Password Teacher Registration + Login Unit Test - ", negative_test_result(test_registration))
# Teacher Registration test


# Student Registration test
class StudentRegistrationTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for registering student user information
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating a student user which can be used in all the functions
            and printing the testing class start
        """
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
        """
            Deleting the student user after the class finishes
            and printing the testing class end
        """
        super(StudentRegistrationTest, cls).tearDownClass()
        print("\n__Student Registration TearDown__")
        cls.student.delete()

    # unit tests

    def test_unit_correct_student_creation(self, username='student', password='student', email='student@stude.nt'):
        """
            Create teacher user information testing function with correct input

            Args:
                username (String): username input which is set as student by default
                password (String): password input which is set as student by default
                email (String): email input which is set as student@stude.nt by default

            Returns:
                Boolean: True or False
        """
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

    def test_unit_wrong_username_student_creation(self, username='wrong', password='student', email='student@stude.nt'):
        """
            Create teacher user information testing function with incorrect username input

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as student by default
                email (String): email input which is set as student@stude.nt by default

            Returns:
                Boolean: True or False
        """
        user = get_user_model().objects.get(username='student')
        test_registration = False
        if user is not None:
            test_registration = (self.student_user.username == username
                                 and self.student_user.password == password
                                 and self.student_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Username Student Registration + Login Unit Test - ", negative_test_result(test_registration))

    def test_unit_wrong_password_teacher_creation(self, username='student', password='wrong', email='student@stude.nt'):
        """
            Create teacher user information testing function with incorrect password input

            Args:
                username (String): username input which is set as student by default
                password (String): password input which is set as wrong by default
                email (String): email input which is set as student@stude.nt by default

            Returns:
                Boolean: True or False
        """
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
        """
            Create student user information testing function with incorrect username and password inputs

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as wrong by default
                email (String): email input which is set as student@stude.nt by default

            Returns:
                Boolean: True or False
        """
        user = get_user_model().objects.get(username='student')
        test_registration = False
        if user is not None:
            test_registration = (self.student_user.username == username
                                 and self.student_user.password == password
                                 and self.student_user.email == email)
        self.assertFalse(test_registration)
        print("\nWrong Password Student Registration + Login Unit Test - ", negative_test_result(test_registration))
# Student Registration test


# News test
class NewsTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for creating, viewing and deleting news
    """
    news_dict = {
        'title': 'news',
        'body': 'testing our news section',
        'date': '2021-05-05 18:33:00',
    }

    @classmethod
    def setUpClass(cls):
        """
            Creating news article which can be used in all the functions
            and printing the testing class start
        """
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
        """
             Deleting the news article after the class finishes
             and printing the testing class end
        """
        super(NewsTest, cls).tearDownClass()
        print("\n__News TearDown__")
        cls.user.delete()

    # unit tests

    def test_unit_news_creation(self):
        """
            Create news article testing function

            Returns:
                Boolean: True or False
        """
        self.news.title = self.news_dict['title']
        self.news.body = self.news_dict['body']
        self.news.date = self.news_dict['date']
        test = (self.news.title == self.news_dict['title'] and self.news.body == self.news_dict['body']
                and self.news.date == self.news_dict['date'])
        self.assertTrue(test)
        print("\nCorrect News Creation Unit Test - ", positive_test_result(test))

    def test_unit_view_news(self):
        """
            View news article testing function

            Returns:
                Boolean: True or False
        """
        test = (self.news.title == self.news_dict['title'] and self.news.body == self.news_dict['body']
                and self.news.date == self.news_dict['date'])
        self.assertTrue(test)
        print("\nView News Unit Test - ", positive_test_result(test))

    def test_unit_delete_news(self):
        """
            Delete news article testing function

            Returns:
                Boolean: True or False
        """
        self.news.title = None
        self.news.body = None
        self.news.date = None
        if self.news.title is None and self.news.body is None and self.news.date is None:
            self.news = None
        test = self.news is None
        self.assertTrue(test)
        print("\nDelete News Unit Test - ", positive_test_result(test))
# News test


# Classroom test
class ClassroomTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for creating class room
    """

    @classmethod
    def setUpClass(cls):
        """
            Creating teacher user and class room which can be used in all the functions
            and printing the testing class start
        """
        super(ClassroomTest, cls).setUpClass()
        print("\n__Classroom SetUp__")
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

        cls.teacher_user = get_user_model().objects.create_user(username=cls.teacher.username,
                                                                password=cls.teacher.password1, email=cls.teacher.email,
                                                                first_name=cls.teacher.first_name,
                                                                last_name=cls.teacher.last_name)
        cls.teacher_user.is_superuser = False
        cls.teacher_user.is_staff = True
        cls.teacher_user.save()

        cls.classroom = Classroom()
        cls.classroom.classname = 'class1'
        cls.classroom.teacher = cls.teacher_user
        cls.classroom.save()

    @classmethod
    def tearDownClass(cls):
        """
             Deleting the teacher user and the class room after the class finishes
             and printing the testing class end
        """
        super(ClassroomTest, cls).tearDownClass()
        print("\n__Classroom TearDown__")
        cls.classroom.delete()
        cls.teacher_user.delete()

    # unit tests

    def test_unit_classroom(self):
        """
            Create class room testing function

            Returns:
                Boolean: True or False
        """
        try:
            test_classroom = Classroom.objects.get(teacher=self.teacher_user.id)
            test = (self.classroom.teacher.id == test_classroom.teacher_id)
        except:
            test = False
        self.assertTrue(test)
        print("\nClassroom Unit Test - ", positive_test_result(test))

    def test_unit_clashes(self):
        """
            Check if 2 different class rooms cant have the same teacher

            Returns:
                Boolean: True or False
        """
        try:
            self.classroom1 = Classroom()
            self.classroom1.class_name = 'class1'
            self.classroom1.teacher = self.teacher_user
            self.classroom1.save()
            test = False
        except django.db.utils.IntegrityError:
            test = True
        self.assertTrue(test)
        print("\nClassroom Unit Test - ", positive_test_result(test))
# Classroom test


# Subject test
class SubjectTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for creating Subject
    """

    @classmethod
    def setUpClass(cls):
        """
            Creating teacher user and subject which can be used in all the functions
            and printing the testing class start
        """
        super(SubjectTest, cls).setUpClass()
        print("\n__Subject SetUp__")
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

        cls.teacher_user = get_user_model().objects.create_user(username=cls.teacher.username,
                                                                password=cls.teacher.password1, email=cls.teacher.email,
                                                                first_name=cls.teacher.first_name,
                                                                last_name=cls.teacher.last_name)
        cls.teacher_user.is_superuser = False
        cls.teacher_user.is_staff = True
        cls.teacher_user.save()

        cls.subject = Subject()
        cls.subject.classname = 'Math'
        cls.subject.teacher = cls.teacher_user
        cls.subject.duration = 2
        cls.subject.save()

    @classmethod
    def tearDownClass(cls):
        """
             Deleting the teacher user and the subject after the class finishes
             and printing the testing class end
        """
        super(SubjectTest, cls).tearDownClass()
        print("\n__Subject TearDown__")
        cls.subject.delete()
        cls.teacher_user.delete()

    # unit tests

    def test_unit_subject(self):
        """
            Create subject testing function

            Returns:
                Boolean: True or False
        """
        test = (self.subject.teacher.id == self.teacher_user.id)
        self.assertTrue(test)
        print("\nSubject Unit Test - ", positive_test_result(test))

    def test_unit_clashes(self):
        """
            Check if 2 different class rooms cant have the same teacher

            Returns:
                Boolean: True or False
        """
        try:
            self.subject1 = Subject()
            self.subject1.subject_name = self.subject.subject_name
            self.subject1.teacher = self.teacher_user
            self.subject1.duration = self.subject1.duration
            self.subject1.save()
            test = False
        except django.db.utils.IntegrityError:
            test = True
        self.assertTrue(test)
        print("\nClassroom Unit Test - ", positive_test_result(test))
# Subject test


# ClassSubject test
class ClassSubjectTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for combining class room and subject
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating teacher user, class room and subject which can be used in all the functions
            and printing the testing class start
        """
        super(ClassSubjectTest, cls).setUpClass()
        print("\n__Subject SetUp__")
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

        cls.teacher_user = get_user_model().objects.create_user(username=cls.teacher.username,
                                                                password=cls.teacher.password1, email=cls.teacher.email,
                                                                first_name=cls.teacher.first_name,
                                                                last_name=cls.teacher.last_name)
        cls.teacher_user.is_superuser = False
        cls.teacher_user.is_staff = True
        cls.teacher_user.save()

        cls.subject = Subject()
        cls.subject.subject_name = 'Math'
        cls.subject.teacher = cls.teacher_user
        cls.subject.duration = 2
        cls.subject.save()

        cls.classroom = Classroom()
        cls.classroom.class_name = 'class1'
        cls.classroom.teacher = cls.teacher_user
        cls.classroom.save()

        cls.class_subject = ClassSubject()
        cls.class_subject.subject = cls.subject
        cls.class_subject.class_room = cls.classroom
        cls.class_subject.days = 'Sunday'
        cls.class_subject.start_time = '08:00'
        cls.class_subject.end_time = '10:00'
        cls.class_subject.meeting = None
        cls.class_subject.save()

    @classmethod
    def tearDownClass(cls):
        """
             Deleting the teacher user, class room and the subject after the class finishes
             and printing the testing class end
        """
        super(ClassSubjectTest, cls).tearDownClass()
        print("\n__Subject TearDown__")
        cls.class_subject.delete()
        cls.subject.delete()
        cls.teacher_user.delete()

    # unit tests

    def test_unit_classSubject(self):
        """
            Create classSubject testing function

            Returns:
                Boolean: True or False
        """
        class_subject = ClassSubject.objects.get(id=1)
        test = (self.class_subject.subject.teacher.id == class_subject.subject.teacher.id
                and self.class_subject.subject.subject_name == class_subject.subject.subject_name
                and self.class_subject.class_room.class_name == class_subject.class_room.class_name)
        self.assertTrue(test)
        print("\nSubject Unit Test - ", positive_test_result(test))

    def test_unit_clashes(self):
        """
            Check if different classSubjects cant have 2 different subjects with same teacher
            or 2 different class rooms with same teacher

            Returns:
                Boolean: True or False
        """
        try:
            class_subject = ClassSubject.objects.get(id=1)

            self.class_subject1 = ClassSubject()
            self.class_subject1.subject = self.subject
            self.class_subject1.class_room = self.classroom
            self.class_subject1.days = class_subject.days
            self.class_subject1.start_time = class_subject.start_time
            self.class_subject1.end_time = class_subject.end_time
            self.class_subject1.meeting = None
            self.class_subject1.save()
            test = False
        except django.db.utils.IntegrityError:
            test = True

        self.assertTrue(test)
        print("\nSubject Unit Test - ", positive_test_result(test))
# ClassSubject test


# Exercise test
class ExerciseTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for combining class room and subject
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating exercise which can be used in all the functions
            and printing the testing class start
        """
        super(ExerciseTest, cls).setUpClass()
        print("\n__Exercise SetUp__")
        print("Module - result")
        cls.exercise = Exercise()
        cls.exercise.question = 'is it working?'
        cls.exercise.a = 'yes'
        cls.exercise.b = 'no'
        cls.exercise.c = 'i dont know'
        cls.exercise.d = 'maybe'
        cls.exercise.ans = 'a'
        cls.exercise.save()


    @classmethod
    def tearDownClass(cls):
        """
             Deleting the exercise and the subject after the class finishes
             and printing the testing class end
        """
        super(ExerciseTest, cls).tearDownClass()
        print("\n__Exercise TearDown__")
        cls.exercise.delete()

    # unit tests

    def test_unit_exercise(self):
        """
            Create Exercise testing function

            Returns:
                Boolean: True or False
        """
        exercise = Exercise.objects.get(id=1)
        test = (self.exercise.question == exercise.question and self.exercise.a == exercise.a
                and self.exercise.b == exercise.b and self.exercise.c == exercise.c
                and self.exercise.d == exercise.d and self.exercise.ans == exercise.ans)
        self.assertTrue(test)
        print("\nExercise Unit Test - ", positive_test_result(test))

    def test_unit_clashes(self):
        """
            Check if different exercises can be created with same fields

            Returns:
                Boolean: True or False
        """
        exercise = Exercise.objects.get(id=1)
        try:
            self.exercise1 = Exercise()
            self.exercise1.question = exercise.question
            self.exercise1.a = exercise.a
            self.exercise1.b = exercise.b
            self.exercise1.c = exercise.c
            self.exercise1.d = exercise.d
            self.exercise1.ans = exercise.ans
            self.exercise1.save()
            test = True
        except django.db.utils.IntegrityError:
            test = False
        self.assertTrue(test)
        print("\nExercise Unit Test - ", positive_test_result(test))
# Exercise test

