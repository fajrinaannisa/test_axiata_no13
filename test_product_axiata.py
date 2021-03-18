import requests
import unittest
import random
import json
# Library Modul tersedia di requirements.txt

class TestAxiataProduct(unittest.TestCase):
    """
    Test Automation API
    - Create Product
    - Detail Product
    - Update Product
    - Delete Product
    """

    def api_create_product(self):
        form_data = dict(
            name="Piano YAMAHA",
            messsage="mahal pianonya",
            description="Beli nya di Jogja",
            image="drive.google.com/rinafajrina/fotopianoyamaha",
            price=873500,
            status=False
        )

        link_url = 'https://gorest.co.in/public-api/products'
        authorize = {
            "Authorization" : "Bearer e3479c4068b18c10ce220f5665f1c206bff27b3e9a722bcc35cf52e36708a1fb"
        }

        request_create_product = requests.post(link_url, data=form_data, headers=authorize)
        response = request_create_product.json()

        return response

    def api_detail_product(self, product_id):
        link_url = 'https://gorest.co.in/public-api/products'

        parameters = dict(
            id=int(product_id)
        )

        request_detail_product = requests.get(link_url, params=parameters)
        response = request_detail_product.json()

        return response

    def api_update_product(self, product_id, discount_amount):
        parameters = dict(
            discount_amount=discount_amount,
            status=True
        )

        link_url = 'https://gorest.co.in/public-api/products/{}'.format(str(product_id))
        authorize = {
            "Authorization" : "Bearer e3479c4068b18c10ce220f5665f1c206bff27b3e9a722bcc35cf52e36708a1fb"
        }

        request_update_product = requests.put(link_url, data=parameters, headers=authorize)
        response = request_update_product.json()

        return response

    def api_delete_product(self, product_id):
        link_url = 'https://gorest.co.in/public-api/products/{}'.format(str(product_id))
        authorize = {
            "Authorization" : "Bearer e3479c4068b18c10ce220f5665f1c206bff27b3e9a722bcc35cf52e36708a1fb"
        }

        request_update_product = requests.delete(link_url, headers=authorize)
        response = request_update_product.json()

        return response

    def test_axiata_create_product(self):
        request_create_product = self.api_create_product()

        # response output harus 201
        self.assertEqual(request_create_product['code'], 201)

    def test_axiata_detail_product(self):
        request_create_product = self.api_create_product()
        request_detail_product = self.api_detail_product(product_id=int(request_create_product['data']['id']))
        
        # response output harus isi detail product
        self.assertEqual(request_create_product['data']['name'], request_detail_product['data'][0]['name'])
        self.assertEqual(request_create_product['data']['price'], request_detail_product['data'][0]['price'])
        self.assertEqual(request_create_product['data']['status'], request_detail_product['data'][0]['status'])
        self.assertEqual(request_create_product['data']['image'], request_detail_product['data'][0]['image'])
        self.assertEqual(request_create_product['data']['description'], request_detail_product['data'][0]['description'])

    def test_axiata_update_product(self):
        request_create_product = self.api_create_product()

        discount_amount = random.randint(1000,50000)

        request_update_product = self.api_update_product(product_id=int(request_create_product['data']['id']), discount_amount=discount_amount)

        # response output harus isi ter update product discount amount
        self.assertEqual(request_create_product['data']['name'], request_update_product['data']['name'])
        self.assertEqual(int(float(request_update_product['data']['discount_amount'])), discount_amount)
        self.assertEqual(request_create_product['data']['description'], request_update_product['data']['description'])

    def test_axiata_delete_product(self):
        request_create_product = self.api_create_product()

        discount_amount = random.randint(1000,50000)

        request_update_product = self.api_update_product(product_id=int(request_create_product['data']['id']), discount_amount=discount_amount)
        
        delete_product = self.api_delete_product(product_id=int(request_update_product['data']['id']))

        # response output harus 204
        self.assertEqual(delete_product['code'], 204)

if __name__ == '__main__':
    unittest.main()