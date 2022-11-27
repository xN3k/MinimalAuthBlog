from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignupPageTest(TestCase):
    def test_signup_url_exitst_at_correct_location(self):
        response =self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_form(self):
        response = self.client.post(reverse('signup'),
        {
            'username':'testuser',
            'email':'test@test.com',
            'password1':'123456prime',
            'password2':'123456prime',
        },
        )
        self.assertEqual(response.status_code, 302),
        self.assertEqual(get_user_model().objects.all().count(), 1),
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'test@test.com')   