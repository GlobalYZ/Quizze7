from unittest import TestCase

from muyang_and_nicole import replace_all
class Test(TestCase):
    def test_replace_all_output_is_created(self):
        replace_all("test.txt", "output.txt", "cat", "dog")
        with open("output.txt") as result:
            content = result.read()
        expected_value = True
        if result:
            actual_value = True
        else:
            actual_value = False
        self.assertEqual(expected_value, actual_value)

    def test_replace_all_output_no_search_term(self):
        replace_all("test.txt", "output.txt", "cat", "dog")
        with open("output.txt") as result:
            content = result.read()
            actual_value = "cat" in result
        expected_value = False
        self.assertEqual(expected_value, actual_value)

    def test_replacement_words_are_present(self):
        replace_all("test.txt", "output.txt", "lovers", "haters")
        with open("output.txt") as file_object:
            content = file_object.read()
        self.assertEqual(True, "haters" in content)

    def test_no_replacements(self):
        self.assertEqual(0, replace_all("test.txt", "output.txt", "dogs", "cats"))

    def test_correct_number_replacements(self):
        self.assertEqual(2, replace_all("test.txt", "output.txt", "are", "aren't"))