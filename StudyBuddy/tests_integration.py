# from django.contrib.auth import authenticate, get_user_model
# from django.test import TestCase
# from StudyBuddy.models import TeacherForm as TeacherExtra, StudentForm as StudentExtra
# from StudyBuddy.models import Article
# from StudyBuddy.forms import ArticleForm
# from StudyBuddy.tests_unit import LoginTest, DeleteTeacherTest, DeleteStudentTest, TeacherRegistrationTest, \
#                                   StudentRegistrationTest, ViewTeacherDetailsTest, ViewStudentDetailsTest, \
#                                   UpdateStudentDetailsTest, UpdateTeacherDetailsTest, NewsTest
# from datetime import datetime
#
# # _____ UTILITY FUNCTIONS _____
#
#
# def positive_test_result(test):
#     """
#         Returns Success for True and Failure for False
#
#         Args:
#             test (boolean): test result
#
#         Returns:
#             String: Success or Failure
#     """
#     if test:
#         return "Success"
#     else:
#         return "Failure"
#
#
# def negative_test_result(test):
#     """
#         Returns Success for False and Failure for True
#
#         Args:
#             test (boolean): test result
#
#         Returns:
#             String: Success or Failure
#     """
#     if not test:
#         return "Success"
#     else:
#         return "Failure"
#
#
# # _____ INTEGRATION TESTS _____
#
# # Delete Teacher  tests
# class DeleteTeacherTest(TestCase):
#     """
#         Testing class (Inheriting TestCase class) for deleting teacher user
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#             Printing the testing class start
#         """
#         super(DeleteTeacherTest, cls).setUpClass()
#         print("\n__Delete Teacher SetUp__")
#         print("Module - result")
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#             Printing the testing class end
#         """
#         super(DeleteTeacherTest, cls).tearDownClass()
#         print("\n__Delete Teacher TearDown__")
#
#     # integration test
#
#     def test_integration_delete_teacher_details(self):
#         """
#             Delete teacher user testing function
#
#             Returns:
#                 Boolean: True or False
#         """
#         self.teacher = get_user_model().objects.create_user(username='teacher', password='teacher',
#                                                             email='teacher@teach.er', first_name='tea',
#                                                             last_name='cher')
#         self.teacher_test = TeacherRegistrationTest
#         if self.teacher_test:
#             self.teacher.save()
#             if self.teacher is not None:
#                 self.teacher.delete()
#                 self.teacher = None
#             test = self.teacher is None
#
#             self.assertTrue(test)
#         print("\nCorrect Delete Teacher Integration Test - ", positive_test_result(test))
# # Delete Teacher tests
#
#
# # Update Teacher Details tests
# class UpdateTeacherDetailsTest(TestCase):
#     """
#         Testing class (Inheriting TestCase class) for updating teacher user information
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#             Creating a teacher user which can be used in all the functions
#             and printing the testing class start
#         """
#         super(UpdateTeacherDetailsTest, cls).setUpClass()
#         print("\n__Update Teacher Details SetUp__")
#         print("Module - result")
#         cls.teacher = get_user_model().objects.create_user(username='teacher', password='teacher',
#                                                            email='teacher@teach.er', first_name='tea', last_name='cher')
#         cls.teacher.save()
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#             Deleting the teacher user after the class finishes
#             and printing the testing class end
#         """
#         super(UpdateTeacherDetailsTest, cls).tearDownClass()
#         print("\n__Update Teacher Details TearDown__")
#         cls.teacher.delete()
#
#     # integration test
#
#     def test_integration_update_teacher_details(self, username='notTeacher', password='notTeacher',
#                                                 email='notTeacher@teach.er', first_name='not', last_name='teacher'):
#         """
#             Update teacher user information testing function
#
#             Args:
#                 username (String): username input which is set as notTeacher by default
#                 password (String): password input which is set as notTeacher by default
#                 email (String): email input which is set as notTeacher@teach.er by default
#                 first_name (String): first name input which is set as not by default
#                 last_name (String): last name input which is set as teacher by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         self.teacher_test = TeacherRegistrationTest
#         if self.teacher_test:
#             if self.teacher is not None:
#                 self.teacher.username = username
#                 self.teacher.password = password
#                 self.teacher.email = email
#                 self.teacher.first_name = first_name
#                 self.teacher.last_name = last_name
#
#                 self.teacher.save()
#
#             test = (self.teacher.username == username and self.teacher.password == password
#                     and self.teacher.email == email and self.teacher.first_name == first_name and
#                     self.teacher.last_name == last_name)
#
#         self.assertTrue(test)
#         print("\nCorrect Update Teacher Details Integration Test - ", positive_test_result(test))
# # Update Teacher Details tests
#
#
# # View Teacher Details tests
# class ViewTeacherDetailsTest(TestCase):
#     """
#         Testing class (Inheriting TestCase class) for viewing teacher user information
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#             Creating a teacher user which can be used in all the functions
#             and printing the testing class start
#         """
#         super(ViewTeacherDetailsTest, cls).setUpClass()
#         print("\n__View Teacher Details SetUp__")
#         print("Module - result")
#
#         cls.user_dict = {
#             'username': 'teacher',
#             'password': 'teacher',
#             'email': 'teacher@teach.er',
#             'first_name': 'tea',
#             'last_name': 'cher',
#         }
#
#         cls.teacher = get_user_model().objects.create_user(username='teacher', password='teacher',
#                                                            email='teacher@teach.er', first_name='tea', last_name='cher')
#         cls.teacher.save()
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#             Deleting the teacher user after the class finishes all its functions
#             and printing the testing class end
#         """
#         super(ViewTeacherDetailsTest, cls).tearDownClass()
#         print("\n__View Teacher Details TearDown__")
#         cls.teacher.delete()
#
#     # integration test
#
#     def test_integration_view_teacher_details(self, username='teacher', password='teacher', email='teacher@teach.er',
#                                               first_name='tea', last_name='cher'):
#         """
#             View teacher user information testing function
#
#             Args:
#                 username (String): username input which is set as teacher by default
#                 password (String): password input which is set as teacher by default
#                 email (String): email input which is set as teacher@teach.er by default
#                 first_name (String): first name input which is set as tea by default
#                 last_name (String): last name input which is set as cher by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         self.teacher_test = TeacherRegistrationTest
#         if self.teacher_test:
#             test = (self.teacher.username == self.user_dict['username'] and self.teacher.email == self.user_dict['email']
#                     and self.teacher.first_name == self.user_dict['first_name']
#                     and self.teacher.last_name == self.user_dict['last_name'])
#
#         self.assertTrue(test)
#         print("\nCorrect View Teacher Details Integration Test - ", positive_test_result(test))
# # View Teacher Details tests
#
#
# # Delete Student  tests
# class DeleteStudentTest(TestCase):
#     """
#         Testing class (Inheriting TestCase class) for deleting student user information
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#             Printing the testing class start
#         """
#         super(DeleteStudentTest, cls).setUpClass()
#         print("\n__Delete Student SetUp__")
#         print("Module - result")
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#             Printing the testing class end
#         """
#         super(DeleteStudentTest, cls).tearDownClass()
#         print("\n__Delete Student TearDown__")
#
#     # integration test
#
#     def test_integration_delete_student_details(self):
#         """
#             Delete teacher user information testing function
#
#             Returns:
#                 Boolean: True or False
#         """
#         self.student = get_user_model().objects.create_user(username='student', password='student',
#                                                             email='student@stude.nt', first_name='stud',
#                                                             last_name='ent')
#         self.student_test = StudentRegistrationTest
#         if self.student_test:
#             self.student.save()
#             if self.student is not None:
#                 self.student.delete()
#                 self.student = None
#             test = self.student is None
#
#             self.assertTrue(test)
#         print("\nCorrect Delete Student Integration Test - ", positive_test_result(test))
# # Delete Student tests
#
#
# # Update Student Details tests
# class UpdateStudentDetailsTest(TestCase):
#     """
#         Testing class (Inheriting TestCase class) for updating student user information
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#             Creating a student user which can be used in all the functions
#             and printing the testing class start
#         """
#         super(UpdateStudentDetailsTest, cls).setUpClass()
#         print("\n__Update Student Details SetUp__")
#         print("Module - result")
#         cls.student = get_user_model().objects.create_user(username='student', password='student',
#                                                            email='student@stude.nt', first_name='stud', last_name='ent')
#         cls.student.save()
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#             Deleting the student user after the class finishes
#             and printing the testing class end
#         """
#         super(UpdateStudentDetailsTest, cls).tearDownClass()
#         print("\n__Update Student Details TearDown__")
#         cls.student.delete()
#
#         # integration test
#
#     def test_integration_update_student_details(self, username='notStudent', password='notStudent',
#                                                 email='notStudent@stude.nt', first_name='not', last_name='student'):
#         """
#             Update student user information testing function
#
#             Args:
#                 username (String): username input which is set as notStudent by default
#                 password (String): password input which is set as notStudent by default
#                 email (String): email input which is set as notStudent@stude.nt by default
#                 first_name (String): first name input which is set as not by default
#                 last_name (String): last name input which is set as student by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         self.student_test = StudentRegistrationTest
#         if self.student_test:
#             if self.student is not None:
#                 self.student.username = username
#                 self.student.password = password
#                 self.student.email = email
#                 self.student.first_name = first_name
#                 self.student.last_name = last_name
#
#                 self.student.save()
#
#             test = (self.student.username == username and self.student.password == password
#                     and self.student.email == email and self.student.first_name == first_name
#                     and self.student.last_name == last_name)
#
#         self.assertTrue(test)
#         print("\nCorrect Update Student Details Integration Test - ", positive_test_result(test))
# # Update Student Details tests
#
#
# # View Student Details tests
# class ViewStudentDetailsTest(TestCase):
#     """
#         Testing class (Inheriting TestCase class) for viewing student user information
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#             Creating a student user which can be used in all the functions
#             and printing the testing class start
#         """
#         super(ViewStudentDetailsTest, cls).setUpClass()
#         print("\n__View Student Details SetUp__")
#         print("Module - result")
#
#         cls.user_dict = {
#             'username': 'student',
#             'password': 'student',
#             'email': 'student@stude.nt',
#             'first_name': 'stud',
#             'last_name': 'ent',
#         }
#
#         cls.student = get_user_model().objects.create_user(username='student', password='student',
#                                                            email='student@stude.nt', first_name='stud', last_name='ent')
#         cls.student.save()
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#             Deleting the student user after the class finishes
#             and printing the testing class end
#         """
#         super(ViewStudentDetailsTest, cls).tearDownClass()
#         print("\n__View Student Details TearDown__")
#         cls.student.delete()
#
#     # integration test
#
#     def test_integration_view_student_details(self, username='student', password='student', email='student@stude.nt',
#                                               first_name='stud', last_name='ent'):
#         """
#             View student user information testing function
#
#             Args:
#                 username (String): username input which is set as student by default
#                 password (String): password input which is set as student by default
#                 email (String): email input which is set as student@stude.nt by default
#                 first_name (String): first name input which is set as stud by default
#                 last_name (String): last name input which is set as ent by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         self.student_test = StudentRegistrationTest
#         if self.student_test:
#             test = (self.student.username == self.user_dict['username'] and self.student.email == self.user_dict['email']
#                     and self.student.first_name == self.user_dict['first_name']
#                     and self.student.last_name == self.user_dict['last_name'])
#
#         self.assertTrue(test)
#         print("\nCorrect View Student Details Integration Test - ", positive_test_result(test))
# # View Student Details tests
#
#
# # Teacher Registration test
# class TeacherRegistrationTest(TestCase):
#     """
#         Testing class (Inheriting TestCase class) for registering teacher user information
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#             Creating a teacher user which can be used in all the functions
#             and printing the testing class start
#         """
#         super(TeacherRegistrationTest, cls).setUpClass()
#         print("\n__Teacher Registration SetUp__")
#         print("Module - result")
#         cls.teacher = TeacherExtra()
#         cls.teacher.username = 'teacher'
#         cls.teacher.password1 = 'teacher'
#         cls.teacher.password2 = 'teacher'
#         cls.teacher.first_name = 'tea'
#         cls.teacher.last_name = 'cher'
#         cls.teacher.email = 'teacher@teach.er'
#         cls.teacher.phone = '0521234567'
#         cls.teacher.subjects = 'math'
#
#         cls.teacher_user = get_user_model().objects.create_user(username=cls.teacher.username,
#                                                                 password=cls.teacher.password1, email=cls.teacher.email,
#                                                                 first_name=cls.teacher.first_name,
#                                                                 last_name=cls.teacher.last_name)
#         cls.teacher_user.is_superuser = False
#         cls.teacher_user.is_staff = True
#         cls.teacher_user.save()
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#             Deleting the teacher user after the class finishes
#             and printing the testing class end
#         """
#         super(TeacherRegistrationTest, cls).tearDownClass()
#         print("\n__Teacher Registration TearDown__")
#         cls.teacher_user.delete()
#
#     # integration tests
#
#     def test_integration_correct_teacher_creation(self, username='teacher', password='teacher'):
#         """
#             Create teacher user information testing function with correct input
#
#             Args:
#                 username (String): username input which is set as teacher by default
#                 password (String): password input which is set as teacher by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         user = get_user_model().objects.get(username='teacher')
#         login_test = LoginTest().test_unit_correct(username=username, password=password)
#         test_registration = False
#         if login_test:
#             test_registration = (self.teacher_user.username == user.username
#                                  and self.teacher_user.password == user.password
#                                  and self.teacher_user.email == user.email
#                                  and self.teacher_user.first_name == user.first_name
#                                  and self.teacher_user.last_name == user.last_name)
#         self.assertTrue(test_registration)
#         print("\nCorrect Teacher Registration + Login Integration Test - ", positive_test_result(test_registration))
#
#     def test_integration_wrong_username_teacher_creation(self, username='wrong', password='teacher'):
#         """
#             Create teacher user information testing function with incorrect username input
#
#             Args:
#                 username (String): username input which is set as wrong by default
#                 password (String): password input which is set as teacher by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         user = get_user_model().objects.get(username='teacher')
#         login_test = LoginTest().test_unit_wrong_username(username=username, password=password)
#         test_registration = False
#         if login_test:
#             test_registration = (self.teacher_user.username == user.username
#                                  and self.teacher_user.password == user.password
#                                  and self.teacher_user.email == user.email)
#         self.assertFalse(test_registration)
#         print("\nWrong Username Teacher Registration + Login Integration Test - ", negative_test_result(test_registration))
#
#     def test_integration_wrong_password_teacher_creation(self, username='teacher', password='wrong'):
#         """
#             Create teacher user information testing function with incorrect password input
#
#             Args:
#                 username (String): username input which is set as teacher by default
#                 password (String): password input which is set as wrong by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         user = get_user_model().objects.get(username='teacher')
#         login_test = LoginTest().test_unit_wrong_password(username=username, password=password)
#         test_registration = False
#         if login_test:
#             test_registration = (self.teacher_user.username == user.username
#                                  and self.teacher_user.password == user.password
#                                  and self.teacher_user.email == user.email)
#         self.assertFalse(test_registration)
#         print("\nWrong Password Teacher Registration + Login Integration Test - ", negative_test_result(test_registration))
#
#     def test_integration_wrong_input_teacher_creation(self, username='wrong', password='wrong'):
#         """
#             Create teacher user information testing function with incorrect username and password inputs
#
#             Args:
#                 username (String): username input which is set as wrong by default
#                 password (String): password input which is set as wrong by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         user = get_user_model().objects.get(username='teacher')
#         login_test = LoginTest().test_unit_wrong_input(username=username, password=password)
#         test_registration = False
#         if login_test:
#             test_registration = (self.teacher_user.username == user.username
#                                  and self.teacher_user.password == user.password
#                                  and self.teacher_user.email == user.email)
#         self.assertFalse(test_registration)
#         print("\nWrong Password Teacher Registration + Login Integration Test - ", negative_test_result(test_registration))
# # Teacher Registration test
#
#
# # Student Registration test
# class StudentRegistrationTest(TestCase):
#     """
#         Testing class (Inheriting TestCase class) for registering student user information
#     """
#     @classmethod
#     def setUpClass(cls):
#         """
#             Creating a student user which can be used in all the functions
#             and printing the testing class start
#         """
#         super(StudentRegistrationTest, cls).setUpClass()
#         print("\n__Student Registration SetUp__")
#         print("Module - result")
#         cls.student = StudentExtra()
#         cls.student.username = 'student'
#         cls.student.password1 = 'student'
#         cls.student.password2 = 'student'
#         cls.student.first_name = 'stud'
#         cls.student.last_name = 'ent'
#         cls.student.email = 'student@stude.nt'
#         cls.student.phone = '0521454567'
#         cls.student.birth_date = '1995-05-01'
#         cls.student.parentName_F = 'bob'
#         cls.student.parentPhone_F = '052987125'
#         cls.student.parentName_M = 'bella'
#         cls.student.parentPhone_M = '0529871256'
#
#         cls.student.is_superuser = False
#         cls.student.is_staff = False
#
#         cls.student_user = get_user_model().objects.create_user(username=cls.student.username,
#                                                                 password=cls.student.password1, email=cls.student.email,
#                                                                 first_name=cls.student.first_name,
#                                                                 last_name=cls.student.last_name)
#
#         cls.student.save()
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#             Deleting the student user after the class finishes
#             and printing the testing class end
#         """
#         super(StudentRegistrationTest, cls).tearDownClass()
#         print("\n__Student Registration TearDown__")
#         cls.student.delete()
#
#     # integration tests
#
#     def test_integration_correct_student_creation(self, username='student', password='student'):
#         """
#             Create teacher user information testing function with correct input
#
#             Args:
#                 username (String): username input which is set as student by default
#                 password (String): password input which is set as student by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         user = get_user_model().objects.get(username='student')
#         login_test = LoginTest().test_unit_correct(username=username, password=password)
#         test_registration = False
#         if login_test:
#             test_registration = (self.student_user.username == user.username
#                                  and self.student_user.password == user.password
#                                  and self.student_user.email == user.email
#                                  and self.student_user.first_name == user.first_name
#                                  and self.student_user.last_name == user.last_name)
#         self.assertTrue(test_registration)
#         print("\nCorrect Student Registration + Login Integration Test - ", positive_test_result(test_registration))
#
#     def test_integration_wrong_username_student_creation(self, username='wrong', password='student'):
#         """
#             Create teacher user information testing function with incorrect username input
#
#             Args:
#                 username (String): username input which is set as wrong by default
#                 password (String): password input which is set as student by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         user = get_user_model().objects.get(username='student')
#         login_test = LoginTest().test_unit_wrong_username(username=username, password=password)
#         test_registration = False
#         if login_test:
#             test_registration = (self.student_user.username == user.username
#                                  and self.student_user.password == user.password
#                                  and self.student_user.email == user.email)
#         self.assertFalse(test_registration)
#         print("\nWrong Username Student Registration + Login Integration Test - ", negative_test_result(test_registration))
#
#     def test_integration_wrong_password_teacher_creation(self, username='student', password='wrong'):
#         """
#             Create teacher user information testing function with incorrect password input
#
#             Args:
#                 username (String): username input which is set as student by default
#                 password (String): password input which is set as wrong by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         user = get_user_model().objects.get(username='student')
#         login_test = LoginTest().test_unit_wrong_password(username=username, password=password)
#         test_registration = False
#         if login_test:
#             test_registration = (self.student_user.username == user.username
#                                  and self.student_user.password == user.password
#                                  and self.student_user.email == user.email)
#         self.assertFalse(test_registration)
#         print("\nWrong Password Student Registration + Login Integration Test - ",
#               negative_test_result(test_registration))
#
#     def test_integration_wrong_input_teacher_creation(self, username='wrong', password='wrong'):
#         """
#             Create student user information testing function with incorrect username and password inputs
#
#             Args:
#                 username (String): username input which is set as wrong by default
#                 password (String): password input which is set as wrong by default
#
#             Returns:
#                 Boolean: True or False
#         """
#         user = get_user_model().objects.get(username='student')
#         login_test = LoginTest().test_unit_wrong_input(username=username, password=password)
#         test_registration = False
#         if login_test:
#             test_registration = (self.student_user.username == user.username
#                                  and self.student_user.password == user.password
#                                  and self.student_user.email == user.email)
#         self.assertFalse(test_registration)
#         print("\nWrong Password Student Registration + Login Integration Test - ", negative_test_result(test_registration))
# # Student Registration test
#
#
# # News test
# class NewsTest(TestCase):
#     """
#         Testing class (Inheriting TestCase class) for creating, viewing and deleting news
#     """
#     news_dict = {
#         'title': 'news',
#         'body': 'testing our news section',
#         'date': '2021-05-05 18:33:00',
#     }
#
#     @classmethod
#     def setUpClass(cls):
#         """
#             Creating news article which can be used in all the functions
#             and printing the testing class start
#         """
#         super(NewsTest, cls).setUpClass()
#         print("\n__News SetUp__")
#         print("Module - result")
#         cls.user = get_user_model().objects.create_user(username='admin', password='admin')
#         cls.user.save()
#         cls.news = ArticleForm(cls.news_dict)
#         cls.news.save(commit=False)
#         cls.news = Article(cls.news_dict)
#
#     @classmethod
#     def tearDownClass(cls):
#         """
#              Deleting the news article after the class finishes
#              and printing the testing class end
#         """
#         super(NewsTest, cls).tearDownClass()
#         print("\n__News TearDown__")
#         cls.user.delete()
#
#     # integration tests
#
#     def test_integration_news_creation(self):
#         """
#             Create news article testing function
#
#             Returns:
#                 Boolean: True or False
#         """
#         login_test = LoginTest().test_unit_correct(username='admin', password='admin')
#         if login_test:
#             user = authenticate(username='admin', password='admin')
#             if user is not None and user.is_authenticated:
#                 self.news.title = self.news_dict['title']
#                 self.news.body = self.news_dict['body']
#                 self.news.date = self.news_dict['date']
#                 test = (self.news.title == self.news_dict['title'] and self.news.body == self.news_dict['body']
#                         and self.news.date == self.news_dict['date'])
#         self.assertTrue(test)
#         print("\nCorrect News Creation Integration Test - ", positive_test_result(test))
#
#     def test_integration_view_news(self):
#         """
#             View news article testing function
#
#             Returns:
#                 Boolean: True or False
#         """
#         login_test = LoginTest().test_unit_correct(username='admin', password='admin')
#         if login_test:
#             user = authenticate(username='admin', password='admin')
#             if user is not None and user.is_authenticated:
#                 test = (self.news.title == self.news_dict['title'] and self.news.body == self.news_dict['body']
#                         and self.news.date == self.news_dict['date'])
#         self.assertTrue(test)
#         print("\nView News Integration Test - ", positive_test_result(test))
#
#     def test_integration_delete_news(self):
#         """
#             Delete news article testing function
#
#             Returns:
#                 Boolean: True or False
#         """
#         login_test = LoginTest().test_unit_correct(username='admin', password='admin')
#         if login_test:
#             user = authenticate(username='admin', password='admin')
#             if user is not None and user.is_authenticated:
#                 self.news.title = None
#                 self.news.body = None
#                 self.news.date = None
#                 if self.news.title is None and self.news.body is None and self.news.date is None:
#                     self.news = None
#                 test = self.news is None
#         self.assertTrue(test)
#         print("\nDelete News Integration Test - ", positive_test_result(test))
# # News test
