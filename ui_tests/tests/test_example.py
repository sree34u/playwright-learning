from ui_tests.pages.example_page import ExamplePage

def test_example_page_title(page):
    example_page = ExamplePage(page)
    example_page.open()
    example_page.assert_title()

def test_example_page_heading(page):
    example_page = ExamplePage(page)
    example_page.open()
    example_page.assert_heading()