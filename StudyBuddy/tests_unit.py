import django
from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from StudyBuddy.models import TeacherForm as TeacherExtra, StudentForm as StudentExtra
from .models import Article, StudentClassroom, Classroom, Subject, ClassSubject
from .models import Exercise, Subject_Exam, Subject_Exercise, Student_Exercises
from .models import Subject_Exam, Subject_Exercise, Student_Exercises
from .forms import ArticleForm, PrivateChatTestForm, ClassChatTestForm
from datetime import datetime
from django.utils import timezone

import pytz

# _____ UTILITY FUNCTIONS _____

timezone.activate(pytz.timezone("UTC"))

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
            Creating teacher user that can be used in all the test methods in the class
            and printing the testing class start
        """
        super(DeleteTeacherTest, cls).setUpClass()
        cls.teacher = get_user_model().objects.create_user(username='teacher', password='teacher', first_name='tea',
                                                           last_name='cher', email='teacher@teach.er')
        cls.teacher.is_superuser = False
        cls.teacher.is_staff = True
        cls.teacher.save()

        cls.teacher_extra = TeacherExtra()
        cls.teacher_extra.user = cls.teacher
        cls.teacher_extra.phone = '0521234567'
        cls.teacher_extra.subjects = 'math'

        cls.teacher_extra.save()
        print("\n__Delete Teacher SetUp__")
        print("Module - result")

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the teacher user at the end of class actions
            and printing the testing class end
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
        try:
            teacher_extra = TeacherExtra.objects.get(id=1)
            teacher_extra.delete()
        except:
            test = False
        try:
            teacher = get_user_model().objects.get(id=1)
            teacher.delete()
        except:
            test = False

        try:
            teacher_extra = TeacherExtra.objects.get(id=1)
            test = False
        except:
            test = True

        try:
            teacher = get_user_model().objects.get(id=1)
            test = False
        except:
            test = True

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

        cls.teacher = get_user_model().objects.create_user(username='teacher', password='teacher', first_name='tea',
                                                           last_name='cher', email='teacher@teach.er')
        cls.teacher.is_superuser = False
        cls.teacher.is_staff = True
        cls.teacher.save()

        cls.teacher_extra = TeacherExtra()
        cls.teacher_extra.user = cls.teacher
        cls.teacher_extra.phone = '0521234567'
        cls.teacher_extra.subjects = 'math'

        cls.teacher_extra.save()

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the teacher user after the class finishes
            and printing the testing class end
        """
        super(UpdateTeacherDetailsTest, cls).tearDownClass()
        print("\n__Update Teacher Details TearDown__")
        cls.teacher_extra.delete()
        cls.teacher.delete()

    # unit test

    def test_unit_update_teacher_username(self, username='notTeacher'):
        """
            Update teacher user information testing function

            Args:
                username (String): username input which is set as notTeacher by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            teacher = get_user_model().objects.get(id=1)
            teacher.username = username
            teacher.save()
        except:
            test = False

        try:
            teacher_extra = TeacherExtra.objects.get(id=1)
        except:
            test = False

        try:
            teacher = get_user_model().objects.get(id=1)
            if (teacher.username == username
                    and teacher.password == self.teacher.password
                    and teacher.email == self.teacher.email
                    and teacher.first_name == self.teacher.first_name
                    and teacher.last_name == self.teacher.last_name
                    and teacher_extra.phone == self.teacher_extra.phone
                    and teacher_extra.subjects == self.teacher_extra.subjects):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Teacher Username Unit Test - ", positive_test_result(test))

    def test_unit_update_teacher_email(self, email='notTeacher@teach.er'):
        """
            Update teacher user information testing function

            Args:
                email (String): email input which is set as notTeacher@teach.er by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            teacher = get_user_model().objects.get(id=1)
            teacher.email = email
            teacher.save()
        except:
            test = False

        try:
         teacher_extra = TeacherExtra.objects.get(id=1)
        except:
            test = False

        try:
            teacher = get_user_model().objects.get(id=1)
            if (teacher.username == self.teacher.username
                    and teacher.password == self.teacher.password
                    and teacher.email == email
                    and teacher.first_name == self.teacher.first_name
                    and teacher.last_name == self.teacher.last_name
                    and teacher_extra.phone == self.teacher_extra.phone
                    and teacher_extra.subjects == self.teacher_extra.subjects):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Teacher Email Unit Test - ", positive_test_result(test))

    def test_unit_update_teacher_first_name(self, first_name='not'):
        """
            Update teacher user information testing function

            Args:
                first_name (String): first name input which is set as not by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            teacher = get_user_model().objects.get(id=1)
            teacher.first_name = first_name
            teacher.save()
        except:
            test = False

        try:
         teacher_extra = TeacherExtra.objects.get(id=1)
        except:
            test = False

        try:
            teacher = get_user_model().objects.get(id=1)
            if (teacher.username == self.teacher.username
                    and teacher.password == self.teacher.password
                    and teacher.email == self.teacher.email
                    and teacher.first_name == first_name
                    and teacher.last_name == self.teacher.last_name
                    and teacher_extra.phone == self.teacher_extra.phone
                    and teacher_extra.subjects == self.teacher_extra.subjects):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Teacher First Name Unit Test - ", positive_test_result(test))

    def test_unit_update_teacher_last_name(self, last_name='not'):
        """
            Update teacher user information testing function

            Args:
                last_name (String): last name input which is set as teacher by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            teacher = get_user_model().objects.get(id=1)
            teacher.last_name = last_name
            teacher.save()
        except:
            test = False

        try:
         teacher_extra = TeacherExtra.objects.get(id=1)
        except:
            test = False

        try:
            teacher = get_user_model().objects.get(id=1)
            if (teacher.username == self.teacher.username
                    and teacher.password == self.teacher.password
                    and teacher.email == self.teacher.email
                    and teacher.first_name == self.teacher.first_name
                    and teacher.last_name == last_name
                    and teacher_extra.phone == self.teacher_extra.phone
                    and teacher_extra.subjects == self.teacher_extra.subjects):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Teacher Last Name Unit Test - ", positive_test_result(test))

    def test_unit_update_teacher_phone(self, phone='0541239856'):
        """
            Update teacher user information testing function

            Args:
                phone (String): username input which is set as 0541239856 by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            teacher = get_user_model().objects.get(id=1)
        except:
            test = False

        try:
         teacher_extra = TeacherExtra.objects.get(id=1)
         teacher_extra.phone = phone
         teacher_extra.save()
        except:
            test = False

        try:
            teacher_extra = TeacherExtra.objects.get(id=1)
            if (teacher.username == self.teacher.username
                    and teacher.password == self.teacher.password
                    and teacher.email == self.teacher.email
                    and teacher.first_name == self.teacher.first_name
                    and teacher.last_name == self.teacher.last_name
                    and teacher_extra.phone == phone
                    and teacher_extra.subjects == self.teacher_extra.subjects):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Teacher Phone Unit Test - ", positive_test_result(test))

    def test_unit_update_teacher_subjects(self, subjects='english'):
        """
            Update teacher user information testing function

            Args:
                subjects (String): username input which is set as english by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            teacher = get_user_model().objects.get(id=1)
        except:
            test = False

        try:
         teacher_extra = TeacherExtra.objects.get(id=1)
         teacher_extra.subjects = subjects
         teacher_extra.save()
        except:
            test = False

        try:
            teacher_extra = TeacherExtra.objects.get(id=1)
            if (teacher.username == self.teacher.username
                    and teacher.password == self.teacher.password
                    and teacher.email == self.teacher.email
                    and teacher.first_name == self.teacher.first_name
                    and teacher.last_name == self.teacher.last_name
                    and teacher_extra.phone == self.teacher_extra.phone
                    and teacher_extra.subjects == subjects):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Teacher Subjects Unit Test - ", positive_test_result(test))

    def test_unit_update_teacher_information(self, username='notTeacher', email='notTeacher@teach.er',
                                             first_name='not', last_name='not',
                                             phone='0541239856', subjects='english'):
        """
            Update teacher user information testing function

            Args:
                username (String): username input which is set as notTeacher by default
                email (String): email input which is set as notTeacher@teach.er by default
                first_name (String): first name input which is set as not by default
                last_name (String): last name input which is set as teacher by default
                phone (String): last name input which is set as 0541239856 by default
                subjects (String): last name input which is set as english by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            teacher = get_user_model().objects.get(id=1)
            teacher.username = username
            teacher.email = email
            teacher.first_name = first_name
            teacher.last_name = last_name
        except:
            test = False

        try:
         teacher_extra = TeacherExtra.objects.get(id=1)
         teacher_extra.phone = phone
         teacher_extra.subjects = subjects
         teacher_extra.save()
        except:
            test = False

        try:
            teacher_extra = TeacherExtra.objects.get(id=1)
            if (teacher.username == username
                    and teacher.password == self.teacher.password
                    and teacher.email == email
                    and teacher.first_name == first_name
                    and teacher.last_name == last_name
                    and teacher_extra.phone == phone
                    and teacher_extra.subjects == subjects):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Teacher Information Unit Test - ", positive_test_result(test))
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

        cls.teacher = get_user_model().objects.create_user(username='teacher', password='teacher', first_name='tea',
                                                           last_name='cher', email='teacher@teach.er')
        cls.teacher.is_superuser = False
        cls.teacher.is_staff = True
        cls.teacher.save()

        cls.teacher_extra = TeacherExtra()
        cls.teacher_extra.user = cls.teacher
        cls.teacher_extra.phone = '0521234567'
        cls.teacher_extra.subjects = 'math'

        cls.teacher_extra.save()

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the teacher user after the class finishes all its functions
            and printing the testing class end
        """
        super(ViewTeacherDetailsTest, cls).tearDownClass()
        print("\n__View Teacher Details TearDown__")
        cls.teacher_extra.delete()
        cls.teacher.delete()

    # unit test

    def test_unit_view_teacher_details(self):
        """
            View teacher user information testing function

            Returns:
                Boolean: True or False
        """
        teacher = get_user_model().objects.get(id=1)
        teacher_extra = TeacherExtra.objects.get(id=1)

        test = (self.teacher.username == teacher.username and self.teacher.email == teacher.email
                and self.teacher.password == teacher.password and self.teacher.first_name == teacher.first_name
                and self.teacher.last_name == teacher.last_name and self.teacher_extra.phone == teacher_extra.phone
                and self.teacher_extra.subjects == teacher_extra.subjects)

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
            Creating student user that can be used in all the test methods in the class
            and printing the testing class start
        """
        super(DeleteStudentTest, cls).setUpClass()

        cls.student = get_user_model().objects.create_user(username='student', password='student',
                                                           email='student@stude.nt', first_name='stud',
                                                           last_name='ent')
        cls.student.is_superuser = False
        cls.student.is_staff = False
        cls.student.save()

        cls.student_extra = StudentExtra()
        cls.student_extra.user = cls.student
        cls.student_extra.grade = 'A1'
        cls.student_extra.birth_date = '1995-05-01'
        cls.student_extra.phone = '0521454567'
        cls.student_extra.parentName_F = 'bob'
        cls.student_extra.parentPhone_F = '052987125'
        cls.student_extra.parentName_M = 'bella'
        cls.student_extra.parentPhone_M = '0529871256'

        print("\n__Delete Student SetUp__")
        print("Module - result")

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the student user at the end of class actions
            and printing the testing class end
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
        try:
            student_extra = StudentExtra.objects.get(id=1)
            student_extra.delete()
        except:
            test = False
        try:
            student = get_user_model().objects.get(id=1)
            student.delete()
        except:
            test = False

        try:
            student_extra = TeacherExtra.objects.get(id=1)
            test = False
        except:
            test = True

        try:
            student = get_user_model().objects.get(id=1)
            test = False
        except:
            test = True

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
                                                           email='student@stude.nt', first_name='stud',
                                                           last_name='ent')
        cls.student.is_superuser = False
        cls.student.is_staff = False
        cls.student.save()

        cls.student_extra = StudentExtra()
        cls.student_extra.user = cls.student
        cls.student_extra.grade = 'A1'
        cls.student_extra.birth_date = '1995-05-01'
        cls.student_extra.personalPhone = '0521454567'
        cls.student_extra.parentName_F = 'bob'
        cls.student_extra.parentPhone_F = '052987125'
        cls.student_extra.parentName_M = 'bella'
        cls.student_extra.parentPhone_M = '0529871256'
        cls.student_extra.save()

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the student user after the class finishes
            and printing the testing class end
        """
        super(UpdateStudentDetailsTest, cls).tearDownClass()
        print("\n__Update Student Details TearDown__")
        cls.student_extra.delete()
        cls.student.delete()

    # unit test

    def test_unit_update_student_username(self, username='notStudent'):
        """
            Update teacher user information testing function

            Args:
                username (String): username input which is set as notTeacher by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            student = get_user_model().objects.get(id=1)
            student.username = username
            student.save()
        except:
            test = False

        try:
            student_extra = StudentExtra.objects.get(id=1)
        except:
            test = False

        try:
            student = get_user_model().objects.get(id=1)
            if (student.username == username
                    and student.password == self.student.password
                    and student.email == self.student.email
                    and student.first_name == self.student.first_name
                    and student.last_name == self.student.last_name
                    and student_extra.grade == self.student_extra.grade
                    and student_extra.personalPhone == self.student_extra.personalPhone
                    and student_extra.parentName_F == self.student_extra.parentName_F
                    and student_extra.parentPhone_F == self.student_extra.parentPhone_F
                    and student_extra.parentName_M == self.student_extra.parentName_M
                    and student_extra.parentPhone_M == self.student_extra.parentPhone_M):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Student Username Unit Test - ", positive_test_result(test))

    def test_unit_update_student_email(self, email='student@stude.nt'):
        """
            Update teacher user information testing function

            Args:
                email (String): email input which is set as student@stude.nt by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            student = get_user_model().objects.get(id=1)
            student.email = email
            student.save()
        except:
            test = False

        try:
            student_extra = StudentExtra.objects.get(id=1)
        except:
            test = False

        try:
            student = get_user_model().objects.get(id=1)
            if (student.username == self.student.username
                    and student.password == self.student.password
                    and student.email == email
                    and student.first_name == self.student.first_name
                    and student.last_name == self.student.last_name
                    and student_extra.grade == self.student_extra.grade
                    and student_extra.personalPhone == self.student_extra.personalPhone
                    and student_extra.parentName_F == self.student_extra.parentName_F
                    and student_extra.parentPhone_F == self.student_extra.parentPhone_F
                    and student_extra.parentName_M == self.student_extra.parentName_M
                    and student_extra.parentPhone_M == self.student_extra.parentPhone_M):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Student Email Unit Test - ", positive_test_result(test))

    def test_unit_update_student_first_name(self, first_name='not'):
        """
            Update teacher user information testing function

            Args:
                first_name (String): first name input which is set as not by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            student = get_user_model().objects.get(id=1)
            student.first_name = first_name
            student.save()
        except:
            test = False

        try:
            student_extra = StudentExtra.objects.get(id=1)
        except:
            test = False

        try:
            student = get_user_model().objects.get(id=1)
            if (student.username == self.student.username
                    and student.password == self.student.password
                    and student.email == self.student.email
                    and student.first_name == first_name
                    and student.last_name == self.student.last_name
                    and student_extra.grade == self.student_extra.grade
                    and student_extra.personalPhone == self.student_extra.personalPhone
                    and student_extra.parentName_F == self.student_extra.parentName_F
                    and student_extra.parentPhone_F == self.student_extra.parentPhone_F
                    and student_extra.parentName_M == self.student_extra.parentName_M
                    and student_extra.parentPhone_M == self.student_extra.parentPhone_M):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Student First Name Unit Test - ", positive_test_result(test))

    def test_unit_update_student_last_name(self, last_name='not'):
        """
            Update teacher user information testing function

            Args:
                last_name (String): last name input which is set as teacher by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            student = get_user_model().objects.get(id=1)
            student.last_name = last_name
            student.save()
        except:
            test = False

        try:
            student_extra = StudentExtra.objects.get(id=1)
        except:
            test = False

        try:
            student = get_user_model().objects.get(id=1)
            if (student.username == self.student.username
                    and student.password == self.student.password
                    and student.email == self.student.email
                    and student.first_name == self.student.first_name
                    and student.last_name == last_name
                    and student_extra.grade == self.student_extra.grade
                    and student_extra.personalPhone == self.student_extra.personalPhone
                    and student_extra.parentName_F == self.student_extra.parentName_F
                    and student_extra.parentPhone_F == self.student_extra.parentPhone_F
                    and student_extra.parentName_M == self.student_extra.parentName_M
                    and student_extra.parentPhone_M == self.student_extra.parentPhone_M):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Teacher Last Name Unit Test - ", positive_test_result(test))

    # def test_unit_update_student_grade(self, grade='A2'):
    #     """
    #         Update teacher user information testing function
    #
    #         Args:
    #             grade (String): username input which is set as A2 by default
    #
    #         Returns:
    #             Boolean: True or False
    #     """
    #     test = False
    #     try:
    #         student = get_user_model().objects.get(id=1)
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra.objects.get(id=1)
    #         student_extra.grade = grade
    #         student_extra.save()
    #     except:
    #         test = False
    #
    #     try:
    #         teacher_extra = TeacherExtra.objects.get(id=1)
    #         if (student.username == self.teacher.username
    #                 and student.password == self.student.password
    #                 and student.email == self.student.email
    #                 and student.first_name == self.student.first_name
    #                 and student.last_name == self.student.last_name
    #                 and student_extra.grade == grade
    #                 and student_extra.personalPhone == self.student_extra.personalPhone
    #                 and student_extra.parentName_F == self.student_extra.parentName_F
    #                 and student_extra.parentPhone_F == self.student_extra.parentPhone_F
    #                 and student_extra.parentName_M == self.student_extra.parentName_M
    #                 and student_extra.parentPhone_M == self.student_extra.parentPhone_M):
    #             test = True
    #     except:
    #         test = False
    #
    #     self.assertTrue(test)
    #     print("\nCorrect Update Teacher Grade Unit Test - ", positive_test_result(test))
    #
    # def test_unit_update_student_phone(self, personalPhone='0541239856'):
    #     """
    #         Update teacher user information testing function
    #
    #         Args:
    #             personalPhone (String): username input which is set as 0541239856 by default
    #
    #         Returns:
    #             Boolean: True or False
    #     """
    #     test = False
    #     try:
    #         student = get_user_model().objects.get(id=1)
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra.objects.get(id=1)
    #         student_extra.personalPhone = personalPhone
    #         student_extra.save()
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra().objects.get(id=1)
    #         if (student.username == self.student.username
    #                 and student.password == self.student.password
    #                 and student.email == self.student.email
    #                 and student.first_name == self.student.first_name
    #                 and student.last_name == self.student.last_name
    #                 and student_extra.grade == self.student_extra.grade
    #                 and student_extra.personalPhone == personalPhone
    #                 and student_extra.parentName_F == self.student_extra.parentName_F
    #                 and student_extra.parentPhone_F == self.student_extra.parentPhone_F
    #                 and student_extra.parentName_M == self.student_extra.parentName_M
    #                 and student_extra.parentPhone_M == self.student_extra.parentPhone_M):
    #             test = True
    #     except:
    #         test = False
    #
    #     self.assertTrue(test)
    #     print("\nCorrect Update Student Phone Unit Test - ", positive_test_result(test))
    #
    # def test_unit_update_student_father_name(self, parentName_F='notBob'):
    #     """
    #         Update teacher user information testing function
    #
    #         Args:
    #             parentName_F (String): username input which is set as notBob by default
    #
    #         Returns:
    #             Boolean: True or False
    #     """
    #     test = False
    #     try:
    #         student = get_user_model().objects.get(id=1)
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra.objects.get(id=1)
    #         student_extra.parentName_F = parentName_F
    #         student_extra.save()
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra().objects.all()
    #         if (student.username == self.student.username
    #                 and student.password == self.student.password
    #                 and student.email == self.student.email
    #                 and student.first_name == self.student.first_name
    #                 and student.last_name == self.student.last_name
    #                 and student_extra.grade == self.student_extra.grade
    #                 and student_extra.personalPhone == self.student_extra.personalPhone
    #                 and student_extra.parentName_F == parentName_F
    #                 and student_extra.parentPhone_F == self.student_extra.parentPhone_F
    #                 and student_extra.parentName_M == self.student_extra.parentName_M
    #                 and student_extra.parentPhone_M == self.student_extra.parentPhone_M):
    #             test = True
    #     except:
    #         test = False
    #
    #     self.assertTrue(test)
    #     print("\nCorrect Update Student Father Name Unit Test - ", positive_test_result(test))
    #
    # def test_unit_update_student_father_phone(self, parentPhone_F='0529871324'):
    #     """
    #         Update teacher user information testing function
    #
    #         Args:
    #             parentPhone_F (String): username input which is set as 0529871324 by default
    #
    #         Returns:
    #             Boolean: True or False
    #     """
    #     test = False
    #     try:
    #         student = get_user_model().objects.get(id=1)
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra.objects.get(id=1)
    #         student_extra.parentPhone_F = parentPhone_F
    #         student_extra.save()
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra().objects.get(id=1)
    #         if (student.username == self.student.username
    #                 and student.password == self.student.password
    #                 and student.email == self.student.email
    #                 and student.first_name == self.student.first_name
    #                 and student.last_name == self.student.last_name
    #                 and student_extra.grade == self.student_extra.grade
    #                 and student_extra.personalPhone == self.student_extra.personalPhone
    #                 and student_extra.parentName_F == self.student_extra.parentName_F
    #                 and student_extra.parentPhone_F == parentPhone_F
    #                 and student_extra.parentName_M == self.student_extra.parentName_M
    #                 and student_extra.parentPhone_M == self.student_extra.parentPhone_M):
    #             test = True
    #     except:
    #         test = False
    #
    #     self.assertTrue(test)
    #     print("\nCorrect Update Student Father Phone Unit Test - ", positive_test_result(test))
    #
    # def test_unit_update_student_mother_name(self, parentName_M='notBella'):
    #     """
    #         Update teacher user information testing function
    #
    #         Args:
    #             parentName_M (String): username input which is set as notBella by default
    #
    #         Returns:
    #             Boolean: True or False
    #     """
    #     test = False
    #     try:
    #         student = get_user_model().objects.get(id=1)
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra.objects.get(id=1)
    #         student_extra.parentName_M = parentName_M
    #         student_extra.save()
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra().objects.get(id=1)
    #         if (student.username == self.student.username
    #                 and student.password == self.student.password
    #                 and student.email == self.student.email
    #                 and student.first_name == self.student.first_name
    #                 and student.last_name == self.student.last_name
    #                 and student_extra.grade == self.student_extra.grade
    #                 and student_extra.personalPhone == self.student_extra.personalPhone
    #                 and student_extra.parentName_F == self.student_extra.parentName_F
    #                 and student_extra.parentPhone_F == self.student_extra.parentPhone_F
    #                 and student_extra.parentName_M == parentName_M
    #                 and student_extra.parentPhone_M == self.student_extra.parentPhone_M):
    #             test = True
    #     except:
    #         test = False
    #
    #     self.assertTrue(test)
    #     print("\nCorrect Update Student Mother Name Unit Test - ", positive_test_result(test))
    #
    # def test_unit_update_student_mother_phone(self, parentPhone_M='0529571256'):
    #     """
    #         Update teacher user information testing function
    #
    #         Args:
    #             parentPhone_M (String): username input which is set as 0529571256 by default
    #
    #         Returns:
    #             Boolean: True or False
    #     """
    #     test = False
    #     try:
    #         student = get_user_model().objects.get(id=1)
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra.objects.get(id=1)
    #         student_extra.parentPhone_M = parentPhone_M
    #         student_extra.save()
    #     except:
    #         test = False
    #
    #     try:
    #         student_extra = StudentExtra().objects.get(id=1)
    #         if (student.username == self.student.username
    #                 and student.password == self.student.password
    #                 and student.email == self.student.email
    #                 and student.first_name == self.student.first_name
    #                 and student.last_name == self.student.last_name
    #                 and student_extra.grade == self.student_extra.grade
    #                 and student_extra.personalPhone == self.student_extra.personalPhone
    #                 and student_extra.parentName_F == self.student_extra.parentName_F
    #                 and student_extra.parentPhone_F == self.student_extra.parentPhone_F
    #                 and student_extra.parentName_M == self.student_extra.parentName_M
    #                 and student_extra.parentPhone_M == parentPhone_M):
    #             test = True
    #     except:
    #         test = False
    #
    #     self.assertTrue(test)
    #     print("\nCorrect Update Student Mother Phone Unit Test - ", positive_test_result(test))
    #
    def test_unit_update_student_information(self, username='notTeacher', email='notTeacher@teach.er',
                                             first_name='not', last_name='not', grade='A1', personalPhone='0541239856',
                                             parentName_F='notBob', parentPhone_F='0529871324',
                                             parentName_M='notBella', parentPhone_M='0529571256'):
        """
            Update teacher user information testing function

            Args:
                username (String): username input which is set as notTeacher by default
                email (String): email input which is set as notTeacher@teach.er by default
                first_name (String): first name input which is set as not by default
                last_name (String): last name input which is set as not by default
                grade (String): last name input which is set as A1 by default
                personalPhone (String): last name input which is set as 0541239856 by default
                parentName_F (String): last name input which is set as notBob by default
                parentPhone_F (String): last name input which is set as 0529871324 by default
                parentName_M (String): last name input which is set as notBella by default
                parentPhone_M (String): last name input which is set as 0529571256 by default

            Returns:
                Boolean: True or False
        """
        test = False
        try:
            student = get_user_model().objects.get(id=1)
            student.username= username
            student.email = email
            student.first_name = first_name
            student.last_name = last_name
            student.save()
        except:
            test = False

        try:
            student_extra = StudentExtra.objects.get(id=1)
            student_extra.grade = grade
            student_extra.personalPhone = personalPhone
            student_extra.parentName_F = parentName_F
            student_extra.parentPhone_F = parentPhone_F
            student_extra.parentName_M = parentName_M
            student_extra.parentPhone_M = parentPhone_M
            student_extra.save()
        except:
            test = False

        try:
            student = get_user_model().objects.get(id=1)
            # student_extra = StudentExtra().objects.get(id=1)
            if (student.username == username
                    and student.password == self.student.password
                    and student.email == email
                    and student.first_name == first_name
                    and student.last_name == last_name):
                    # and student_extra.grade == grade
                    # and student_extra.personalPhone == personalPhone
                    # and student_extra.parentName_F == parentName_F
                    # and student_extra.parentPhone_F == parentPhone_F
                    # and student_extra.parentName_M == parentName_M
                    # and student_extra.parentPhone_M == parentPhone_M):
                test = True
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Update Student Information Unit Test - ", positive_test_result(test))
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

        cls.student = get_user_model().objects.create_user(username='student', password='student',
                                                           email='student@stude.nt', first_name='stud',
                                                           last_name='ent')
        cls.student.is_superuser = False
        cls.student.is_staff = False
        cls.student.save()

        cls.student_extra = StudentExtra()
        cls.student_extra.user = cls.student
        cls.student_extra.grade = 'A1'
        cls.student_extra.birth_date = '1995-05-01'
        cls.student_extra.personalPhone = '0521454567'
        cls.student_extra.parentName_F = 'bob'
        cls.student_extra.parentPhone_F = '052987125'
        cls.student_extra.parentName_M = 'bella'
        cls.student_extra.parentPhone_M = '0529871256'
        cls.student_extra.save()

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the student user after the class finishes
            and printing the testing class end
        """
        super(ViewStudentDetailsTest, cls).tearDownClass()
        print("\n__View Student Details TearDown__")
        cls.student_extra.delete()
        cls.student.delete()

    # unit test

    def test_unit_view_student_details(self):
        """
            View student user information testing function

            Returns:
                Boolean: True or False
        """
        student = get_user_model().objects.get(id=1)
        student_extra = StudentExtra.objects.get(id=1)

        test = (self.student.username == student.username and self.student.email == student.email
                and self.student.password == student.password and self.student.first_name == student.first_name
                and self.student.last_name == student.last_name
                and self.student_extra.grade == student_extra.grade
                and self.student_extra.personalPhone == student_extra.personalPhone
                and self.student_extra.parentName_M == student_extra.parentName_M
                and self.student_extra.parentPhone_M == student_extra.parentPhone_M
                and self.student_extra.parentName_F == student_extra.parentName_F
                and self.student_extra.parentPhone_F == student_extra.parentPhone_F)

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
            Printing the testing class start
        """
        cls.teacher = None
        cls.teacher_extra = None
        super(TeacherRegistrationTest, cls).setUpClass()
        print("\n__Teacher Registration SetUp__")
        print("Module - result")

    @classmethod
    def tearDownClass(cls):
        """
            Printing the testing class end
        """
        super(TeacherRegistrationTest, cls).tearDownClass()
        print("\n__Teacher Registration TearDown__")

    # unit tests

    def test_unit_correct_teacher_creation(self, username='teacher', password='teacher', email='teacher@teach.er',
                                           first_name='tea', last_name='cher'):
        """
            Create teacher user information testing function with correct input

            Args:
                username (String): username input which is set as teacher by default
                password (String): password input which is set as teacher by default
                email (String): email input which is set as teacher@teach.er by default
                first_name (String): password input which is set as tea by default
                last_name (String): email input which is set as cher by default

            Returns:
                Boolean: True or False
        """
        self.teacher = get_user_model().objects.create_user(username=username, password=password, email=email,
                                                            first_name=first_name, last_name=last_name)
        self.teacher.is_superuser = False
        self.teacher.is_staff = True
        self.teacher.save()

        self.teacher_extra = TeacherExtra()
        self.teacher_extra.user = self.teacher
        self.teacher_extra.phone = '0521234567'
        self.teacher_extra.subjects = 'math'

        self.teacher_extra.save()

        try:
            teacher = get_user_model().objects.get(id=1)
            teacher_extra = TeacherExtra.objects.get(id=1)
            test = (self.teacher.username == teacher.username
                    and self.teacher.password == teacher.password
                    and self.teacher.email == teacher.email
                    and self.teacher.first_name == teacher.first_name
                    and self.teacher.last_name == teacher.last_name
                    and self.teacher_extra.phone == teacher_extra.phone
                    and self.teacher_extra.subjects == teacher_extra.subjects)
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Teacher Registration + Login Unit Test - ", positive_test_result(test))
        return teacher, teacher_extra

    def test_unit_existing_email_teacher_creation(self, username='teacher', password='teacher',
                                                  email='teacher@teach.er', first_name='tea', last_name='cher'):
        """
            Create teacher user information testing function with already existing email address

            Args:
                username (String): username input which is set as teach by default
                password (String): password input which is set as teacher by default
                email (String): email input which is set as teacher@teach.er by default

            Returns:
                Boolean: True or False
        """
        self.teacher = get_user_model().objects.create_user(username=username, password=password, email=email,
                                                            first_name=first_name, last_name=last_name)
        self.teacher.is_superuser = False
        self.teacher.is_staff = True
        self.teacher.save()

        self.teacher_extra = TeacherExtra()
        self.teacher_extra.user = self.teacher
        self.teacher_extra.phone = '0521234567'
        self.teacher_extra.subjects = 'math'

        self.teacher_extra.save()

        test = False

        try:
            self.teacher1 = get_user_model().objects.create_user(username=username, password=password, email=email,
                                                                 first_name=first_name, last_name=last_name)
            self.teacher1.is_superuser = False
            self.teacher1.is_staff = True
            self.teacher1.save()

            self.teacher1_extra = TeacherExtra()
            self.teacher1_extra.user = self.teacher1
            self.teacher1_extra.phone = self.teacher_extra.phone
            self.teacher1_extra.subjects = self.teacher_extra.subjects

            self.teacher1_extra.save()
        except:
            test = False

        print("\nAlready Existing Email Address Teacher Registration + Login Unit Test - ",
              negative_test_result(test))

