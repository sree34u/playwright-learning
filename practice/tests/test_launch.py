from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        page.goto("https://www.wikipedia.org")

        english_link = page.locator("a#js-link-box-en")
        english_link.wait_for()
        english_link.click()

        page.wait_for_load_state("load")

        print(f"The page title is: {page.title()}.")
        browser.close()

if __name__ == "__main__":
    run()
 