import pytest
from string_utils import *

def test_count_vowels_standard(): assert count_vowels("Hello") == 2
def test_count_vowels_none():
    with pytest.raises(TypeError): count_vowels(None)

def test_reverse_string_standard(): assert reverse_string("abc") == "cba"
def test_reverse_string_none():
    with pytest.raises(TypeError): reverse_string(None)

def test_is_palindrome_standard(): assert is_palindrome("racecar") is True
def test_is_palindrome_phrase(): assert is_palindrome("A man a plan a canal Panama") is True
def test_is_palindrome_none():
    with pytest.raises(TypeError): is_palindrome(None)

def test_word_count_standard(): assert word_count("Hello World") == 2
def test_word_count_none():
    with pytest.raises(TypeError): word_count(None)

def test_capitalise_words_standard(): assert capitalise_words("hello world") == "Hello World"
def test_capitalise_words_none():
    with pytest.raises(TypeError): capitalise_words(None)

def test_remove_duplicates_standard(): assert remove_duplicates("aaabbbcc") == "abc"
def test_remove_duplicates_long(): assert remove_duplicates("aaaaa") == "a"
def test_remove_duplicates_none():
    with pytest.raises(TypeError): remove_duplicates(None)
def test_remove_duplicates_empty(): assert remove_duplicates("") == ""
