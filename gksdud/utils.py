from .constants import *


def compose(scattered_ko):
    """
    ["ㅎ", "ㅏ", "ㄴ"] => "한"

    :param scattered_ko: 분리된 한글 자모
    :type scattered_ko: list
    :return: 완성된 한 글자
    """
    return chr(
        KOREAN_OFF_SET
        + INITIAL.index(scattered_ko[0]) * INITIAL_OFF_SET
        + MEDIAL.index(scattered_ko[1]) * MEDIAL_OFF_SET
        + FINAL.index(scattered_ko[2])
    )


def decompose(complete_ko):
    """
    "한" => ["ㅎ", "ㅏ", "ㄴ"]

    :param complete_ko: 완전한 한 글자
    :type complete_ko: str
    :return: 분리된 한글 자모 (list)
    """
    if '가' > complete_ko or complete_ko > '힣':
        raise Exception("split_gks() got wrong parameter {}".format(complete_ko))

    unicode = ord(complete_ko)

    initial = (unicode - KOREAN_OFF_SET) // INITIAL_OFF_SET
    medial = ((unicode - KOREAN_OFF_SET) - (INITIAL_OFF_SET * initial)) // MEDIAL_OFF_SET
    final = (unicode - KOREAN_OFF_SET) - (INITIAL_OFF_SET * initial) - MEDIAL_OFF_SET * medial
    return [INITIAL[initial], MEDIAL[medial], FINAL[final]]


