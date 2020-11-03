from practical import *
import io


def test_unique_words():
    """
    A test to ensure that the word the appears 1457 times
    """
    word = 'the'
    count = 1457
    filename = "shawshank.txt"

    word_dict = unique_words(filename)

    assert(word_dict != None)
    assert(word in word_dict)
    assert(word_dict[word] == count)


def test_search_word(capsys, monkeypatch):
    word = "wall"
    expected_count = 42
    filename = "shawshank.txt"
    monkeypatch.setattr('sys.stdin', io.StringIO(word + "\n"))

    word_dict = unique_words(filename)
    search_word(word_dict)

    capture = capsys.readouterr()

    assert(capture.out == "Enter a word: " + word + " appeared " + str(expected_count) + " times.\n")


def test_search_word_not_in_dict(capsys, monkeypatch):
    word = "not a word"
    expected_count = 0
    filename = "shawshank.txt"
    monkeypatch.setattr('sys.stdin', io.StringIO(word + "\n"))

    word_dict = unique_words(filename)
    search_word(word_dict)

    capture = capsys.readouterr()

    assert(capture.out == "Enter a word: " + word + " appeared " + str(expected_count) + " times.\n")