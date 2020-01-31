from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_auth_email_successful(self):
        """ creating new user with email suceessful"""
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_email_normalize(self):
        """test user for new email is normalized"""
        email = 'vishallimgire@GmaIL.com'
        user = get_user_model().objects.create_user(
            email,
            'test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ create user with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,
                'test123'
            )

    def test_create_new_superuser(self):
        """create and save new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )
        # import pdb;pdb.set_trace()
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
