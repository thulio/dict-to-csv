# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from dict_to_csv import extract_keys, transform


class TestExtractKeys(unittest.TestCase):
    def test_simple_data(self):
        data = [
            {
                'key_1': 'value 1',
                'key_2': 'value 2'
            },
            {
                'key_1': 'value 3',
                'key_2': 'value 4'
            }
        ]

        self.assertEqual(extract_keys(data), ['key_1', 'key_2'])

    def test_nested_data(self):
        data = [{
            "customer": {
                "name": "John",
                "address": {
                    "street": "Street 1",
                    "number": "42"
                }
            },
            "product": {
                "sku": "1",
                "price": 9.99
            }
        },
            {
                "customer": {
                    "name": "Bob",
                    "address": {
                        "street": "Street 2",
                        "number": "314"
                    }
                },
                "product": {
                    "sku": "2",
                    "price": 15.00
                }
            }
        ]

        self.assertEqual(extract_keys(data), ['customer.address.number', 'customer.address.street', 'customer.name',
                                              'product.price', 'product.sku'])


class TestTransform(unittest.TestCase):
    def test_simple_data(self):
        data = [
            {
                'key_1': 'value 1',
                'key_2': 'value 2'
            },
            {
                'key_1': 'value 3',
                'key_2': 'value 4'
            }
        ]

        self.assertEqual(transform(data), 'key_1,key_2\nvalue 1,value 2\nvalue 3,value 4\n')

    @unittest.skip("Can't make it work on Python 2")
    def test_non_ascii_data(self):
        data = [
            {
                'ã': 'joão',
                'key_2': 'value 2'
            },
            {
                'ã': 'value 3',
                'key_2': 'value 4'
            }
        ]

        self.assertEqual(transform(data), 'key_2,ã\nvalue 2,joão\nvalue 4,value 3\n')

    def test_nested_data(self):
        data = [{
            "customer": {
                "name": "John",
                "address": {
                    "street": "Street 1",
                    "number": "42"
                }
            },
            "product": {
                "sku": "1",
                "price": 9.99
            }
        },
            {
                "customer": {
                    "name": "Bob",
                    "address": {
                        "street": "Street 2",
                        "number": "314"
                    }
                },
                "product": {
                    "sku": "2",
                    "price": 15.00
                }
            }
        ]

        self.assertEqual(transform(data),
                         'customer.address.number,customer.address.street,customer.name,product.price,product.sku\n42,Street 1,John,9.99,1\n314,Street 2,Bob,15.0,2\n')

    def test_simple_data_missing_key_first(self):
        data = [
            {
                'key_1': 'value 1',
            },
            {
                'key_1': 'value 3',
                'key_2': 'value 4'
            }
        ]

        self.assertEqual(transform(data), 'key_1,key_2\nvalue 1,\nvalue 3,value 4\n')

    def test_simple_data_missing_key_other(self):
        data = [
            {
                'key_1': 'value 1',
                'key_2': 'value 2'
            },
            {
                'key_2': 'value 4'
            }
        ]

        self.assertEqual(transform(data), 'key_1,key_2\nvalue 1,value 2\n,value 4\n')

    def test_nested_data_missing_key_first(self):
        data = [{
            "customer": {
                "name": "John",
                "address": {
                    "street": "Street 1",
                    "number": "42"
                }
            },
            "product": {
                "price": 9.99
            }
        },
            {
                "customer": {
                    "name": "Bob",
                    "address": {
                        "street": "Street 2",
                        "number": "314"
                    }
                },
                "product": {
                    "sku": "2",
                    "price": 15.00
                }
            }
        ]

        self.assertEqual(transform(data),
                         'customer.address.number,customer.address.street,customer.name,product.price,product.sku\n42,Street 1,John,9.99,\n314,Street 2,Bob,15.0,2\n')

    def test_nested_data_missing_key_other(self):
        data = [{
            "customer": {
                "name": "John",
                "address": {
                    "street": "Street 1",
                    "number": "42"
                }
            },
            "product": {
                "sku": "1",
                "price": 9.99
            }
        },
            {
                "customer": {
                    "name": "Bob",
                    "address": {
                        "street": "Street 2",
                        "number": "314"
                    }
                },
                "product": {
                    "price": 15.00
                }
            }
        ]

        self.assertEqual(transform(data),
                         'customer.address.number,customer.address.street,customer.name,product.price,product.sku\n42,Street 1,John,9.99,1\n314,Street 2,Bob,15.0,\n')

    def test_simple_data_without_header(self):
        data = [
            {
                'key_1': 'value 1',
                'key_2': 'value 2'
            },
            {
                'key_1': 'value 3',
                'key_2': 'value 4'
            }
        ]

        self.assertEqual(transform(data, include_headers=False), 'value 1,value 2\nvalue 3,value 4\n')
