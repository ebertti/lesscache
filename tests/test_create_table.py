from unittest import TestCase

from moto import mock_dynamodb2

from lesscache.dynamodb import create_table, get_dynamodb
from lesscache.settings import Settings


@mock_dynamodb2
class TestCreateTable(TestCase):

    def test_create_table_simple(self):

        settings = Settings(
            aws_region_name='us-east-1',
            table_name='test_less',
        )
        dynamodb = get_dynamodb(settings)

        table = create_table(settings, dynamodb)
        self.assertEqual(table.table_name, 'test_less')
        self.assertEqual(table.table_status, 'ACTIVE')
