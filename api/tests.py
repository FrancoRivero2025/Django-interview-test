import json
from techfixsolutions.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from techfixsolutions.models import Company


class CompanyListCreateAPIViewTestCase(APITestCase):
    url = reverse("company-list")

    def setUp(self):
        self.username = "user_test"
        self.email = "test@techfixsolutions.com"
        self.password = "Tech123"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_company(self):
        response = self.client.post(self.url,
                                    {
                                        "name": "company delete!",
                                        "phone": "123456789",
                                        "email": "test@techfixsolutions.com",
                                        "website": "http://www.test.com"
                                    }
                                    )
        self.assertEqual(201, response.status_code)

    def test_list_company(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(json.loads(response.content)) == Company.objects.count())
