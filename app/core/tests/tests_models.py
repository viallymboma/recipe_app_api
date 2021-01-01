from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """
    docstring
    """
    def test_create_user_with_email_sucessful(self):
        """
        Making sure the eamil adress is uccessful
        """
        email = "viallymboma@gmail.com"
        password = "123"
        user = get_user_model().object.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """
        docstring
        """
        email = "viallymboma@MaiL.com"
        user = get_user_model().object.create_user(
            email,
            'test123'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        docstring
        """
        with self.assertRaises(ValueError):
            get_user_model().object.create_user(
                None,
                'test123'
            )

    def test_create_new_superuser(self):
        user = get_user_model().object.create_superuser(
            'viallymboma@MaiL.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
