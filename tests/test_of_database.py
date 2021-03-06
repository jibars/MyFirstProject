import unittest
import time
from mock import patch, Mock, MagicMock
import functions.repository as repository


class BasicDatabaseTests(unittest.TestCase):

    def setUp(self):
        self.repository = repository.postgres_repository(user = 'root', host = 'localhost', port = '5433', database = 'test', password = '123456').connect()

    def tearDown(self):
        self.repository.close()

    def test_postgres_repository(self):
        postgres = self.repository
        postgres.delete("DROP TABLE IF EXISTS stores")
        postgres.create("CREATE TABLE stores (store_id serial, name varchar(100), email varchar(100), phone varchar(100))")
        postgres.post("INSERT INTO stores VALUES(62126, 'Moviles Android Baratos', 'ventas@movilesandroidbaratos.com', '672616995')")
        expected = [(62126, 'Moviles Android Baratos', 'ventas@movilesandroidbaratos.com', '672616995')]
        result = postgres.get("SELECT store_id, name, email, phone FROM stores WHERE store_id=62126")

        self.assertEqual(expected, result)

    @patch('functions.repository.postgres_repository')
    def test_mock_get(self, mock_class):
        repository_mock = mock_class(user = 'jibars', host = 'localhost', port = '5432', database = 'test')
        repository_mock.get.return_value = [(62126, 'Moviles Android Baratos', 'ventas@movilesandroidbaratos.com', '672616995')]

        response = repository_mock.get("SELECT store_id, name, email, phone FROM stores WHERE store_id=62126")

        self.assertIsNotNone(response)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], tuple)
