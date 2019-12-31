import unittest

import gksdud


class BoilerPythonTest(unittest.TestCase):
    """
        Sample Test
    """

    def test_py_kor2eng(self):
        """
        gksdud.kor2eng("한영") should be "gksdud"

        """

        self.assertEqual(gksdud.kor2eng("한영"), "gksdud")

    def test_py_eng2kor(self):
        """
        gksdud.eng2kor("dudgks") should be "영한"

        """

        self.assertEqual(gksdud.kor2eng("dudgks"), "영한")

    def test_py_util_compose(self):
        """
        gksdud.utils.compose(['ㅎ', 'ㅏ', 'ㄴ']) should be "한"

        :return:
        """
        self.assertEqual(
            gksdud.utils.compose(['ㅎ', 'ㅏ', 'ㄴ']),
            "한",
        )

    def test_py_util_decompose(self):
        """
        gksdud.utils.decompose("한") should be  ['ㅎ', 'ㅏ', 'ㄴ']

        :return:
        """
        self.assertEqual(
            gksdud.utils.decompose("한"),
            ['ㅎ', 'ㅏ', 'ㄴ'],
        )


if __name__ == '__main__':
    unittest.main()
