from django.test import Client, TestCase

from ads_txt.models import Rule


class AdsTxtTest(TestCase):
    def setUp(self):
        self.client = Client()
        Rule.objects.create(
            domain='test.com',
            account_id='121243d',
            account_type='DIRECT',
            authority_id='',
        )

    def test_get_ads_txt(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get('content-type'), 'text/plain')
        self.assertIn('test.com', str(response.content))
