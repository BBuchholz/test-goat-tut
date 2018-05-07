from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # a user has heard about a new online to-do app, they go
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # they notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # they are invited to enter a to-do item straight away

        # they type "Do a django based tdd tutorial" into a text box 

        # When they hit enter, the page updates, and now the page lists
        # "1: Do a django based tdd tutorial" as an item in a to-do list

        # There is still a text box inviting them to add another item. They
        # enter "Adapt tutorial to a piece of an existing code base"

        # The page updates again, and now shows both items on their list

        # They wonder whether the site will remember their list. Then they see
        # that the site has generated a unique URL for them -- there is some
        # explanatory text to that effect.

        # They visit that URL - their to-do list is still there.

        # Satisfied, they go back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')

