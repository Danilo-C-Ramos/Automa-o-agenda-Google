from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    firefox = playwright.firefox # or "firefox" or "webkit".
    browser = firefox.launch()
    page = browser.new_page()
    page.goto("https://calendar.google.com/calendar/u/0/r")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)