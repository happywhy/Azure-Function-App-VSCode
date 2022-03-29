# <project_root>/tests/test_my_first_function.py
import unittest

import azure.functions as func
from double_value import main

class TestFunction(unittest.TestCase):
    def test_double_value(self):
        # Construct a mock HTTP request.
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/double_value',
            params={'value': '21'})

        # Call the function.
        resp = main(req)

        # Check the output.
        self.assertEqual(
            resp.get_body(),
            b'21 * 2 = 42',
        )