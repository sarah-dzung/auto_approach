from selenium import webdriver
import json
from selenium.webdriver.chrome.options import Options as ChromeOptions

def save(driver: webdriver) -> None:
    # Save session information for later use
    executor_url = driver.command_executor._url
    session_id = driver.session_id

    session_info = {'executor_url': executor_url, 'session_id': session_id}
    with open('session_info.txt', 'w') as file:
        json.dump(session_info, file)

def reconnect() -> webdriver:
    # Reconnect to the existing session
    with open('session_info.txt', 'r') as file:
        session_info = json.load(file)

    options = ChromeOptions()

    driver = webdriver.Remote(command_executor=session_info['executor_url'], options=options)
    driver.session_id = session_info['session_id']
    return driver


