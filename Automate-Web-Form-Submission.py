from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def submit_form(url, form_data):
    # Initialize the WebDriver (ensure the driver executable is in PATH)
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        # Fill in the form fields
        for field_id, value in form_data.items():
            element = driver.find_element(By.ID, field_id)
            element.clear()
            element.send_keys(value)
        
        # Submit the form (assuming there's a submit button with ID 'submit')
        submit_button = driver.find_element(By.ID, 'submit')
        submit_button.click()
        
        time.sleep(2)  # Wait for submission to process
        print("Form submitted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://www.example.com/form"
    form_data = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "message": "Automating form submission with Python!",
    }
    submit_form(url, form_data)
