from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from time import sleep

# LOCATION = "Havoc at 4th Floor Renaissance Plaza, 498 Haile Selassie Road, Masaki, Tanzania"

# Selenium Wire configuration to use a proxy
PROXY_USERNAME = "14a51f7dce1cf"
PROXY_PASSWORD = "e041b7ba43"
PROXY_HOST = "89.42.81.219"
PROXY_PORT = "12323"
seleniumwire_options = {
    'proxy': {
        'http': f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}',
        'verify_ssl': False,
    },
}

driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options)
driver.maximize_window()
driver.get("https://www.google.com/maps")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"searchboxinput\"]")))

def scrape_google_maps(location):
    location_url = ""
    accessibility = []
    amenities = []
    offers = []
    try:
        input_keyword = driver.find_element(By.CSS_SELECTOR, "input[id=\"searchboxinput\"]")
        input_keyword.clear()
        input_keyword.send_keys(location)
        input_keyword.send_keys(Keys.RETURN)
        # Allow the page to load
        sleep(10)

        input_keyword = driver.find_element(By.CSS_SELECTOR, "input[id=\"searchboxinput\"]")
        redirected_keyword = input_keyword.get_attribute('value')
        print(redirected_keyword)

        if redirected_keyword != location:
            input_keyword = driver.find_element(By.CSS_SELECTOR, "input[id=\"searchboxinput\"]")
            input_keyword.clear()
            input_keyword.send_keys(location)
            input_keyword.send_keys(Keys.RETURN)

        sleep(5)

        
        try:
            input_keyword = driver.find_element(By.CSS_SELECTOR, "input[id=\"searchboxinput\"]")
            redirected_keyword = input_keyword.get_attribute('value')
            if redirected_keyword != "":
                location_url = driver.current_url
            driver.find_element(By.CSS_SELECTOR, "div[class=\"Gpq6kf fontTitleSmall\"]")
            title_elements = driver.find_elements(By.CSS_SELECTOR, "div[class=\"Gpq6kf fontTitleSmall\"]")
            for title_element in title_elements:
                if "About" in title_element.text:
                    title_element.click()
            
        except:
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"hfpxzc\"]")))
                driver.find_element(By.CSS_SELECTOR, "a[class=\"hfpxzc\"]").click()
                sleep(3)
                input_keyword = driver.find_element(By.CSS_SELECTOR, "input[id=\"searchboxinput\"]")
                redirected_keyword = input_keyword.get_attribute('value')
                if redirected_keyword != "":
                    location_url = driver.current_url
                
                title_elements = driver.find_elements(By.CSS_SELECTOR, "div[class=\"Gpq6kf fontTitleSmall\"]")
                for title_element in title_elements:
                    if "About" in title_element.text:
                        title_element.click()

            except:
                pass
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class=\"iP2t7d fontBodyMedium\"]")))
        info_elements = driver.find_elements(By.CSS_SELECTOR, "div[class=\"iP2t7d fontBodyMedium\"]")
        print(len(info_elements))

        amenities = []
        accessibility = []
        offers = []
        for info_element in info_elements:
            title = info_element.find_element(By.TAG_NAME, "h2").text
            print(title)
            if title.lower() == "accessibility":
                accessibility_items = info_element.find_elements(By.TAG_NAME, "li")
                for item in accessibility_items:
                    accessibility.append(item.text)

            if title.lower() == "amenities":
                amenities_items = info_element.find_elements(By.TAG_NAME, "li")
                for item in amenities_items:
                    amenities.append(item.text)
            
            if title.lower() == "highlights":
                amenities_items = info_element.find_elements(By.TAG_NAME, "li")
                for item in amenities_items:
                    amenities.append(item.text)

            if title.lower() == "service options":
                amenities_items = info_element.find_elements(By.TAG_NAME, "li")
                for item in amenities_items:
                    amenities.append(item.text)  

            if title.lower() == "payments":
                amenities_items = info_element.find_elements(By.TAG_NAME, "li")
                for item in amenities_items:
                    amenities.append(item.text)

            if title.lower() == "children":
                amenities_items = info_element.find_elements(By.TAG_NAME, "li")
                for item in amenities_items:
                    amenities.append(item.text)

            if title.lower() == "parking":
                amenities_items = info_element.find_elements(By.TAG_NAME, "li")
                for item in amenities_items:
                    amenities.append(item.text)

            if title.lower() == "offerings":
                offers_items = info_element.find_elements(By.TAG_NAME, "li")
                for item in offers_items:
                    offers.append(item.text)

            if title.lower() == "dining options":
                offers_items = info_element.find_elements(By.TAG_NAME, "li")
                for item in offers_items:
                    offers.append(item.text)
                    

        print(accessibility)
        print(amenities)
        print(offers)
    except:
        pass

    return location_url, accessibility, amenities, offers


# LOCATION = "THE CAMP JOINT, LOCATION : KIGAMBONI"
# print(scrape_google_maps(LOCATION))