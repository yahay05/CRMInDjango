from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.

class LandingPageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('landing-page'))
        self.assertTemplateUsed(response, 'landing.html')
        self.assertEqual(response.status_code, 200)
