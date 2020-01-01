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
        test_inputs = [
            ["ㅎ", "ㅏ", "ㄴ"],
            ["ㄱ", "ㅡ", "ㄹ"],
            ["ㅌ", "ㅣ"],
            ["ㅁ", "ㅗ"],
            ["ㅂ", "ㅞ", "ㄺ"]
        ]

        test_expects = [
            "한", "글",
            "티", "모",
            "뷁",
        ]

        for test_input, test_expect in zip(test_inputs, test_expects):
            self.assertEqual(
                gksdud.utils.compose(test_input), test_expect
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
        test_inputs = [
            ["ㅁ", "ㅝ", "ㄴ", "", "ㄷ", "ㅔ", "", "ㅋ", "ㅋ", "ㅋ"],
            ["ㅇ", "ㅗ", "", "ㄴ", "ㅡ", "ㄹ", "", "ㅇ", "ㅢ", "", " ", "ㄴ", "ㅏ", "ㄹ", "", "ㅆ", "ㅣ", ""],
            ["ㅇ", "ㅙ", "", "?", "!"],
        ]
        test_expects = [
            "뭔데ㅋㅋㅋ",
            "오늘의 날씨",
            "왜?!",
        ]

        for test_input, test_expect in zip(test_inputs, test_expects):
            self.assertEqual(
                gksdud.utils.compose_sentence(test_input),
                test_expect
            )

    def test_py_util_decompose_sentence(self):
        self.assertEqual(
            gksdud.utils.decompose_sentence("뭔데ㅋㅋㅋ"),
            ["ㅁ", "ㅝ", "ㄴ", "", "ㄷ", "ㅔ", "", "ㅋ", "ㅋ", "ㅋ"]
        )


if __name__ == '__main__':
    unittest.main()
