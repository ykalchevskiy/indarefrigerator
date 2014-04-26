from tests import InDaTestCase


class ProductsPageTest(InDaTestCase):

    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