# Teacher Registration test


# Student Registration test
class StudentRegistrationTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for registering student user information
    """
    @classmethod
    def setUpClass(cls):
        """
            Printing the testing class start
        """
        super(StudentRegistrationTest, cls).setUpClass()
        print("\n__Student Registration SetUp__")
        print("Module - result")

    @classmethod
    def tearDownClass(cls):
        """
            Printing the testing class end
        """
        super(StudentRegistrationTest, cls).tearDownClass()
        print("\n__Student Registration TearDown__")

    # unit tests

    def test_unit_correct_student_creation(self, username='student', password='student', email='student@stude.nt',
                                           first_name='stud', last_name='ent'):
        """
            Create teacher user information testing function with correct input

            Args:
                username (String): username input which is set as student by default
                password (String): password input which is set as student by default
                email (String): email input which is set as student@stude.nt by default

            Returns:
                Boolean: True or False
        """
        self.student = get_user_model().objects.create_user(username=username, password=password, email=email,
                                                            first_name=first_name, last_name=last_name)
        self.student.is_superuser = False
        self.student.is_staff = False
        self.student.save()

        self.student_extra = StudentExtra()
        self.student_extra.user = self.student
        self.student_extra.grade = 'A1'
        self.student_extra.birth_date = '1995-05-01'
        self.student_extra.personalPhone = '0521454567'
        self.student_extra.parentName_F = 'bob'
        self.student_extra.parentPhone_F = '052987125'
        self.student_extra.parentName_M = 'bella'
        self.student_extra.parentPhone_M = '0529871256'
        self.student_extra.save()

        try:
            student = get_user_model().objects.get(id=1)
            student_extra = StudentExtra.objects.get(id=1)
            test = (self.student.username == student.username
                    and self.student.password == student.password
                    and self.student.email == student.email
                    and self.student.first_name == student.first_name
                    and self.student.last_name == student.last_name
                    and self.student_extra.grade == student_extra.grade
                    and self.student_extra.personalPhone == student_extra.personalPhone
                    and self.student_extra.parentName_F == student_extra.parentName_F
                    and self.student_extra.parentPhone_F == student_extra.parentPhone_F
                    and self.student_extra.parentName_M == student_extra.parentName_M
                    and self.student_extra.parentPhone_M == student_extra.parentPhone_M)
        except:
            test = False

        self.assertTrue(test)
        print("\nCorrect Student Registration + Login Unit Test - ", positive_test_result(test))
        return student, student_extra

    def test_unit_existing_email_student_creation(self, username='student', password='student',
                                                  email='student@stude.nt', first_name='stud', last_name='ent'):
        """
            Create teacher user information testing function with already existing email address

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as student by default
                email (String): email input which is set as student@stude.nt by default
                first_name (String): password input which is set as stud by default
                last_name (String): password input which is set as ent by default

            Returns:
                Boolean: True or False
        """
        self.student = get_user_model().objects.create_user(username=username, password=password, email=email,
                                                            first_name=first_name, last_name=last_name)
        self.student.is_superuser = False
        self.student.is_staff = False
        self.student.save()

        self.student_extra = StudentExtra()
        self.student_extra.user = self.student
        self.student_extra.grade = 'A1'
        self.student_extra.birth_date = '1995-05-01'
        self.student_extra.personalPhone = '0521454567'
        self.student_extra.parentName_F = 'bob'
        self.student_extra.parentPhone_F = '052987125'
        self.student_extra.parentName_M = 'bella'
        self.student_extra.parentPhone_M = '0529871256'
        self.student_extra.save()

        try:
            self.student1 = get_user_model().objects.create_user(username=username, password=password, email=email,
                                                                 first_name=first_name, last_name=last_name)
            self.student1.is_superuser = False
            self.student1.is_staff = False
            self.student1.save()

            self.student1_extra = StudentExtra()
            self.student1_extra.user = self.student1
            self.student1_extra.grade = self.student_extra.grade
            self.student1_extra.birth_date = self.student_extra.birth_date
            self.student1_extra.personalPhone = self.student_extra.personalPhone
            self.student1_extra.parentName_F = self.student_extra.parentName_F
            self.student1_extra.parentPhone_F = self.student_extra.parentPhone_F
            self.student1_extra.parentName_M = self.student_extra.parentName_M
            self.student1_extra.parentPhone_M = self.student_extra.parentPhone_M
            self.student1_extra.save()
            test = True
        except:
            test = False

        self.assertFalse(test)
        print("\nAlready Existing Email Address Student Registration + Login Unit Test - ", negative_test_result(test))
# Student Registration test


# News test
class NewsTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for creating, viewing and deleting news
    """
    news_dict = {
        'title': 'news',
        'body': 'testing our news section',
        'date': datetime(day=5, month=5, year=2021, hour=18, minute=33, tzinfo=pytz.UTC),
    }

    @classmethod
    def setUpClass(cls):
        """
            Printing the testing class start
        """
        super(NewsTest, cls).setUpClass()
        print("\n__News SetUp__")
        print("Module - result")

    @classmethod
    def tearDownClass(cls):
        """
             Printing the testing class end
        """
        super(NewsTest, cls).tearDownClass()
        print("\n__News TearDown__")

    # unit tests

    def test_unit_news_creation(self):
        """
            Create news article testing function

            Returns:
                Boolean: True or False
        """
        self.news = Article(title='news', body='testing our news section', date=datetime(day=5, month=5, year=2021,
                                                                                         hour=18, minute=33,
                                                                                         tzinfo=pytz.UTC))
        self.news.save()

        try:
            news = Article.objects.get(id=1)

            test = (news.title == self.news_dict['title'] and news.body == self.news_dict['body'])
        except:
            test = False

        self.news.delete()
        self.assertTrue(test)
        print("\nCorrect News Creation Unit Test - ", positive_test_result(test))


    def test_unit_delete_news(self):
        """
            Delete news article testing function

            Returns:
                Boolean: True or False
        """
        self.news = Article(title='news', body='testing our news section', date=datetime(day=5, month=5, year=2021,
                                                                                         hour=18, minute=33,
                                                                                         tzinfo=pytz.UTC))
        self.news.save()

        if self.news is not None:
            self.news.delete()

        try:
            self.news = Article.objects.get(id=1)
            test = False
        except:
            test = True

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

    def test_unit_create_classroom(self):
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
        print("\nClassroom Creation Unit Test - ", positive_test_result(test))

    def test_unit_same_teacher(self):
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
        print("\nClassroom Same Teacher Unit Test - ", positive_test_result(test))
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

    def test_unit_creat_subject(self):
        """
            Create subject testing function

            Returns:
                Boolean: True or False
        """
        try:
            teacher = get_user_model().objects.get(id=1, is_superuser=0, is_staff=1)
            test = (self.subject.teacher.id == teacher.id)
        except:
            test = False
        self.assertTrue(test)
        print("\nSubject Creation Unit Test - ", positive_test_result(test))

    def test_unit_same_teacher(self):
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
        print("\nSubject Same Teacher Unit Test - ", positive_test_result(test))
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
        print("\n__ClassSubject SetUp__")
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
        print("\n__ClassSubject TearDown__")
        cls.class_subject.delete()
        cls.subject.delete()
        cls.teacher_user.delete()

    # unit tests

    def test_unit_create_classSubject(self):
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
        print("\nClassSubject Creation Unit Test - ", positive_test_result(test))

    def test_unit_same_fields(self):
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
        print("\nClassSubject Same Fields Unit Test - ", positive_test_result(test))
