from pytest import raises
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    string = "srt"
    number = 123

    with raises(TypeError, match="tipo inválido para message"):
        encrypt_message(number, number)

    with raises(TypeError, match="tipo inválido para key"):
        encrypt_message(string, string)

    message = "52050"

    key_case2 = 3
    assert encrypt_message(message, key_case2) == "025_05"

    key_case1 = 4
    assert encrypt_message(message, key_case1) == "0_5025"

    key_case3 = -1
    assert encrypt_message(message, key_case3) == "05025"
