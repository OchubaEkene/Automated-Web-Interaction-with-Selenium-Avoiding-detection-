# Import necessary libraries
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# List of user-agents
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/89.0"
]

# Randomly select a user-agent and window size
selected_user_agent = random.choice(user_agents)
window_sizes = [(1920, 1080), (1280, 800), (1440, 900)]
selected_window_size = random.choice(window_sizes)

# Create an Options object and set the user agent
options = Options()
options.add_argument(f"user-agent={selected_user_agent}")
options.add_argument(f"--window-size={selected_window_size[0]},{selected_window_size[1]}")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--headless")  # Run in headless mode

# Path to webdriver
driver_path = r'C:\Users\Tester\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
service = Service(driver_path)

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Remove the webdriver property to avoid detection
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


# Function to wait for page to fully load
def wait_for_any_text_in_span(driver, locator, texts):
    wait = WebDriverWait(driver, 10)
    for text in texts:
        try:
            element = wait.until(EC.text_to_be_present_in_element(locator, text))
            return element
        except Exception as e:
            print(f"Text '{text}' not found yet. Waiting...")


# Function to simulate human-like mouse movements
def human_like_mouse_move(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    for _ in range(10):
        x_offset = random.randint(-10, 10)
        y_offset = random.randint(-10, 10)
        actions.move_by_offset(x_offset, y_offset)
        time.sleep(0.1)
    actions.perform()


# Function to introduce random delays
def random_delay():
    delay = random.uniform(1.0, 3.0)  # Random delay between 1 to 3 seconds
    time.sleep(delay)


# Function to simulate scrolling
def simulate_scroll(driver):
    scroll_amount = random.randint(500, 1000)  # Random scroll amount
    driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
    time.sleep(0.5)  # Small delay after scrolling


try:
    driver.get("https://www.browserscan.net/")
    random_delay()  # Introduce a random delay
    simulate_scroll(driver)  # Simulate Scrolling
    print("Page title:", driver.title)  # Print page title to verify if page loaded
except Exception as e:
    print("Error occurred:", str(e))

# Wait for the page to fully load
span_locator = (By.CSS_SELECTOR, "div._1b07lqw span")
wait_for_any_text_in_span(driver, span_locator, ["No", "Yes"])

# You can modify this part to interact with an actual element if necessary
# For demonstration, we'll move the mouse over the page's body
body = driver.find_element(By.TAG_NAME, "body")
human_like_mouse_move(driver, body)
random_delay()

# Take a screenshot to verify the headless browser operation
driver.save_screenshot("screenshot.png")

driver.quit()