# ClassSubject test


# Exercise test
class ExerciseTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for creating exercise
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

    def test_unit_create_exercise(self):
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
        print("\nExercise Creation Unit Test - ", positive_test_result(test))

    def test_unit_same_exercise(self):
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
        print("\nExercise Same Exercise Unit Test - ", positive_test_result(test))
# Exercise test


# Subject_Exam test
class Subject_ExamTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for combining exercise and subject
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating teacher user, subject, exercise and exam which can be used in all the functions
            and printing the testing class start
        """
        super(Subject_ExamTest, cls).setUpClass()
        print("\n__Subject_Exam SetUp__")
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
        cls.subject.teacher = get_user_model().objects.get(id=1, is_staff=1, is_superuser=0)
        cls.subject.duration = 2
        cls.subject.save()

        cls.exercise = Exercise()
        cls.exercise.question = 'is it working?'
        cls.exercise.a = 'yes'
        cls.exercise.b = 'no'
        cls.exercise.c = 'i dont know'
        cls.exercise.d = 'maybe'
        cls.exercise.ans = 'a'
        cls.exercise.save()

        cls.exam = Subject_Exam()
        cls.exam.exercise = Exercise.objects.get(id=1)
        cls.exam.subject = Subject.objects.get(id=1)
        cls.exam.description = 'exam description'
        cls.exam.start_time = datetime(day=2, month=7, year=2021, hour=8, tzinfo=pytz.UTC)
        cls.exam.end_time = datetime(day=2, month=7, year=2021, hour=11, tzinfo=pytz.UTC)
        cls.exam.save()


    @classmethod
    def tearDownClass(cls):
        """
             Deleting the teacher user, subject, exercise and the exam after the class finishes
             and printing the testing class end
        """
        super(Subject_ExamTest, cls).tearDownClass()
        print("\n__Subject_Exam TearDown__")
        cls.exam.delete()
        cls.subject.delete()
        cls.exercise.delete()
        cls.teacher_user.delete()

    # unit tests

    def test_unit_create_subject_exam(self):
        """
            Create Exercise testing function

            Returns:
                Boolean: True or False
        """
        try:
            exam = Subject_Exam.objects.get(id=1)
            test = (self.exam.exercise == Exercise.objects.get(id=1)
                    and self.exam.subject == Subject.objects.get(id=1)
                    and self.exam.description == exam.description
                    and self.exam.start_time == exam.start_time
                    and self.exam.end_time == exam.end_time)
        except:
            test = False
        self.assertTrue(test)
        print("\nSubject_Exam Creation Unit Test - ", positive_test_result(test))

    def test_unit_same_exercise(self):
        """
            Check if different exercises cant be created with same fields

            Returns:
                Boolean: True or False
        """
        exam = Subject_Exam.objects.get(id=1)
        try:
            self.exam1 = Subject_Exam()
            self.exam1.subject = Subject.objects.get(id=1)
            self.exam1.exercise = Exercise.objects.get(id=1)
            self.exam1.description = exam.description
            self.exam1.start_time = exam.start_time
            self.exam1.end_time = exam.end_time
            self.exam1.save()
            test = False
        except django.db.utils.IntegrityError:
            test = True
        self.assertTrue(test)
        print("\nSubject_Exam Same Exercise Unit Test - ", positive_test_result(test))
# Subject_Exam test


# Subject_Exercise test
class Subject_ExerciseTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for combining exercise and subject
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating teacher user, subject, exercise and exam which can be used in all the functions
            and printing the testing class start
        """
        super(Subject_ExerciseTest, cls).setUpClass()
        print("\n__Subject_Exercise SetUp__")
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
        cls.subject.teacher = get_user_model().objects.get(id=1, is_staff=1, is_superuser=0)
        cls.subject.duration = 2
        cls.subject.save()

        cls.exercise = Exercise()
        cls.exercise.question = 'is it working?'
        cls.exercise.a = 'yes'
        cls.exercise.b = 'no'
        cls.exercise.c = 'i dont know'
        cls.exercise.d = 'maybe'
        cls.exercise.ans = 'a'
        cls.exercise.save()

        cls.subject_exercise = Subject_Exercise()
        cls.subject_exercise.exercise = Exercise.objects.get(id=1)
        cls.subject_exercise.subject = Subject.objects.get(id=1)
        cls.subject_exercise.description = 'exam description'
        cls.subject_exercise.start_time = datetime(day=2, month=7, year=2021, hour=8, tzinfo=pytz.UTC)
        cls.subject_exercise.end_time = datetime(day=2, month=7, year=2021, hour=11, tzinfo=pytz.UTC)
        cls.subject_exercise.save()


    @classmethod
    def tearDownClass(cls):
        """
             Deleting the exercise and the subject after the class finishes
             and printing the testing class end
        """
        super(Subject_ExerciseTest, cls).tearDownClass()
        print("\n__Subject_Exercise TearDown__")
        cls.subject_exercise.delete()
        cls.subject.delete()
        cls.exercise.delete()
        cls.teacher_user.delete()

    # unit tests

    def test_unit_create_subject_exercise(self):
        """
            Create Exercise testing function

            Returns:
                Boolean: True or False
        """
        try:
            subject_exercise = Subject_Exercise.objects.get(id=1)
            test = (self.subject_exercise.exercise == Exercise.objects.get(id=1)
                    and self.subject_exercise.subject == Subject.objects.get(id=1)
                    and self.subject_exercise.description == subject_exercise.description
                    and self.subject_exercise.start_time == subject_exercise.start_time
                    and self.subject_exercise.end_time == subject_exercise.end_time)
        except:
            test = False
        self.assertTrue(test)
        print("\nSubject_Exercise Creation Unit Test - ", positive_test_result(test))

    def test_unit_same_exercise(self):
        """
            Check if different exercises can be created with same fields

            Returns:
                Boolean: True or False
        """
        try:
            subject_exercise = Subject_Exercise.objects.get(id=1)

            self.subject_exercise1 = Subject_Exam()
            self.subject_exercise1.subject = Subject.objects.get(id=1)
            self.subject_exercise1.exercise = Exercise.objects.get(id=1)
            self.subject_exercise1.description = subject_exercise.description
            self.subject_exercise1.start_time = subject_exercise.start_time
            self.subject_exercise1.end_time = subject_exercise.end_time
            self.subject_exercise1.save()
            test = True
        except django.db.utils.IntegrityError:
            test = False
        self.assertTrue(test)
        print("\nSubject_Exercise Same Exercise Unit Test - ", positive_test_result(test))
