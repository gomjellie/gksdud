import unittest

import gksdud


class BoilerPythonTest(unittest.TestCase):
    """
        Sample Test
    """

    def test_py_kor2eng(self):
        """
        Test result of python script gksdud.kor2eng("한영") equals "gksdud"

        """

        self.assertEqual(gksdud.kor2eng("한영"), "gksdud")

    def test_py_eng2kor(self):
        """
        Test result of python script gksdud.eng2kor("dudgks") equals "영한"

        """

        self.assertEqual(gksdud.kor2eng("dudgks"), "영한")


if __name__ == '__main__':
    unittest.main()
