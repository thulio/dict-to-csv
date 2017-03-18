# dict-to-csv

[![Build Status](https://travis-ci.org/thulio/dict-to-csv.svg?branch=master)](https://travis-ci.org/thulio/dict-to-csv)

dict-to-csv transforms nested Python dictionaries into CSV lines.

Example:

```json
[{
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
```

```csv
customer.address.number,customer.address.street,customer.name,product.price,product.sku
42,Street 1,John,9.99,1
314,Street 2,Bob,15.0,2
```