from .constants import *


def compose(scattered_ko):
    """
    decompose 의 역함수
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
    compose 의 역함수
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


def is_complete_ko_word(candidate):
    """

    :param candidate:
    :return:
    """
    if '가' > candidate or candidate > '힣':
        return False

    return True


def compose_sentence(scattered_ko):
    """
    ["ㅁ", "ㅝ", "ㄴ", "", "ㄷ", "ㅔ", "", "ㅋ", "ㅋ", "ㅋ"] => 뭔데ㅋㅋㅋ

    :param scattered_ko: 분리된 한글 조각들, ㅋㅋㅋ 같은 온전하지 않은 연속된 입력이 주어지는 경우도 있다.
    :return:
    """
    pass


def decompose_sentence(complete_ko):
    """
    뭔데ㅋㅋㅋ => ["ㅁ", "ㅝ", "ㄴ", "", "ㄷ", "ㅔ", "", "ㅋ", "ㅋ", "ㅋ"]

    :param complete_ko: 완전한 한글 문장, ㅋㅋㅋ 같은 온전하게 완성되지 않은 글자가 포함될 수 있다.
    :return:
    """
    pass