# Subject_Exercise test


# Student_Exercises test
class Student_ExercisesTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for combining exercise and student
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating teacher and student users, exercise, student exercise and subject
            which can be used in all the functions and printing the testing class start
        """
        super(Student_ExercisesTest, cls).setUpClass()
        print("\n__Student_Exercises SetUp__")
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

        cls.student_user = get_user_model().objects.create_user(username=cls.student.username,
                                                                password=cls.student.password1, email=cls.student.email,
                                                                first_name=cls.student.first_name,
                                                                last_name=cls.student.last_name)
        cls.student_user.is_superuser = False
        cls.student_user.is_staff = False
        cls.student_user.save()

        cls.subject = Subject()
        cls.subject.subject_name = 'Math'
        cls.subject.teacher = get_user_model().objects.get(is_staff=1, is_superuser=0)
        cls.subject.duration = 2
        cls.subject.save()

        cls.exercise = Exercise()
        cls.exercise.question = 'is it working?'
        cls.exercise.a = 'yes'
        cls.exercise.b = 'no'
        cls.exercise.c = 'i dont know'
        cls.exercise.d = 'maybe'
        cls.exercise.ans = 'a'
        cls.exercise.save()

        cls.subject_exercise = Subject_Exercise()
        cls.subject_exercise.exercise = Exercise.objects.get(id=1)
        cls.subject_exercise.subject = Subject.objects.get(id=1)
        cls.subject_exercise.description = 'exam description'
        cls.subject_exercise.start_time = datetime(day=2, month=7, year=2021, hour=8, tzinfo=pytz.UTC)
        cls.subject_exercise.end_time = datetime(day=2, month=7, year=2021, hour=11, tzinfo=pytz.UTC)
        cls.subject_exercise.save()

        cls.student_exercises = Student_Exercises()
        cls.student_exercises.student = get_user_model().objects.get(is_staff=0, is_superuser=0)
        cls.student_exercises.subject_exercise = Subject_Exercise.objects.get(id=1)
        cls.student_exercises.correct_ans = 1
        cls.student_exercises.total_amount_of_exercises = 1
        cls.student_exercises.save()


    @classmethod
    def tearDownClass(cls):
        """
             Deleting the teacher and student users, exercise, student exercise and the subject after the class finishes
             and printing the testing class end
        """
        super(Student_ExercisesTest, cls).tearDownClass()
        print("\n__Student_Exercises TearDown__")
        cls.student_exercises.delete()
        cls.subject_exercise.delete()
        cls.subject.delete()
        cls.exercise.delete()
        cls.teacher_user.delete()
        cls.student_user.delete()

    # unit tests

    def test_unit_create_student_exercise(self):
        """
            Create Exercise testing function

            Returns:
                Boolean: True or False
        """
        try:
            student_exercises = Student_Exercises.objects.get(id=1)
            test = (self.student_exercises.student == get_user_model().objects.get(is_staff=0, is_superuser=0)
                    and self.student_exercises.subject_exercise == Subject_Exercise.objects.get(id=1)
                    and self.student_exercises.correct_ans == student_exercises.correct_ans
                    and self.student_exercises.total_amount_of_exercises == student_exercises.total_amount_of_exercises)
        except:
            test = False
        self.assertTrue(test)
        print("\nStudent_Exercise Creation Unit Test - ", positive_test_result(test))

    def test_unit_same_subject_exercise(self):
        """
            Check if different student_exercises cant be created with same fields

            Returns:
                Boolean: True or False
        """
        try:
            student_exercises = Student_Exercises.objects.get(id=1)

            self.student_exercises1 = Subject_Exam()
            self.student_exercises1.student = get_user_model().objects.get(is_staff=0, is_superuser=0)
            self.student_exercises1.subject_exercise = Subject_Exercise.objects.get(id=1)
            self.student_exercises1.correct_ans = student_exercises.correct_ans
            self.student_exercises1.total_amount_of_exercises = student_exercises.total_amount_of_exercises
            self.student_exercises1.save()
            test = False
        except django.db.utils.IntegrityError:
            test = True
        self.assertTrue(test)
        print("\nStudent_Exercises Same Subject_Exercise Unit Test - ", positive_test_result(test))
# Student_Exercises test


# StudentClassroom test
class StudentClassroomTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for combining class room and student
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating student users, student and classroom
            which can be used in all the functions and printing the testing class start
        """
        super(StudentClassroomTest, cls).setUpClass()
        print("\n__StudentClassroom SetUp__")
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

        cls.student_user = get_user_model().objects.create_user(username=cls.student.username,
                                                                password=cls.student.password1, email=cls.student.email,
                                                                first_name=cls.student.first_name,
                                                                last_name=cls.student.last_name)
        cls.student_user.is_superuser = False
        cls.student_user.is_staff = False
        cls.student_user.save()

        cls.classroom = Classroom()
        cls.classroom.class_name = 'class1'
        cls.classroom.teacher = cls.teacher_user
        cls.classroom.save()

        cls.student_classroom = StudentClassroom()
        cls.student_classroom.class_room = Classroom.objects.get(id=1)
        cls.student_classroom.user = get_user_model().objects.get(is_superuser=0, is_staff=0)
        cls.student_classroom.save()

    @classmethod
    def tearDownClass(cls):
        """
             Deleting the student users and the classroom after the class finishes
             and printing the testing class end
        """
        super(StudentClassroomTest, cls).tearDownClass()
        print("\n__StudentClassroom TearDown__")
        cls.student_classroom.delete()
        cls.classroom.delete()
        cls.student_user.delete()
        cls.teacher_user.delete()

    # unit tests

    def test_unit_create_student_classroom(self):
        """
            Create student classroom testing function

            Returns:
                Boolean: True or False
        """
        try:
            student_classroom = StudentClassroom.objects.get(id=1)
            test = (self.student_classroom.class_room == Classroom.objects.get(id=1)
                    and self.student_classroom.user == get_user_model().objects.get(is_superuser=0, is_staff=0))
        except:
            test = False
        self.assertTrue(test)
        print("\nStudent_Classroom Creation Unit Test - ", positive_test_result(test))

    def test_unit_same_student_classroom(self):
        """
            Check if different student_exercises cant be created with same student

            Returns:
                Boolean: True or False
        """
        try:
            self.student_classroom1 = Subject_Exam()
            self.student_classroom1.class_room = Classroom.objects.get(id=1)
            self.student_classroom1.user = get_user_model().objects.get(is_superuser=0, is_staff=0)
            self.student_classroom1.save()
            test = False
        except django.db.utils.IntegrityError:
            test = True
        self.assertTrue(test)
        print("\nStudent_Classroom Same Student Unit Test - ", positive_test_result(test))
