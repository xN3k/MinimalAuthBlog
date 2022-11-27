from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class HomepageTest(SimpleTestCase):
    
    def test_url_exist_on_exact_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, 'Home')
