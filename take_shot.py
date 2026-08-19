from playwright.sync_api import sync_playwright
import time

def take_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # iPhone 12 viewport
        context = browser.new_context(
            viewport={'width': 390, 'height': 844},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
        )
        page = context.new_page()
        page.goto('http://localhost:8501', timeout=60000)
        time.sleep(5) # wait for streamlit to render
        page.screenshot(path='mobile_screenshot.png', full_page=True)
        browser.close()

if __name__ == '__main__':
    take_screenshot()
