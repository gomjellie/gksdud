import unittest

import boilerplate


class BoilerPythonTest(unittest.TestCase):
    """
        Sample Test
    """

    def test_print_string(self):
        """
        Test result of python script boilerplate.print_string("print") equals "print"

        """

        self.assertEqual(boilerplate.print_string("print"), "print")

    def test_login(self):
        """
        Test result of python script boilerplate.login("adam", "smith") equals success dictionary

        """

        self.assertEqual(boilerplate.login("adam", "smith"), {
            'result': 'success',
            'msg': 'log in success',
            'status-code': 200,
        })

    def test_login_fail(self):
        """
        Test result of python script boilerplate.login("adam", "smith") equals success dictionary

        """

        self.assertNotEqual(boilerplate.login("black", "smith"), {
            'result': 'success',
            'msg': 'log in success',
            'status-code': 200,
        })


if __name__ == '__main__':
    unittest.main()
