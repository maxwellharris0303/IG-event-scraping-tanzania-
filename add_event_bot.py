from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import re
import match_words


USERNAME = "chiefdontrun56@gmail.com"
PASSWORD = "maxwell24"

def main(event_name, description, amenities, offerings, accessibilties, music_policy, price, phone_number, website, email_address, instagram_url):
    driver = webdriver.Chrome()
    driver.get("https://nakuja.com/auth/")

    username_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=\"login_username\"]")))
    username_input.send_keys(USERNAME)
    password_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name=\"login_password\"]")))
    password_input.send_keys(PASSWORD)

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]")
    login_button.click()
    sleep(5)

    driver.get("https://nakuja.com/create-events-2-2/")
    event_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder=\"Event name\"]")))
    event_name_input.send_keys(event_name)

    description_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id=\"content\"]")))
    driver.execute_script("arguments[0].innerHTML = arguments[1]", description_input.find_element(By.TAG_NAME, "p"), description)
    sleep(3)
    description_input.send_keys(Keys.TAB)

    event_category_parent = driver.find_element(By.CSS_SELECTOR, "div[class=\"ts-form-group field-key-taxonomy\"]")
    event_category_element = event_category_parent.find_element(By.TAG_NAME, "div")
    event_category_element.click()

    event_category_list = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"simplify-ul ts-term-dropdown-list\"]")))
    event_category_list.find_element(By.TAG_NAME, "li").click()

    next_step_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-next ts-btn ts-btn-1 ts-btn-large form-btn\"]")
    driver.execute_script("arguments[0].scrollIntoView(true);", next_step_button)
    next_step_button.click()
    sleep(2)



    current_dir = os.getcwd()
    print(current_dir)
    file_path = os.path.join(current_dir, "image.jpg")
    print(file_path)

    file_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"file\"]")
    file_input.send_keys(file_path)

    next_step_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-next ts-btn ts-btn-1 ts-btn-large form-btn\"]")
    driver.execute_script("arguments[0].scrollIntoView(true);", next_step_button)
    next_step_button.click()
    sleep(2)

    amenities_parent = driver.find_element(By.CSS_SELECTOR, "div[class=\"ts-form-group field-key-amenities\"]")
    amenities_parent = amenities_parent.find_element(By.TAG_NAME, "div")
    amenities_parent.click()

    amenities_list_parent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"simplify-ul ts-term-dropdown-list\"]")))
    amenities_list = amenities_list_parent.find_elements(By.TAG_NAME, "li")
    print(len(amenities_list))
    for list in amenities_list:
        print(list.text)
        for amenity in amenities:
            if list.text == amenity:
                list.click()
                break
        # sleep(0.2)
    save_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-btn ts-btn-2\"]")
    save_button.click()

    offerings_parent = driver.find_element(By.CSS_SELECTOR, "div[class=\"ts-form-group field-key-offerings\"]")
    offerings_parent = offerings_parent.find_element(By.TAG_NAME, "div")
    offerings_parent.click()

    offerings_list_parent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"simplify-ul ts-term-dropdown-list\"]")))
    offerings_list = offerings_list_parent.find_elements(By.TAG_NAME, "li")
    print(len(offerings_list))
    for list in offerings_list:
        print(list.text)
        for offering in offerings:
            if list.text == offering:
                list.click()
                break
        # sleep(0.2)
    save_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-btn ts-btn-2\"]")
    save_button.click()

    accessibilty_parent = driver.find_element(By.CSS_SELECTOR, "div[class=\"ts-form-group field-key-accessibility\"]")
    accessibilty_parent = accessibilty_parent.find_element(By.TAG_NAME, "div")
    driver.execute_script("arguments[0].scrollIntoView(true);", accessibilty_parent)
    accessibilty_parent.click()

    accessibilty_list_parent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"simplify-ul ts-term-dropdown-list\"]")))
    accessibilty_list = accessibilty_list_parent.find_elements(By.TAG_NAME, "li")
    print(len(accessibilty_list))

    for list in accessibilty_list:
        print(list.text)
        for accessibilty in accessibilties:
            matches = match_words.find_matching_words(list.text, accessibilty)
            if len(matches) != 0:
                list.click()
                break
        # sleep(0.2)
    save_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-btn ts-btn-2\"]")
    save_button.click()

    music_policy_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"Who plays the music?\"]")
    music_policy_input.send_keys(music_policy)

    next_step_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-next ts-btn ts-btn-1 ts-btn-large form-btn\"]")
    driver.execute_script("arguments[0].scrollIntoView(true);", next_step_button)
    next_step_button.click()
    sleep(2)

    event_date_parent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"ts-form-group field-key-event_date\"]")))
    event_date_parent.find_element(By.CSS_SELECTOR, "a[class=\"ts-repeater-add ts-btn ts-btn-4\"]").click()
    sleep(0.5)
    event_date_parent.find_element(By.CSS_SELECTOR, "div[class=\"ts-form-group\"]").click()
    driver.find_element(By.CSS_SELECTOR, "button[class=\"pika-button pika-day\"]").click()

    next_step_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-next ts-btn ts-btn-1 ts-btn-large form-btn\"]")
    driver.execute_script("arguments[0].scrollIntoView(true);", next_step_button)
    next_step_button.click()
    sleep(2)


    pricing_parent = driver.find_element(By.CSS_SELECTOR, "div[class=\"ts-form-group field-key-taxonomy-2\"]")
    pricing_parent = pricing_parent.find_element(By.TAG_NAME, "div")
    pricing_parent.click()

    pricing_list_parent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"simplify-ul ts-term-dropdown-list\"]")))
    pricing_list = pricing_list_parent.find_elements(By.TAG_NAME, "li")
    print(len(pricing_list))
    for list in pricing_list:
        print(list.text)
        if list.text.lower() in price.lower():
            list.click()
    try:
        save_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-btn ts-btn-2\"]")
        save_button.click()
    except:
        pass


    if "free" not in price.lower():
        currency_parent = driver.find_element(By.CSS_SELECTOR, "div[class=\"ts-form-group field-key-currency\"]")
        currency_parent.find_element(By.TAG_NAME, "div").click()

        currency_list_parent = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[class=\"simplify-ul ts-term-dropdown-list\"]")))
        currency_list = currency_list_parent.find_elements(By.TAG_NAME, "li")
        print(len(currency_list))
        for list in currency_list:
            print(list.text)
            if list.text.lower() in price.lower():
                list.click()

        try:
            save_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-btn ts-btn-2\"]")
            save_button.click()
        except:
            pass

        numbers = re.findall(r'\d+', price)
        result = ''.join(numbers)

        print(result)  # Output: 10000
        amount_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"How much is the entrance/ticket fee?\"]")
        amount_input.send_keys(result)

        ticket_available_parent = driver.find_element(By.CSS_SELECTOR, "div[class=\"ts-form-group switcher-label field-key-switcher\"]")
        ticket_switch = ticket_available_parent.find_element(By.CSS_SELECTOR, "div[class=\"switch-slider\"]")
        ticket_switch.click()

    next_step_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-next ts-btn ts-btn-1 ts-btn-large form-btn\"]")
    driver.execute_script("arguments[0].scrollIntoView(true);", next_step_button)
    next_step_button.click()
    sleep(2)

    # location_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"Location\"]")
    # location_input.send_keys(locaton)

    next_step_button = driver.find_element(By.CSS_SELECTOR, "a[class=\"ts-next ts-btn ts-btn-1 ts-btn-large form-btn\"]")
    driver.execute_script("arguments[0].scrollIntoView(true);", next_step_button)
    next_step_button.click()
    sleep(2)



    phone_nuber_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"Phone\"]")
    phone_nuber_input.send_keys(phone_number)

    def validate_website(url):
        # Basic URL pattern
        url_pattern = re.compile(
            r'^(https?://)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(/[\w-]*)*/?$'
        )
        return re.match(url_pattern, url) is not None

    is_valid_website = validate_website(website)

    def validate_email(email):
        # Basic email pattern
        email_pattern = re.compile(
            r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        )
        return re.match(email_pattern, email) is not None

    is_valid_email = validate_email(email_address)

    if is_valid_website:
        website_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"Website\"]")
        website_input.send_keys(website)
    if is_valid_email:
        email_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"Email\"]")
        email_input.send_keys(email_address)

    instagram_url_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"Instagram URL\"]")
    instagram_url_input.send_keys(instagram_url)

    sleep(2)
    save_as_draft_button = driver.find_element(By.CSS_SELECTOR, "a[data-tooltip=\"Save as draft\"]")
    save_as_draft_button.click()
    sleep(7)