from django.test import TestCase, Client
from django.urls import reverse

class MainTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_main_url_is_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_main_using_main_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_main_contains_correct_data(self):
        response = self.client.get('/')
        self.assertContains(response, 'PlayMax Sport Station')
        self.assertContains(response, 'Muhammad Alfa Mubarok')
        self.assertContains(response, 'PBP D')
        self.assertContains(response, 'Adidas Adizero Evo SL')
        self.assertContains(response, '2600000')
        self.assertContains(response, 'Boost ur running performance')
        self.assertContains(response, 'Running Shoes')