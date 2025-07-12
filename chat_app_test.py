from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://app65656565.pythonanywhere.com/chat")
    driver.maximize_window()
    time.sleep(2)

    input_box = driver.find_element(By.ID, "chat-input-box")  # Replace with actual ID
    input_box.send_keys("Hello from automation!")
    input_box.send_keys(Keys.ENTER)

    time.sleep(2)
    chat_area = driver.find_element(By.ID, "chat-container")  # Replace with actual ID
    if "Hello from automation!" in chat_area.text:
        print("✅ Test Passed: Message is displayed in chat.")
    else:
        print("❌ Test Failed: Message not found in chat area.")

except Exception as e:
    print(f"❌ Test Error: {e}")

finally:
    time.sleep(2)
    driver.quit()
