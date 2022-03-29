import unittest
from array import array

import azure.functions as func
from array_sum import main

class TestFunction(unittest.TestCase):
    def test_array_sum(self):
        # Construct a mock HTTP request.
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/array_sum',
            params={'value': [1, 2, 3, 4, 5]}
            )

        # Call the function.
        resp = main(req)

        # Check the output.
        self.assertEqual(
            resp.get_body(),
            b'1+2+3+4+5 = 15',
        )
test_array = TestFunction()
test_array.test_array_sum()