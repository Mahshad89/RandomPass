import unittest
from unittest.mock import patch
from io import StringIO
import sys
from RPG import (
    generate_password,
    generate_pronounceable_password,
    check_password_strength,
    generate_passphrase,
    save_passwords_to_file,
    main
)

class TestRPGFunctions(unittest.TestCase):

    def test_generate_password_default(self):
        password = generate_password()
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.islower() for char in password))

    def test_generate_password_custom_length(self):
        password = generate_password(length=16)
        self.assertEqual(len(password), 16)

    def test_generate_password_with_entropy(self):
        password = generate_password(entropy=3)  
        self.assertTrue(len(password) >= 5)

    def test_generate_pronounceable_password(self):
        pronounceable_password = generate_pronounceable_password(10)
        self.assertEqual(len(pronounceable_password), 10)

    def test_check_password_strength(self):
        strong_password = "Str0ngP@ssw0rd"
        weak_password = "weakpassword"
        
        strength_strong = check_password_strength(strong_password)
        strength_weak = check_password_strength(weak_password)

        self.assertEqual(strength_strong, 4)  # Contains uppercase, lowercase, digit, and special character
        self.assertEqual(strength_weak, 1)    # Contains lowercase characters

    def test_generate_passphrase(self):
        word_list = ["word1", "word2", "word3"]
        passphrase = generate_passphrase(word_list, num_words=3, delimiter=' ')
        self.assertEqual(len(passphrase.split(' ')), 3)


if __name__ == "__main__":
        unittest.main()


