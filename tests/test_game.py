from hungman import hungman


def test_oleg_1(capsys):
    word = 'oleg'
    input_values = ['o', 'l', 'e', 'g']

    def mock_input(s):
        # print(s)
        return input_values.pop(0)

    hungman.input = mock_input
    assert hungman.play(word) is True


def test_oleg_2(capsys):
    word = 'oleg'
    input_values = ['o', 'l', 'd', 'e', 'k', 'g']

    def mock_input(s):
        # print(s)
        return input_values.pop(0)

    hungman.input = mock_input
    assert hungman.play(word) is True


def test_wrong_oleg(capsys):
    word = 'oleg'
    input_values = ['t', 'i', 'n', 'k', 'o', 'f', 'f']

    def mock_input(s):
        # print(s)
        return input_values.pop(0)

    hungman.input = mock_input
    assert hungman.play(word) is False
