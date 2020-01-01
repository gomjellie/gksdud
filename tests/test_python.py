import unittest

import gksdud


class InterfaceTest(unittest.TestCase):
    """
        Interface Test
    """

    @unittest.skip("밑의 utils 가 먼저 구현되어야 가능함")
    def test_py_kor2eng(self):
        """
        gksdud.kor2eng("한영") should be "gksdud"

        """

        self.assertEqual(gksdud.kor2eng("한영"), "gksdud")

    @unittest.skip("밑의 utils 가 먼저 구현되어야 가능함")
    def test_py_eng2kor(self):
        """
        gksdud.eng2kor("dudgks") should be "영한"

        """

        self.assertEqual(gksdud.kor2eng("dudgks"), "영한")


class UtilsTest(unittest.TestCase):
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

    def test_py_util_compose_sentence(self):
        self.assertEqual(
            gksdud.utils.compose_sentence(["ㅁ", "ㅝ", "ㄴ", "", "ㄷ", "ㅔ", "", "ㅋ", "ㅋ", "ㅋ"]),
            "뭔데ㅋㅋㅋ"
        )

    def test_py_util_decompose_sentence(self):
        self.assertEqual(
            gksdud.utils.decompose_sentence("뭔데ㅋㅋㅋ"),
            ["ㅁ", "ㅝ", "ㄴ", "", "ㄷ", "ㅔ", "", "ㅋ", "ㅋ", "ㅋ"]
        )


if __name__ == '__main__':
    unittest.main()
