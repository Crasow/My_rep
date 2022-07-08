import unittest

from common_for_tests.client import presence, process_ans
from common_for_tests.vars import USER, STATUS_HERE, GUEST, \
    ACTION, PRESENCE, TIME, ACC_LOGIN, STATUS, RESPONSE, ERROR, \
    ERROR_TEXT


class TestClass(unittest.TestCase):
    """
    Класс с тестами
    """

    def test_def_presence(self):
        """Тест присутствие"""
        test = presence(GUEST, STATUS_HERE)
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1,
                                USER: {ACC_LOGIN: GUEST, STATUS: STATUS_HERE}})

    def test_OK_ans(self):
        ok_data = {RESPONSE: 200}
        test = process_ans(ok_data)
        self.assertEqual(test, '200 : OK')

    def test_error_ans(self):
        not_ok_data = {RESPONSE: 400,
                       ERROR: ERROR_TEXT}
        test = process_ans(not_ok_data)
        self.assertEqual(test, f'400 : {not_ok_data[ERROR]}')

    def test_no_response(self):
        self.assertRaises(ValueError, process_ans({}), {ERROR:'Bad Request'})


