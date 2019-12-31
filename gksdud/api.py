"""
    API HERE
"""


def kor2eng(kor_string):
    """
    한글 -> gksrmf
    :param kor_string: 온전한 한글 입력이 들어온다.
    :type kor_string: str
    :return: str
    """
    if type(kor_string) not in [str]:
        raise ValueError("kor2eng() got wrong arguments example_string")

    return kor_string


def eng2kor(eng_string):
    """
    gksrmf -> 한글
    :param eng_string: 한글로 입력되는줄 알고 영어 입력상태에서 입력한 스트링
    :type eng_string: str
    :type password: str
    :return:
    """

    if type(eng_string) not in [str]:
        raise ValueError("print_string() got wrong arguments example_string")

    return eng_string