# StudentClassroom test


# Private_Chat test
class Private_ChatTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for private chatting
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating student and teacher users and private chat
            which can be used in all the functions and printing the testing class start
        """
        super(Private_ChatTest, cls).setUpClass()
        print("\n__Private_Chat SetUp__")
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

        cls.student_user = get_user_model().objects.create_user(username=cls.student.username,
                                                                password=cls.student.password1, email=cls.student.email,
                                                                first_name=cls.student.first_name,
                                                                last_name=cls.student.last_name)
        cls.student_user.is_superuser = False
        cls.student_user.is_staff = False
        cls.student_user.save()

        cls.chat_dict = {
            'receiver_id': get_user_model().objects.get(id=2).id,
            'publish_date': '2021-05-05 18:33:00',
            'msg': 'Good day fine sir!'
        }

        cls.private_chat = PrivateChatTestForm(cls.chat_dict)
        cls.private_chat.save(commit=False)

    @classmethod
    def tearDownClass(cls):
        """
             Deleting the student and teacher users and the private chat after the class finishes
             and printing the testing class end
        """
        super(Private_ChatTest, cls).tearDownClass()
        print("\n__Private_Chat TearDown__")
        cls.student_user.delete()
        cls.teacher_user.delete()

    # unit tests

    def test_unit_private_chat_creation(self):
        """
            Create student private chat testing function

            Returns:
                Boolean: True or False
        """
        self.private_chat.receiver_id = self.chat_dict['receiver_id']
        self.private_chat.msg = self.chat_dict['msg']
        self.private_chat.publish_date = self.chat_dict['publish_date']
        test = (self.private_chat.receiver_id == self.chat_dict['receiver_id'] and self.private_chat.msg == self.chat_dict['msg']
                and self.private_chat.publish_date == self.chat_dict['publish_date'])
        self.assertTrue(test)
        print("\nPrivate_Chat Creation Unit Test - ", positive_test_result(test))
# Private_Chat test


# Class_Chat test
class Class_ChatTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for class chatting
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating student and teacher users, classroom and class chat
            which can be used in all the functions and printing the testing class start
        """
        super(Class_ChatTest, cls).setUpClass()
        print("\n__Class_Chat SetUp__")
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

        cls.student_user = get_user_model().objects.create_user(username=cls.student.username,
                                                                password=cls.student.password1, email=cls.student.email,
                                                                first_name=cls.student.first_name,
                                                                last_name=cls.student.last_name)
        cls.student_user.is_superuser = False
        cls.student_user.is_staff = False
        cls.student_user.save()

        cls.classroom = Classroom()
        cls.classroom.class_name = 'class1'
        cls.classroom.teacher = cls.teacher_user
        cls.classroom.save()

        cls.chat_dict = {
            'publish_date': '2021-05-05 18:33:00',
            'msg': 'Good day fine sir!'
        }

        cls.class_chat = ClassChatTestForm(cls.chat_dict)
        cls.class_chat.save(commit=False)

    @classmethod
    def tearDownClass(cls):
        """
             Deleting the student and teacher users, classroom and the class chat after the class finishes
             and printing the testing class end
        """
        super(Class_ChatTest, cls).tearDownClass()
        print("\n__Class_Chat TearDown__")
        cls.classroom.delete()
        cls.student_user.delete()
        cls.teacher_user.delete()

    # unit tests

    def test_unit_class_chat_creation(self):
        """
            Create student class chat testing function

            Returns:
                Boolean: True or False
        """
        self.class_chat.msg = self.chat_dict['msg']
        self.class_chat.publish_date = self.chat_dict['publish_date']
        test = (self.class_chat.msg == self.chat_dict['msg']
                and self.class_chat.publish_date == self.chat_dict['publish_date'])
        self.assertTrue(test)
        print("\nClass_Chat Creation Unit Test - ", positive_test_result(test))
# Class_Chat test
