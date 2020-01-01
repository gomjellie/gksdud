import unittest
from click.testing import CliRunner

import gksdud


class CliTest(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    @classmethod
    def output2str(cls, output):
        return output.replace('\n', '')

    @unittest.skip("kor2eng 가 먼저 구현되어야 가능함")
    def test_cli_kor2eng(self):
        """
        Test output of CLI Command gksdud cli_kor2eng --string="한영" equals "gksdud"

        """

        result = self.runner.invoke(gksdud.cli.cli_kor2eng, ["--string", "한영"])
        self.assertEqual(
            self.output2str(result.output),
            "gksdud",
        )

    @unittest.skip("eng2kor 가 먼저 구현되어야 가능함")
    def test_cli_eng2kor(self):
        """
        Test output of CLI Command gksdud cli_eng2kor --string="dudgks" equals "영한"

        """

        result = self.runner.invoke(gksdud.cli.cli_eng2kor, ["--string", "dudgks"])
        self.assertEqual(
            self.output2str(result.output),
            "영한",
        )


if __name__ == '__main__':
    unittest.main()
