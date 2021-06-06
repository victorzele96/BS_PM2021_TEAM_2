from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from StudyBuddy.models import TeacherForm as TeacherExtra, StudentForm as StudentExtra
from StudyBuddy.models import Article
from StudyBuddy.forms import ArticleForm
from StudyBuddy.tests_unit import LoginTest, DeleteTeacherTest, DeleteStudentTest, TeacherRegistrationTest, \
                                  StudentRegistrationTest, ViewTeacherDetailsTest, ViewStudentDetailsTest, \
                                  UpdateStudentDetailsTest, UpdateTeacherDetailsTest, NewsTest
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


# _____ INTEGRATION TESTS _____

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

    # integration test

    def test_integration_delete_teacher_details(self):
        """
            Delete teacher user testing function

            Returns:
                Boolean: True or False
        """
        TeacherRegistrationTest().test_unit_correct_teacher_creation(
            'teacher', 'teacher', 'teacher@teach.er', 'bob', 'marley'
        )

        try:
            teacher = get_user_model().objects.get(id=1)
            teacher.delete()
            test = True
        except:
            test = False

            try:
                teacher = get_user_model().objects.get(id=1)
                test = False
            except:
                test = True


            self.assertTrue(test)
        print("\nCorrect Delete Teacher Integration Test - ", positive_test_result(test))
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
        cls.teacher, cls.teacher_extra = TeacherRegistrationTest().test_unit_correct_teacher_creation(
            'teacher', 'teacher', 'teacher@teach.er', 'bob', 'marley'
        )

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

    # integration test

    def test_integration_update_teacher_username(self, username='notTeacher'):
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
        print("\nCorrect Update Teacher Username Integration Test - ", positive_test_result(test))

    def test_integration_update_teacher_email(self, email='notTeacher@teach.er'):
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
        print("\nCorrect Update Teacher Email Integration Test - ", positive_test_result(test))

    def test_integration_update_teacher_first_name(self, first_name='not'):
        """
            Update teacher user information testing function

            Args:
                first_name (String): email input which is set as not by default

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
        print("\nCorrect Update Teacher First Name Integration Test - ", positive_test_result(test))

    def test_integration_update_teacher_last_name(self, last_name='not'):
        """
            Update teacher user information testing function

            Args:
                last_name (String): email input which is set as not by default

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
        print("\nCorrect Update Teacher Last Name Integration Test - ", positive_test_result(test))

    def test_integration_update_teacher_phone(self, phone='0541239856'):
        """
            Update teacher user information testing function

            Args:
                phone (String): email input which is set as 0541239856 by default

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
        print("\nCorrect Update Teacher Phone Integration Test - ", positive_test_result(test))

    def test_integration_update_teacher_subjects(self, subjects='english'):
        """
            Update teacher user information testing function

            Args:
                phone (String): email input which is set as 0541239856 by default

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
        print("\nCorrect Update Teacher Subjects Integration Test - ", positive_test_result(test))
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

        cls.teacher, cls.teacher_extra = TeacherRegistrationTest().test_unit_correct_teacher_creation(
            'teacher', 'teacher', 'teacher@teach.er', 'bob', 'marley'
        )

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

    # integration test

    def test_integration_view_teacher_details(self, username='teacher', password='teacher', email='teacher@teach.er',
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
        teacher = get_user_model().objects.get(id=1)
        teacher_extra = TeacherExtra.objects.get(id=1)

        test = (self.teacher.username == teacher.username and self.teacher.email == teacher.email
                and self.teacher.password == teacher.password and self.teacher.first_name == teacher.first_name
                and self.teacher.last_name == teacher.last_name and self.teacher_extra.phone == teacher_extra.phone
                and self.teacher_extra.subjects == teacher_extra.subjects)

        self.assertTrue(test)
        print("\nCorrect View Teacher Details Integration Test - ", positive_test_result(test))
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

    # integration test

    def test_integration_delete_student_details(self):
        """
            Delete teacher user information testing function

            Returns:
                Boolean: True or False
        """
        StudentRegistrationTest().test_unit_correct_student_creation(
            'student', 'student', 'student@stud.ent', 'marley', 'bob'
        )

        try:
            student = get_user_model().objects.get(id=1)
            student.delete()
            test = True
        except:
            test = False

        try:
            student = get_user_model().objects.get(id=1)
            test = False
        except:
            test = True

            self.assertTrue(test)
        print("\nCorrect Delete Student Integration Test - ", positive_test_result(test))
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

        cls.student, cls.student_extra = StudentRegistrationTest().test_unit_correct_student_creation(
            'student', 'student', 'student@stud.ent', 'marley', 'bob'
        )

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

        # integration test

    def test_integration_update_student_username(self, username='notStudent'):
        """
            Update student user information testing function

            Args:
                username (String): username input which is set as notStudent by default

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
        print("\nCorrect Update Student Username Integration Test - ", positive_test_result(test))

    def test_integration_update_student_email(self, email='notStudent@stude.nt'):
        """
            Update student user information testing function

            Args:
                email (String): email input which is set as notStudent@stude.nt by default

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
        print("\nCorrect Update Student Email Integration Test - ", positive_test_result(test))

    def test_integration_update_student_first_name(self, first_name='not'):
        """
            Update student user information testing function

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
        print("\nCorrect Update Student First Name Integration Test - ", positive_test_result(test))

    def test_integration_update_student_last_name(self, username='notStudent', password='notStudent',
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
        print("\nCorrect Update Student Last Name Integration Test - ", positive_test_result(test))

    def test_integration_update_student_information(self, username='notStudent', email='notStudent@stud.ent',
                                                    first_name='not', last_name='not', grade='A1',
                                                    personalPhone='0541239856',
                                                    parentName_F='notBob', parentPhone_F='0529871324',
                                                    parentName_M='notBella', parentPhone_M='0529571256'):
        """
            Update student user information testing function

            Args:
                username (String): username input which is set as notStudent by default
                email (String): email input which is set as notStudent@stud.ent by default
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
            student.username = username
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
        print("\nCorrect Update Student Information Integration Test - ", positive_test_result(test))
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

        cls.student, cls.student_extra = StudentRegistrationTest().test_unit_correct_student_creation(
            'student', 'student', 'student@stud.ent', 'marley', 'bob'
        )

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

    # integration test

    def test_integration_view_student_details(self, username='student', password='student', email='student@stude.nt',
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
        print("\nCorrect View Student Details Integration Test - ", positive_test_result(test))
# View Student Details tests


# Teacher Login test
class TeacherLoginTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for login teacher user
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating a teacher user which can be used in all the functions
            and printing the testing class start
        """
        super(TeacherLoginTest, cls).setUpClass()
        print("\n__Teacher Login SetUp__")
        print("Module - result")

        cls.teacher, cls.teacher_extra = TeacherRegistrationTest().test_unit_correct_teacher_creation(
            'teacher', 'teacher', 'teacher@teach.er', 'bob', 'marley'
        )

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the teacher user after the class finishes
            and printing the testing class end
        """
        super(TeacherLoginTest, cls).tearDownClass()
        print("\n__Teacher Login TearDown__")
        cls.teacher_extra.delete()
        cls.teacher.delete()

        # integration tests

    def test_integration_correct_teacher_creation(self):
        """
            Create teacher user information testing function with correct input

            Returns:
                Boolean: True or False
        """
        test = LoginTest().test_unit_correct(self.teacher.username, self.teacher.username)
        self.assertTrue(test)
        print("\nCorrect Teacher Registration + Login Integration Test - ", positive_test_result(test))

    def test_integration_wrong_username_teacher_creation(self, username='wrong', password='teacher'):
        """
            Create teacher user information testing function with incorrect username input

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as teacher by default

            Returns:
                Boolean: True or False
        """
        test = LoginTest().test_unit_wrong_username(username, self.teacher.username)

        self.assertFalse(test)
        print("\nWrong Username Teacher Registration + Login Integration Test - ", negative_test_result(test))

    def test_integration_wrong_password_teacher_creation(self, username='teacher', password='wrong'):
        """
            Create teacher user information testing function with incorrect password input

            Args:
                username (String): username input which is set as teacher by default
                password (String): password input which is set as wrong by default

            Returns:
                Boolean: True or False
        """
        test = LoginTest().test_unit_wrong_password(self.teacher.username, password)

        self.assertFalse(test)
        print("\nWrong Password Teacher Registration + Login Integration Test - ", negative_test_result(test))

    def test_integration_wrong_input_teacher_creation(self, username='wrong', password='wrong'):
        """
            Create teacher user information testing function with incorrect username and password inputs

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as wrong by default

            Returns:
                Boolean: True or False
        """
        test = LoginTest().test_unit_wrong_input(username, password)

        self.assertFalse(test)
        print("\nWrong Password Teacher Registration + Login Integration Test - ", negative_test_result(test))
# Teacher Login test


# Student Login test
class StudentLoginTest(TestCase):
    """
        Testing class (Inheriting TestCase class) for login student user
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating a student user which can be used in all the functions
            and printing the testing class start
        """
        super(StudentLoginTest, cls).setUpClass()
        print("\n__Student Login SetUp__")
        print("Module - result")

        cls.student, cls.student_extra = StudentRegistrationTest().test_unit_correct_student_creation(
            'student', 'student', 'student@stud.ent', 'marley', 'bob'
        )

    @classmethod
    def tearDownClass(cls):
        """
            Deleting the student user after the class finishes
            and printing the testing class end
        """
        super(StudentLoginTest, cls).tearDownClass()
        print("\n__Student Login TearDown__")
        cls.student_extra.delete()
        cls.student.delete()

        # integration tests

    def test_integration_correct_student_creation(self):
        """
            Create student user information testing function with correct input

            Returns:
                Boolean: True or False
        """
        test = LoginTest().test_unit_correct(self.student.username, self.student.username)
        self.assertTrue(test)
        print("\nCorrect Student Registration + Login Integration Test - ", positive_test_result(test))

    def test_integration_wrong_username_student_creation(self, username='wrong'):
        """
            Create student user information testing function with incorrect username input

            Args:
                username (String): username input which is set as wrong by default

            Returns:
                Boolean: True or False
        """
        test = LoginTest().test_unit_wrong_username(username, self.student.username)

        self.assertFalse(test)
        print("\nWrong Username Student Registration + Login Integration Test - ", negative_test_result(test))

    def test_integration_wrong_password_student_creation(self, password='wrong'):
        """
            Create student user information testing function with incorrect password input

            Args:
                password (String): password input which is set as wrong by default

            Returns:
                Boolean: True or False
        """
        test = LoginTest().test_unit_wrong_password(self.student.username, password)

        self.assertFalse(test)
        print("\nWrong Password Student Registration + Login Integration Test - ", negative_test_result(test))

    def test_integration_wrong_input_student_creation(self, username='wrong', password='wrong'):
        """
            Create student user information testing function with incorrect username and password inputs

            Args:
                username (String): username input which is set as wrong by default
                password (String): password input which is set as wrong by default

            Returns:
                Boolean: True or False
        """
        test = LoginTest().test_unit_wrong_input(username, password)

        self.assertFalse(test)
        print("\nWrong Password Student Registration + Login Integration Test - ", negative_test_result(test))
# Student Login test


# News test
class News_Test(TestCase):
    """
        Testing class (Inheriting TestCase class) for creating, viewing and deleting news
    """
    @classmethod
    def setUpClass(cls):
        """
            Creating news article which can be used in all the functions
            and printing the testing class start
        """
        super(News_Test, cls).setUpClass()
        print("\n__News SetUp__")
        print("Module - result")

        cls.admin = get_user_model().objects.create_user(username='admin', password='admin')
        cls.admin.is_superuser = 1
        cls.admin.save()

    @classmethod
    def tearDownClass(cls):
        """
             Deleting the news article after the class finishes
             and printing the testing class end`
        """
        super(News_Test, cls).tearDownClass()
        print("\n__News TearDown__")
        cls.admin.delete()

    # integration tests

    def test_integration_news_creation(self):
        """
            Create news article testing function

            Returns:
                Boolean: True or False
        """
        try:
            admin = get_user_model().objects.get(is_superuser=1)
            test = True
        except:
            test = False
        login_test = LoginTest().test_unit_correct(username=admin.username, password=admin.username)
        if login_test:
            user = authenticate(username=admin.username, password=admin.username)
            if user is not None and user.is_authenticated:
                test = NewsTest().test_unit_news_creation()
        else:
            test = False
        self.assertTrue(test)
        print("\nCorrect News Creation Integration Test - ", positive_test_result(test))

    def test_integration_news_same_fields(self):
        """
            View news article testing function

            Returns:
                Boolean: True or False
        """
        try:
            admin = get_user_model().objects.get(is_superuser=1)
            test = True
        except:
            test = False
        login_test = LoginTest().test_unit_correct(username=admin.username, password=admin.username)
        if login_test:
            user = authenticate(username=admin.username, password=admin.username)
            if user is not None and user.is_authenticated:
                test = NewsTest().test_unit_news_same_fields()
        else:
            test = False
        self.assertTrue(test)
        print("\nNews With Same Fields Integration Test - ", positive_test_result(test))

    def test_integration_delete_news(self):
        """
            Delete news article testing function

            Returns:
                Boolean: True or False
        """
        try:
            admin = get_user_model().objects.get(is_superuser=1)
            test = True
        except:
            test = False
        login_test = LoginTest().test_unit_correct(username=admin.username, password=admin.username)
        if login_test:
            user = authenticate(username=admin.username, password=admin.username)
            if user is not None and user.is_authenticated:
                test = NewsTest().test_unit_delete_news()
        else:
            test = False
        self.assertTrue(test)
        print("\nDelete News Integration Test - ", positive_test_result(test))
# News test
